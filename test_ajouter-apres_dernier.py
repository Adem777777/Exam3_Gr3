import pytest
from debogue_moi import *

def test_ajouter_apres_dernier():
    # Arrange
    calendrier = {
        "Amélie": ("08:15", 60),
        "Hakim": ("09:30", 90),
        "Bouchra": ("11:15", 60),
        "Jacob": ("13:45", 30)
    }
    nom = "Adem"
    duree = "60"
    resultat_attendu = "Rendez-vous confirmé à 14:30."
    # Act
    resultat_fonc = ajouter_apres_dernier(calendrier, nom, duree)

    # Assert
    assert resultat_attendu == resultat_fonc