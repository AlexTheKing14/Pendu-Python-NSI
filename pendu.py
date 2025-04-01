import random

listemotpossibles = ["chat", "chien", "oiseau", "poisson", "lapin", "souris", "poule", "cochon", "vache", "cheval", "mouton", "canard", "pigeon", "poule", "renard", "loup", "ours", "tigre", "lion", "girafe", "elephant", "singe", "gorille", "kangourou", "koala", "panda", "souris", "chameau", "dromadaire", "baleine", "dauphin", "requin", "meduse"]

def choix_nom():
    return random.choice(listemotpossibles) # Fonction permettant de choisir un mot aléatoire dans la liste listemotpossibles

mot_a_trouver = choix_nom()
mot_courant = "-" * len(mot_a_trouver)
lettre_trouve = []
tentative_restante = 7
gagne = False 
lettre_erreur = []
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def demande_lettre(): # Fonction permettant de demander une lettre à l'utilisateur
    global mot_a_trouver
    global lettre_trouve
    global tentative_restante
    global mot_courant
    global gagne
    if gagne == True:
        return  
    global tentative_restante
    lettre = input("Entrez une lettre : ").lower() # On demande à l'utilisateur de rentrer une lettre, qui sera mise en minuscule
    if lettre == "ABANDON" or lettre == "abandon":
        print("Vous avez abandonné")
        return False
    while len(lettre) != 1 or lettre not in alphabet or lettre in lettre_trouve:
        lettre = input("Entrez une lettre valide : ").lower()
    affichageErreur(lettre)

def affichageErreur(lettre): # Fonction permettant d'afficher les erreurs
    global mot_a_trouver
    global lettre_trouve
    global tentative_restante
    global mot_courant
    global gagne
    if gagne == True:
        return
    if lettre not in mot_a_trouver: # Si la lettre n'est pas dans le mot à trouver
        print("La lettre", lettre, "n'est pas dans le mot")
        lettre_erreur.append(lettre) 
        print("Les lettres déjà essayées sont :", lettre_erreur)
        print("Si vous souhaitez abandonner, tapez ABANDON")
        global tentative_restante
        tentative_restante -= 1
        if tentative_restante == 6: # Si il reste 6 tentatives
            print("==============")
            print("Il te reste 6 tentatives")
            demande_lettre()
        elif tentative_restante == 5: # Si il reste 5 tentatives
            print(" /| | ")
            print("==============")
            print("Il te reste 5 tentatives")
            demande_lettre()
        elif tentative_restante == 4: # Si il reste 4 tentatives
            print(" | |      /  \\ ")
            print("/| | ")
            print("==============")
            print("Il te reste 4 tentatives")
            demande_lettre()
        elif tentative_restante == 3: # Si il reste 3 tentatives
            print(" | |      /|\\ ")
            print(" | |      / \\ ")
            print("/| | ")
            print("==============")
            print("Il te reste 3 tentatives")
            demande_lettre()
        elif tentative_restante == 2: # Si il reste 2 tentatives
            print(" | |       0  ")
            print(" | |      /|\\ ")
            print(" | |      / \\ ")
            print("/| | ")
            print("==============")
            print("Il te reste 2 tentatives")
            demande_lettre()
        elif tentative_restante == 1: # Si il reste 1 tentative
            print(" | |/      |  ")
            print(" | |       0  ")
            print(" | |      /|\\ ")
            print(" | |      / \\ ")
            print("/| | ")
            print("==============")
            print("Il te reste 1 tentative")
            demande_lettre()
        elif tentative_restante == 0: # Si il ne reste plus de tentatives
            print("===========Y==")
            print(" | |/      |  ")
            print(" | |       0  ")
            print(" | |      /|\\ ")
            print(" | |      / \\ ")
            print("/| | ")
            print("==============")
            print("Vous avez perdu !")
            print("Le mot était", mot_a_trouver)
            if tentative_restante == 0:
                print("===============")
                print("Voulez vous rejouer ? (O/N)")
                print("===============")
                reponse2 = input("Entrez votre choix : ").lower() # On demande à l'utilisateur s'il veut rejouer
                if reponse2 == "o": # Va initialiser les variables pour une nouvelle partie
                    gagne = False 
                    lettre_trouve = []
                    mot_a_trouver = choix_nom()
                    mot_courant = "-" * len(mot_a_trouver)
                    tentative_restante = 7
                    lancementpendu()
                elif reponse2 == "n":
                    print("Merci d'avoir joué !")
                else: # Si le choix est invalide ou alors N est répondu, alors la partie est terminée 
                    print("Choix invalide. La partie est terminé.")
                    print("===============")
                return False
            return False
    else: # Si la lettre est dans le mot à trouver
        print("La lettre", lettre, "est dans le mot")
        lettre_trouve.append(lettre) # On rajoute dans la liste lettre_trouve la lettre trouvée
        nouveauMotCourant(lettre)
        demande_lettre()
        if mot_courant == mot_a_trouver: # On vérifie si le mot courant est égal au mot à trouver
            #print("Vous avez gagné !")
            gagne = True
            

def nouveauMotCourant(char):
    global mot_a_trouver
    global lettre_trouve
    global tentative_restante
    global mot_courant
    for i in range(len(mot_a_trouver)): # On parcourt le mot à trouver
        if mot_a_trouver[i] == char:
            mot_courant = mot_courant[:i] + char + mot_courant[i+1:]
    print(mot_courant)
    if "-" not in mot_courant: # Si le mot courant ne contient plus de tirets, cela signifie que le joueur a trouvé le mot
        global gagne
        gagne = True
        print("Vous avez gagné ! Le mot était :", mot_a_trouver)
        print("===============")
        print("Voulez vous rejouer ? (O/N)")
        print("===============")
        reponse = input("Entrez votre choix : ").lower() # On demande à l'utilisateur s'il veut rejouer
        if reponse == "o": # initialise les variables pour une nouvelle partie
            gagne = False 
            lettre_trouve = []
            mot_a_trouver = choix_nom()
            mot_courant = "-" * len(mot_a_trouver)
            tentative_restante = 7
            lancementpendu()
        elif reponse == "n":
            print("Merci d'avoir joué !")
        else:
            print("Choix invalide. La partie est terminé.")
            print("===============")
        return 

def lancementpendu(): # Fonction permettant le lancement du jeu
    global mot_a_trouver
    global mot_courant
    print("Bienvenue dans le jeu du pendu !")
    print("/!\\ Si vous souhaitez choisir le mot à trouver tapez 1 si vous préférez qu'il soit choisi aléatoirement tapez 2 !")
    print("===============")
    choix = input("Votre choix : ") # Demander à l'utilisateur de choisir entre 1 ou 2 qui va modifier le mot à trouver
    if choix == "1":
        print("Entrez le mot à trouver : ")
        mot_a_trouver = input().lower() # Le mot sera choisi par l'utilisateur
        global mot_courant
        mot_courant = "-" * len(mot_a_trouver)
        print("===============")
    elif choix == "2": # Le mot sera choisi aléatoirement
        print("Le mot à trouver est choisi aléatoirement.")
        print("===============")
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        print("===============")
        lancementpendu()
        return
    #print(mot_a_trouver) Print a réactiver pour voir le mot à trouver pour faire différents tests
    print("Le mot à trouver contient", len(mot_a_trouver), "lettres")
    print("Le mot :", mot_courant)
    demande_lettre()

lancementpendu() # Lancement du jeu
