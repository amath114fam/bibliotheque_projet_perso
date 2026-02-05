import json
def menu():
    print("-" * 30)
    print("1. Afficher la bibliothèque")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Rechercher un livre")
    print("5. Emprunter un livre")
    print("6. Retourner un livre")
    print("0. Quitter")
    return input("Choisis un numéro : ")
fichier = "bibbliotheque.json"
identifiant = 0
bibliotheque = []
#Les fichiers .json et leur création
def save():
    with open(fichier, "w", encoding="utf-8") as file:
        json.dump(bibliotheque, file, ensure_ascii=False, indent=4)
try:
    with open(fichier, "r") as file:
        bibliotheque = json.load(file)
except FileNotFoundError:
    save()
#********************************
def retour_au_menu():
    """Pour retourner au menu"""
    print("1. Ajouter un nouveau livre")
    print("2. Retour au menu")
    while True:
        choice = input("Choisis 1 ou 2 : ").replace(" ", "")
        if choice == "1":
            ajouter_livre()
            break
        elif choice == "2":
            break
        else:
            print("Choix invalide") 
#Fonction pour ajouter livre
def ajouter_livre():
    """Ajouter un livre"""
    global bibliotheque
    if bibliotheque:
        identifiant = bibliotheque[-1]["id"]
    while True: 
        if bibliotheque:
            identifiant += 1
        else:
            identifiant = 1
        print("Bienvenu dans la bibliothèque")
        print("-" * 30)
        titre = input("Entrer le titre du livre : ").strip()
        auteur = input("Entrer l'auteur du livre : ").strip()
        livre = {
            "id" : identifiant,
            "titre" : titre,
            "auteur" : auteur,
            "disponible" : "disponible"
        }
        bibliotheque.append(livre)
        save()
        print(f"Le livre {titre} de {auteur} a été bien ajouté dans le bibliothèque")
        print("-" * 10)
        print("1. Ajouter un nouveau livre")
        print("2. Retour au menu")
        choice = input("Choisis 1 ou 2 : ").replace(" ", "")
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("Choix invalide") 
# pour voir les livres et leurs auteurs
def biblios():
    print("Les livres et leur auteurs : ")
    for element in bibliotheque:
        print(f"N°{element["id"]} : {element["titre"]} de {element["auteur"]}")
#****************************************************************
# Pour rechercher un livre
trouver = False
def rechercher_livre():
    """Fonction pour rechercher un livre"""
    global trouver
    titre_du_livre = input("Entrer le titre du livre : ").strip()
    for element in bibliotheque:
        if titre_du_livre.lower() == element["titre"].lower():
            trouver = True
            auteur = element["auteur"]
    if trouver:
        print(f"{titre_du_livre} de {auteur}")
    else:
        print("Ce livre n'existe pas")

def supprimer_livre():
    """Fonction pour supprimmer un livre"""
    vue = False
    print("Vous voulez supprimer un livre.....")
    print("-" * 4)
    biblios()
    while True:
        numero= input("Chosissez le numéro du livre que vous voulez emprunter N° : ").strip()
        print("-" * 4)
        try:
            for element in bibliotheque:
                if int(numero) == element["id"]:
                    vue = True
                    a_supprimer = element
            if vue:
                print(f"le livre {a_supprimer["titre"]} de {a_supprimer["auteur"]} a été bien supprimer avec succès!!")
                bibliotheque.remove(a_supprimer)
                print("-" * 10)
                save()
            else:
                print("Le numéro de l'identifiant enregistré n'existe pas dans la bibliothèque")
            print("-" * 10)
            print("1. Supprimer un autre livre")
            print("2. Retour au menu")
            choice = input("Choisis 1 ou 2 : ").replace(" ", "")
            if choice == "1":
                continue
            elif choice == "2":
                break
            else:
                print("Choix invalide") 
        except ValueError:
            print("Veillez-choisir uniquement un chiffre ou un nombre")
            print("-" * 10)
            print("1. Supprimer un autre livre")
            print("2. Retour au menu")
            choice = input("Choisis 1 ou 2 : ").replace(" ", "")
            if choice == "1":
                continue
            elif choice == "2":
                break
            else:
                print("Choix invalide") 
def emprunter_livre():
    """Fonction pour emprunter un """
    print("Bienvenue dans la bibliothèque")
    print("-" * 4)
    biblios()
    while True:
        numero= input("Chosissez le numéro du livre que vous voulez emprunter N° : ").strip()
        print("-" * 4)
        try:
            for element in bibliotheque:
                if int(numero) == element["id"]:
                    if element["disponible"] == "disponible":
                        a_emprunter = element
                        bibliotheque[element["id"] - 1]["disponible"] = "indisponible"
                        save()
                        print(f"le livre {a_emprunter["titre"]} de {a_emprunter["auteur"]} est emprunté avec succès!!")
                        print("-" * 10)
                    else:
                        print("Le livre est indisponible")
                        break
                else:
                    print("Le numéro de l'identifiant enregistré n'existe pas dans la bibliothèque")
                    break
            #     print(f"le livre {a_emprunter["titre"]} de {a_emprunter["auteur"]} est emprunté avec succès!!")
            #     print("-" * 10)
            # else:
                
            print("-" * 10)
            print("1. emprunter un autre livre")
            print("2. Retour au menu")
            choice = input("Choisis 1 ou 2 : ").replace(" ", "")
            if choice == "1":
                continue
            elif choice == "2":
                break
            else:
                print("Choix invalide") 
        except ValueError:
            print("Veillez-choisir uniquement un chiffre ou un nombre")
            print("-" * 10)
            print("1. Supprimer un autre livre")
            print("2. Retour au menu")
            choice = input("Choisis 1 ou 2 : ").replace(" ", "")
            if choice == "1":
                continue
            elif choice == "2":
                break
            else:
                print("Choix invalide") 
while True:
    choix = menu()
    match choix:
        case "1":
            print("-" * 10)
            if bibliotheque:
                biblios()
            else:
                print("Le bibliothèque est vide")
            print("-" * 10)
        case "2":
            print("-" * 10)
            ajouter_livre()
            print("-" * 10)
        case "3":
            print("-" * 10)
            if bibliotheque:
                supprimer_livre()
            else:
                print("Le bibliothèque est vide")
            print("-" * 10)
        case "4":
            print("-" * 10)
            rechercher_livre()
            print("-" * 10)
        case "5":
            print("-" * 10)
            if bibliotheque:
                emprunter_livre()
            else:
                print("Le bibliothèque est vide")
            print("-" * 10)
        case "6":
            print("-" * 10)
            print("C'est pour retourner un livre")
            print("-" * 10)
        case _:
            exit()

