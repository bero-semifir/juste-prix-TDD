from src.JustePrix import comparer, peut_jouer

def test_comparer_juste():
    assert comparer(500, 500)   == "C'est gagné"
    assert comparer(50, 50)     == "C'est gagné"
    assert comparer(1200, 1200) == "C'est gagné"

def test_comparer_inferieur():
    assert comparer(100, 500) == "C'est plus"
    assert comparer(10, 500)  == "C'est plus"
    assert comparer(499, 500) == "C'est plus"

def test_comparer_superieur():
    assert comparer(501, 500)  == "C'est moins"
    assert comparer(700, 500)  == "C'est moins"
    assert comparer(1200, 500) == "C'est moins"

def test_comparer_avec_nombre_joueur_string():
    assert comparer('500', 500)  == "C'est gagné"
    assert comparer('100', 500)  == "C'est plus"
    assert comparer('1000', 500) == "C'est moins"

def test_peut_jouer_true():
    assert peut_jouer(0, 10) == True
    assert peut_jouer(9, 10) == True
    assert peut_jouer(5, 10) == True

def test_peut_jouer_false():
    assert peut_jouer(11, 10) == False
    assert peut_jouer(1000, 10) == False
