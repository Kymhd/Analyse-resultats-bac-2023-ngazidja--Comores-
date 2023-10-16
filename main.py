import csv
from tabulate import tabulate
from pyfiglet import Figlet
import datetime
import time
import statistics
import matplotlib.pyplot as plt

def tri_etudiant():

    """
    Trie les étudiants selon leur série et renvoie une liste filtrée.

    Demande à l'utilisateur d'entrer le nom d'une série parmi les critères possibles (A1, A4, A2, C, D, G).
    Renvoie une liste d'étudiants dont la série correspond à la série entrée par l'utilisateur.
    Si la série entrée n'est pas valide, redemande à l'utilisateur jusqu'à ce qu'il entre une série valide.
    """

    criter = [
        "A1", "A4", "A2", "C", "D", "G"
    ]

    while True:
        tri = input(
            f"Entrez le TRI {('; ').join(criter)}: ").upper().strip()
        if tri not in criter:
            print(f"Le criter '{tri}' ne fait pas parti")
            continue
        etudiants_tries = [ e for e in afficher_csv() if e["Serie"] == tri]
        return etudiants_tries


def recherche_etudiant(numero_rechercher):

    """Recherche un étudiant par son numéro et renvoie une liste contenant l'étudiant trouvé.

    Demande à l'utilisateur d'entrer le numéro d'un étudiant à rechercher.
    Renvoie une liste contenant l'étudiant dont le numéro correspond au numéro entré par l'utilisateur.
    Si le numéro entré n'est pas valide ou ne correspond à aucun étudiant,
    redemande à l'utilisateur jusqu'à ce qu'il entre un numéro valide.
    """
    try:
        numero_rechercher = str(numero_rechercher)
        etudiant_trouve = list(filter(lambda e: e["Numéro"] == numero_rechercher, afficher_csv()))
        return etudiant_trouve
    except ValueError:
        raise ValueError("Numero Invalide")


def afficher_csv():

    """
    Affiche le contenu du fichier resultat.csv sous forme de liste de dictionnaires.

    Ouvre le fichier resultat.csv en mode lecture avec l'encodage utf-8.
    Utilise le module csv pour lire le fichier avec le délimiteur ';'.
    Renvoie une liste de dictionnaires représentant les étudiants.
    """

    with open("resultat.csv", 'r', encoding='utf-8') as resultat:
        reader = csv.DictReader(resultat, delimiter=';')
        return list(reader)


def creer_graphique_serie():
    
    """
    Crée un graphique en barres qui montre la répartition des étudiants par série.

    Lit les données depuis le fichier resultat.csv et compte le nombre d'étudiants par série.
    Crée un graphique en barres avec les séries en abscisse et le nombre d'étudiants en ordonnée.
    Affiche le graphique à l'écran.
    """

    series = {}
    for ligne in afficher_csv():
        serie = ligne["Serie"]
        if serie in series:
            series[serie] += 1
        else:
            series[serie] = 1

    # Extraction des séries et de leurs fréquences
    series_labels = list(series.keys())
    series_counts = [series[serie] for serie in series_labels]

    # Création du graphique en barres
    plt.bar(series_labels, series_counts)
    plt.title('Répartition des élèves par série')
    plt.xlabel('Série')
    plt.ylabel('Nombre d\'étudiants')

    # Affichage du graphique
    plt.show()


def creer_graphique_langue():
    """
    Crée un graphique en camembert qui montre la répartition des étudiants par langue préférée.

    Lit les données depuis le fichier resultat.csv et compte le nombre d'étudiants par langue préférée.
    Crée un graphique en camembert avec les langues en légende et le pourcentage d'étudiants en secteurs.
    Affiche le graphique à l'écran.
    """
    langues = {}

    for ligne in afficher_csv():
        langue = ligne["Lvi"]
        if langue in langues:
            langues[langue] += 1
        else:
            langues[langue] = 1

    # Extraction des langues et de leurs fréquences
    langues_labels = list(langues.keys())
    langues_counts = [langues[langue] for langue in langues_labels]

    # Création du graphique en secteurs (camembert)
    plt.pie(langues_counts, labels=langues_labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Assure un cercle parfait

    plt.title('Répartition des étudiants par langue préférée')

    # Affichage du graphique
    plt.show()



def calcule_moyenne():

    """
    Calcule la moyenne d'âge des étudiants et renvoie une chaîne de caractères formatée.

    Parcourt la liste des étudiants renvoyée par la fonction afficher_csv.
    Extrait la date de naissance de chaque étudiant et la convertit en objet datetime.
    Calcule l'âge de chaque étudiant en soustrayant l'année de naissance à l'année actuelle.
    Ajoute l'âge de chaque étudiant à une liste.
    Utilise la fonction mean du module statistics pour calculer la moyenne des âges.
    Renvoie une chaîne de caractères formatée avec la moyenne arrondie à deux décimales.
    """

    liste = []

    for line in afficher_csv():
        date, lieu = line["Date et Lieu de Naissance"].split(' ', 1)
        date_ = datetime.datetime.strptime(date, "%d/%m/%Y")
        age = datetime.datetime.now().year - date_.year
        liste.append(age)

    return f"Moyenne d'age d'etudiants est {statistics.mean(liste):.2f}"


def print_welcome_message():
    print("Dans le programme de résultats des BACHELIERS 2023")
    print("Vous pouvez effectuer les actions suivantes :" )


def main():
    
    """
    Lance le programme principal et propose des options à l'utilisateur.

    Affiche une liste d'options possibles pour l'utilisateur :
    - Chercher un élève avec son numéro
    - Trier les élèves selon leur série
    - Afficher tous les élèves
    - Afficher la moyenne d'âge des élèves cette année
    - Répartition des éleves par Langue
    - Afficher les stats sous forme d'un graphe
    - Quitter le programme
    Demande à l'utilisateur de choisir une option en entrant le numéro correspondant.
    Exécute la fonction correspondant à l'option choisie par l'utilisateur.
    Si l'option entrée n'est pas valide, redemande à l'utilisateur jusqu'à ce qu'il entre une option valide.
    """

    figlet = Figlet()
    figlet = figlet.getFonts()
    figlet = Figlet(font='slant')
    print(figlet.renderText("BIENVENUE"))

    print_welcome_message()

    palette = [
        "Chercher éleve avec son Numéro",
        "Triez les les éléves selon leur série",
        "Afficher tous les éleves",
        "Afficher la moyenne d'âge des éléves cette année",
        "Répartition des éleves par Langue",
        "Afficher les stats sous forme d'un graphe",
        "quitter le programme"
    ]

    CONTROLE_PROGRAMME = True

    while CONTROLE_PROGRAMME: 
        time.sleep(2.4)
        print()
        choix_numer = 0
        for compter, i in enumerate(palette):
            print(f"{compter +1}.|| {i.upper()}: ")
 
        while True:
            try:
                choix = int(input("Choisissez une option (entrez le numéro) : "))
                if 1 <= choix <= len(palette):
                    choix_numer = choix
                    break
                else:
                    print("Option invalide. Veuillez choisir un numéro parmi les options disponibles.")
            except ValueError:
                print("Option invalide. Veuillez choisir un numéro parmi les options disponibles.")

        if choix_numer == 1:
            numero_rechercher = int(input("Entrez le numéro à rechercher : "))
            etudiant_trouve = recherche_etudiant(numero_rechercher)

            if len(etudiant_trouve):
                for l in etudiant_trouve:
                    date, lieu = l["Date et Lieu de Naissance"].split(' ', 1)
                    print("Felicitations !")
                    time.sleep(1.4)
                    info = [
                        ["Noms et Prénom:", l["Noms et Prenom"]],
                        ["Série:", l["Serie"]],
                        ["Numéro:", l["Numéro"]],
                        ["Date Naissance:", date],
                        ["lieu de Naissance:", lieu],
                        ["Nin:", l["Nin"]],
                    ]
                    print(tabulate(info))
            else:
                time.sleep(0.5)
                print(f"Désolé le numéro, ne figure pas !")

        elif choix_numer == 2:
            trie = tri_etudiant()
            print(f"Il y a {len(trie)} eléves triés selon ce critère")
            time.sleep(1.5)
            print(tabulate(trie, headers='keys', tablefmt="grid"))

        elif choix_numer == 3:
            tous = afficher_csv()
            print(tabulate(tous, headers='keys', tablefmt="grid"))
            print("---" * 12)
            print(f"Il y a {len(tous)} bachéliers cette année")
            print("---" * 12)

        elif choix_numer == 4:
            age = calcule_moyenne()
            print(tabulate([age]))

        elif choix_numer == 5:
            creer_graphique_langue()

        elif choix_numer == 6:
            creer_graphique_serie()
        else:
            CONTROLE_PROGRAMME = False

if __name__ == "__main__":
    main()
