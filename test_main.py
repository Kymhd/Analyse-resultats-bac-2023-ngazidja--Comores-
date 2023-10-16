from main import recherche_etudiant

def test_recherche_etudiant():
    # Cas où le numéro est valide et correspond à un étudiant
    assert recherche_etudiant(1) == [
    {'N': '1', 'Serie': 'A1', 'Numéro': '1', 'Noms et Prenom': 'AHMED ELYACHOURTU ZAID IBTISSAM ', 'Date et Lieu de Naissance': '30/08/2004 MATERNITE DE MORONI', 'Nin': 'UC1088607', 'Lvi': 'An'}
    ]


    # Cas où le numéro est valide mais ne correspond à aucun étudiant
    assert recherche_etudiant(3456) == []

    # Cas où le numéro est invalide
    try:
        recherche_etudiant("abc")
    except ValueError as e:
        assert str(e) == "Numero Invalide"
