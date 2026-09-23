"""
Tests pour `database_init.py` : création du schéma et seed de l'admin shop.

Ces tests utilisent la fixture `pool` (voir conftest.py), qui pointe vers une
base de données PostgreSQL de test créée pour l'occasion — jamais la prod.
"""
import database_init
from cogs.tamagotchi import db_tamagotchi


async def test_init_db_cree_les_trois_tables(pool):
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'
            """
        )
    table_names = {r["table_name"] for r in rows}
    assert {"users", "tamagotchis", "admin_shop_pricings"} <= table_names


async def test_init_db_est_idempotent(pool):
    # Ré-exécuter init_db ne doit ni planter, ni dupliquer la ligne d'admin shop
    # (les CREATE TABLE utilisent IF NOT EXISTS, et create_admin_shop vérifie
    # l'existence avant d'insérer).
    await database_init.init_db(pool)
    await database_init.init_db(pool)

    async with pool.acquire() as conn:
        count = await conn.fetchval("SELECT COUNT(*) FROM admin_shop_pricings")
    assert count == 1


async def test_init_db_seed_les_prix_par_defaut_de_ladmin_shop(pool):
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT * FROM admin_shop_pricings WHERE id = 1")
    assert row is not None
    assert row["tamagotchi_base_price"] == 500.0
    assert row["tamagotchi_skin_base_price"] == 100.0


async def test_create_admin_shop_nadd_pas_de_doublon_si_deja_present(pool):
    await db_tamagotchi.create_admin_shop(pool)
    await db_tamagotchi.create_admin_shop(pool)

    async with pool.acquire() as conn:
        count = await conn.fetchval("SELECT COUNT(*) FROM admin_shop_pricings")
    assert count == 1