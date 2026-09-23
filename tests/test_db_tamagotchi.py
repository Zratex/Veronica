"""
Tests pour `cogs/tamagotchi/db_tamagotchi.py` : gestion des utilisateurs
(argent), et gestion des tamagotchis (achat, stats, cycle de vie).

Ces tests utilisent la fixture `pool` (voir conftest.py), qui pointe vers une
base de données PostgreSQL de test créée pour l'occasion — jamais la prod.
Les tables métier ("users", "tamagotchis") sont vidées avant chaque test.
"""
import pytest # type: ignore

from cogs.tamagotchi import db_tamagotchi
from type_classes.Tamagotchi import Tamagotchi

USER_ID = 111111111111111111
OTHER_USER_ID = 222222222222222222


# --- get_or_create_user -----------------------------------------------------

async def test_get_or_create_user_cree_un_nouvel_utilisateur_avec_500(pool):
    user = await db_tamagotchi.get_or_create_user(pool, USER_ID)
    assert user["id"] == USER_ID
    assert user["money"] == 500.0


async def test_get_or_create_user_ne_duplique_pas_un_utilisateur_existant(pool):
    first = await db_tamagotchi.get_or_create_user(pool, USER_ID)
    await db_tamagotchi.update_money(pool, USER_ID, 100)  # on modifie son solde
    second = await db_tamagotchi.get_or_create_user(pool, USER_ID)

    assert second["id"] == first["id"]
    assert second["money"] == 600.0  # la valeur modifiée est bien conservée

    async with pool.acquire() as conn:
        count = await conn.fetchval("SELECT COUNT(*) FROM users WHERE id = $1", USER_ID)
    assert count == 1


# --- update_money ------------------------------------------------------

async def test_update_money_credite_le_compte(pool):
    await db_tamagotchi.get_or_create_user(pool, USER_ID)
    await db_tamagotchi.update_money(pool, USER_ID, 250.0)
    assert await db_tamagotchi.get_user_money(pool, USER_ID) == 750.0


async def test_update_money_debite_le_compte(pool):
    await db_tamagotchi.get_or_create_user(pool, USER_ID)
    await db_tamagotchi.update_money(pool, USER_ID, -200.0)
    assert await db_tamagotchi.get_user_money(pool, USER_ID) == 300.0


async def test_update_money_cree_lutilisateur_sil_nexiste_pas_encore(pool):
    # Aucun get_or_create_user préalable : la fonction doit le faire elle-même.
    await db_tamagotchi.update_money(pool, USER_ID, -50.0)
    assert await db_tamagotchi.get_user_money(pool, USER_ID) == 450.0  # 500 - 50


# --- get_user_money ----------------------------------------------------

async def test_get_user_money_utilisateur_inexistant_retourne_zero(pool):
    assert await db_tamagotchi.get_user_money(pool, 999999) == 0


# --- create_tamagotchi / get_tamagotchi_from_id -----------------------------

async def test_create_tamagotchi_cree_un_tamagotchi_lie_a_lutilisateur(pool):
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Pouic")

    ids = await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID)
    assert len(ids) == 1

    tama = await db_tamagotchi.get_tamagotchi_from_id(pool, ids[0])
    assert tama["name"] == "Pouic"
    assert tama["user_id"] == USER_ID
    # Valeurs par défaut définies dans le schéma :
    assert tama["max_energy"] == 10
    assert tama["current_energy"] == 10
    assert tama["max_fun"] == 10
    assert tama["current_fun"] == 10


async def test_create_tamagotchi_cree_lutilisateur_sil_nexiste_pas_encore(pool):
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Pouic")
    async with pool.acquire() as conn:
        user_exists = await conn.fetchval("SELECT COUNT(*) FROM users WHERE id = $1", USER_ID)
    assert user_exists == 1


async def test_get_tamagotchi_from_id_inexistant_retourne_none(pool):
    assert await db_tamagotchi.get_tamagotchi_from_id(pool, 999999) is None


async def test_le_resultat_est_compatible_avec_la_classe_tamagotchi(pool):
    """Vérifie que le dict renvoyé par la BD peut bien être passé tel quel
    à `Tamagotchi(**resultQuery)`, comme le fait `tamagotchi_main.py`."""
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Pouic")
    ids = await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID)
    row = await db_tamagotchi.get_tamagotchi_from_id(pool, ids[0])

    tama = Tamagotchi(**row)
    assert tama.name == "Pouic"
    assert tama.id == ids[0]


# --- get_tamagotchis_ids_by_user ----------------------------------------

async def test_get_tamagotchis_ids_by_user_liste_vide_si_aucun(pool):
    assert await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID) == []


async def test_get_tamagotchis_ids_by_user_ne_retourne_que_les_siens(pool):
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Pouic")
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Riri")
    await db_tamagotchi.create_tamagotchi(pool, OTHER_USER_ID, "PasLeMien")

    ids = await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID)
    assert len(ids) == 2

    other_ids = await db_tamagotchi.get_tamagotchis_ids_by_user(pool, OTHER_USER_ID)
    assert len(other_ids) == 1


# --- update_tamagotchi_stats (avec clamp GREATEST/LEAST) --------------------

async def test_update_tamagotchi_stats_variation_normale(pool):
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Pouic")
    tama_id = (await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID))[0]

    await db_tamagotchi.update_tamagotchi_stats(pool, tama_id, energy_change=-3, fun_change=-2)

    tama = await db_tamagotchi.get_tamagotchi_from_id(pool, tama_id)
    assert tama["current_energy"] == 7  # 10 - 3
    assert tama["current_fun"] == 8     # 10 - 2


async def test_update_tamagotchi_stats_est_plafonne_au_max(pool):
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Pouic")
    tama_id = (await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID))[0]

    # +100 alors que max_energy/max_fun valent 10 par défaut : doit être plafonné.
    await db_tamagotchi.update_tamagotchi_stats(pool, tama_id, energy_change=100, fun_change=100)

    tama = await db_tamagotchi.get_tamagotchi_from_id(pool, tama_id)
    assert tama["current_energy"] == 10
    assert tama["current_fun"] == 10


async def test_update_tamagotchi_stats_est_plancher_a_zero(pool):
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "Pouic")
    tama_id = (await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID))[0]

    # -100 doit être plafonné à 0, jamais négatif.
    await db_tamagotchi.update_tamagotchi_stats(pool, tama_id, energy_change=-100, fun_change=-100)

    tama = await db_tamagotchi.get_tamagotchi_from_id(pool, tama_id)
    assert tama["current_energy"] == 0
    assert tama["current_fun"] == 0


# --- pricing de l'admin shop ---------------------------------------------

async def test_get_base_price_to_buy_tamagotchi_retourne_le_prix_par_defaut(pool):
    price = await db_tamagotchi.get_base_price_to_buy_tamagotchi(pool)
    assert price == 500.0


async def test_scenario_achat_dun_tamagotchi_debite_bien_le_prix(pool):
    """Scénario bout-en-bout reproduisant la logique de la commande
    `buy-tamagotchi` : vérifier le solde, débiter, créer le tamagotchi."""
    await db_tamagotchi.get_or_create_user(pool, USER_ID)
    price = await db_tamagotchi.get_base_price_to_buy_tamagotchi(pool)
    money_before = await db_tamagotchi.get_user_money(pool, USER_ID)

    assert money_before >= price  # l'utilisateur a de quoi acheter

    await db_tamagotchi.update_money(pool, USER_ID, -price)
    await db_tamagotchi.create_tamagotchi(pool, USER_ID, "NouveauTama")

    assert await db_tamagotchi.get_user_money(pool, USER_ID) == money_before - price
    assert len(await db_tamagotchi.get_tamagotchis_ids_by_user(pool, USER_ID)) == 1