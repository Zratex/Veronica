"""
Tests unitaires "purs" (aucune BD requise) pour `type_classes.Tamagotchi.Tamagotchi`.

Ces tests couvrent la logique de jeu : besoins exprimés par `parle()`,
actions `mange()` / `joue()`, et les 3 conditions de mort.
"""
from type_classes.Tamagotchi import Tamagotchi


def make_tama(**overrides) -> Tamagotchi:
    """Fabrique un Tamagotchi de test avec des valeurs explicites (jamais les
    valeurs par défaut de la classe, qui reposent sur `randint` et sont donc
    non déterministes / fixées au chargement du module)."""
    defaults = dict(
        id=1, user_id=42, name="Pouic", age=0,
        max_energy=10, current_energy=10, max_fun=10, current_fun=10,
    )
    defaults.update(overrides)
    return Tamagotchi(**defaults)


# --- parle() -------------------------------------------------------------

def test_parle_est_chill_quand_energie_et_fun_ok():
    tama = make_tama(current_energy=5, current_fun=5)
    assert tama.parle() == 0


def test_parle_a_faim_quand_energie_basse():
    tama = make_tama(current_energy=4, current_fun=10)
    assert tama.parle() == 1


def test_parle_priorise_la_faim_si_energie_et_fun_bas():
    # Quand l'énergie ET le fun sont bas, le code priorise la faim (return 1)
    tama = make_tama(current_energy=1, current_fun=1)
    assert tama.parle() == 1


def test_parle_sennuie_quand_fun_bas_mais_energie_ok():
    tama = make_tama(current_energy=10, current_fun=4)
    assert tama.parle() == 2


# --- mange() ---------------------------------------------------------------

def test_mange_augmente_lenergie_si_pas_au_max(monkeypatch):
    monkeypatch.setattr("type_classes.Tamagotchi.randint", lambda a, b: 2)
    tama = make_tama(max_energy=10, current_energy=5)
    assert tama.mange() is True
    assert tama.current_energy == 7


def test_mange_ne_fait_rien_si_deja_au_max():
    tama = make_tama(max_energy=10, current_energy=10)
    assert tama.mange() is False
    assert tama.current_energy == 10


# --- joue() ------------------------------------------------------------

def test_joue_augmente_le_fun_si_pas_au_max(monkeypatch):
    monkeypatch.setattr("type_classes.Tamagotchi.randint", lambda a, b: 3)
    tama = make_tama(max_fun=10, current_fun=4)
    assert tama.joue() is True
    assert tama.currentFun == 7


def test_joue_ne_fait_rien_si_deja_au_max():
    tama = make_tama(max_fun=10, current_fun=10)
    assert tama.joue() is False
    assert tama.currentFun == 10


# --- conditions de mort ---------------------------------------------------

def test_est_mort_denergy_vrai_si_energie_nulle_ou_negative():
    assert make_tama(current_energy=0).estMortDenergy() is True
    assert make_tama(current_energy=-1).estMortDenergy() is True


def test_est_mort_denergy_faux_si_energie_positive():
    assert make_tama(current_energy=1).estMortDenergy() is False


def test_est_mort_de_marasme_vrai_si_fun_nul_ou_negatif():
    assert make_tama(current_fun=0).estMortDeMarasme() is True
    assert make_tama(current_fun=-1).estMortDeMarasme() is True


def test_est_mort_de_marasme_faux_si_fun_positif():
    assert make_tama(current_fun=1).estMortDeMarasme() is False


def test_est_mort_vieillesse_vrai_a_partir_de_lifetime():
    assert make_tama(age=Tamagotchi.lifeTime).estMortVieillesse() is True
    assert make_tama(age=Tamagotchi.lifeTime + 5).estMortVieillesse() is True


def test_est_mort_vieillesse_faux_avant_lifetime():
    assert make_tama(age=Tamagotchi.lifeTime - 1).estMortVieillesse() is False