"""
Configuration pytest partagée pour les tests du bot Discord Véronica.

=====================================================================
 GESTION DE LA BASE DE DONNÉES DE TEST — LIS-MOI
=====================================================================
Le projet ne dispose que d'UNE seule instance PostgreSQL (celle de prod).
Pour ne jamais risquer de toucher aux données réelles, cette suite :

  1. Se connecte au serveur Postgres (mêmes identifiants que la prod par
     défaut) via la base système "postgres".
  2. Y crée une base de données dédiée aux tests, nommée par défaut
     "<POSTGRES_DB>_test" (donc différente de la base de prod).
  3. Exécute `database_init.init_db()` dessus pour (re)créer tout le schéma.
  4. Fait tourner TOUS les tests sur cette base, jamais sur la prod.
  5. Supprime la base de test à la fin de la session (sauf si
     la variable d'environnement KEEP_TEST_DB=1 est positionnée).

Un garde-fou refuse de démarrer si le nom de la base de test est
identique à celui de la prod, ou ne contient pas "test".

Variables d'environnement reconnues (toutes optionnelles) :
  TEST_POSTGRES_HOST      (repli : POSTGRES_HOST, sinon "localhost")
  TEST_POSTGRES_PORT      (repli : 5432)
  TEST_POSTGRES_USER      (repli : POSTGRES_USER, sinon "postgres")
  TEST_POSTGRES_PASSWORD  (repli : POSTGRES_PASSWORD, sinon "password")
  TEST_POSTGRES_DB        (repli : "<POSTGRES_DB>_test")
  KEEP_TEST_DB=1          Conserve la base de test après la session (debug)

Le rôle Postgres utilisé doit avoir le droit CREATEDB (c'est le cas par
défaut du rôle "bootstrap" créé par l'image officielle postgres, celui
défini par POSTGRES_USER dans le docker-compose du projet).
"""
import os
import sys
from pathlib import Path

import asyncpg
import pytest_asyncio # type: ignore

# Permet d'importer les modules du projet (database_init, cogs.*, type_classes.*)
# peu importe le répertoire depuis lequel `pytest` est lancé.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import database_init  # noqa: E402
from cogs.tamagotchi import db_tamagotchi  # noqa: E402

# --- Paramètres de connexion -------------------------------------------------
PG_HOST = os.environ.get("TEST_POSTGRES_HOST", os.environ.get("POSTGRES_HOST", "localhost"))
PG_PORT = int(os.environ.get("TEST_POSTGRES_PORT", "5432"))
PG_USER = os.environ.get("TEST_POSTGRES_USER", os.environ.get("POSTGRES_USER", "postgres"))
PG_PASSWORD = os.environ.get("TEST_POSTGRES_PASSWORD", os.environ.get("POSTGRES_PASSWORD", "password"))
PROD_DB_NAME = os.environ.get("POSTGRES_DB", "veronica")
TEST_DB_NAME = os.environ.get("TEST_POSTGRES_DB", f"{PROD_DB_NAME}_test")

# Garde-fou : on ne veut JAMAIS que la suite de tests tourne sur la base de prod.
if TEST_DB_NAME == PROD_DB_NAME or "test" not in TEST_DB_NAME.lower():
    raise RuntimeError(
        "Le nom de la base de test doit être différent de la base de prod et "
        f"contenir 'test' (valeur actuelle : {TEST_DB_NAME!r}). Vérifiez vos "
        "variables d'environnement avant de lancer les tests !"
    )


async def _connect_maintenance() -> asyncpg.Connection:
    """Connexion à la base 'postgres', utilisée uniquement pour créer/supprimer
    la base de données de test (on ne peut pas DROP/CREATE la base sur laquelle
    on est actuellement connecté)."""
    return await asyncpg.connect(
        user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT, database="postgres"
    )


async def _drop_test_database(sys_conn: asyncpg.Connection) -> None:
    # On coupe d'abord les connexions actives à la base de test, sinon le DROP échoue.
    await sys_conn.execute(
        """
        SELECT pg_terminate_backend(pid)
        FROM pg_stat_activity
        WHERE datname = $1 AND pid <> pg_backend_pid()
        """,
        TEST_DB_NAME,
    )
    await sys_conn.execute(f'DROP DATABASE IF EXISTS "{TEST_DB_NAME}"')


@pytest_asyncio.fixture(scope="session")
async def test_database():
    """Crée une base de données PostgreSQL dédiée aux tests (isolée de la prod),
    et la supprime à la fin de la session de tests."""
    sys_conn = await _connect_maintenance()
    try:
        await _drop_test_database(sys_conn)  # au cas où un run précédent aurait planté
        await sys_conn.execute(f'CREATE DATABASE "{TEST_DB_NAME}"')
    finally:
        await sys_conn.close()

    yield TEST_DB_NAME

    if not os.environ.get("KEEP_TEST_DB"):
        sys_conn = await _connect_maintenance()
        try:
            await _drop_test_database(sys_conn)
        finally:
            await sys_conn.close()


@pytest_asyncio.fixture(scope="session")
async def db_pool(test_database):
    """Pool asyncpg pointant vers la base de test, avec le schéma déjà initialisé
    (tables créées + ligne de config de l'admin shop insérée), via le vrai code
    d'init de production `database_init.init_db`."""
    pool = await asyncpg.create_pool(
        user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT, database=test_database
    )
    await database_init.init_db(pool)
    yield pool
    await pool.close()


@pytest_asyncio.fixture
async def pool(db_pool):
    """A utiliser par les tests qui touchent la BD : fournit le pool de test après
    avoir vidé les tables métier, pour garantir l'isolation entre chaque test."""
    async with db_pool.acquire() as conn:
        await conn.execute("TRUNCATE TABLE tamagotchis, users RESTART IDENTITY CASCADE")
    # La ligne de pricing de l'admin shop (id=1) n'est pas vidée : c'est une
    # donnée de configuration partagée, pas une donnée créée par les tests.
    yield db_pool