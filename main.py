from random import randint



shifumi = ["pierre", "feuille", "ciseaux"]
def initialisation_variable():

    #initialisation des variables
    score_bot = 0
    score_user= 0
    nbe_manche = 0
    return score_bot,score_user,nbe_manche

#fonction pour vérifier qui a gagné
def check_winner(user,bot,score_user,score_bot):
    if user == bot:
        print("Egalité")

    # Cas bot winner
    if (user == "pierre" and bot == "feuille") or ( user == "ciseaux" and bot == "pierre") or (user =="feuille" and bot=="ciseaux"):
        print("Vous avez perdu")
        score_bot += 1

    # Cas user winner
    if (user == "feuille" and bot == "pierre") or (user == "pierre" and bot == "ciseaux") or (user =="ciseaux" and bot=="feuille"):
        print("Vous avez gagné")
        score_user += 1
    return score_bot,score_user


# début de la partie
score_bot,score_user,nbe_manche = initialisation_variable()
while nbe_manche < 3 :
    # entrée de l'utilisateur
    user= input("Veuillez entrer pierre, feuille ou ciseaux:\n ").lower()
    print(user)

    # si l'utilisateur entre autre chose que ce qui est demandé
    if user not in shifumi:
        continue
        
    # choix du bot
    nbe_aleatoire = randint(0,2) 

    bot = shifumi[nbe_aleatoire]
    print(f"L'adversaire a joué {bot}")
    print(f"Vous avez joué {user}")

    # on vérifie qui gagne et augmente le score du gagnant
    score_bot,score_user = check_winner(user,bot,score_user,score_bot)

    #incrémente le nombre de manche joué
    nbe_manche +=1
    print(f"Score: user {score_user} - {score_bot} bot")

    # Si la partie est terminé, on propose de recommencer
    if nbe_manche == 3:
        if score_user > score_bot:
            print("Vous avez gagné")
        elif score_user<score_bot:
            print("Vous avez perdu")
        else:
            print("Egalité !")
        repondu = False
        while not repondu:
            reponse = input("Recommencer la partie ? oui/non\n").lower()
            if reponse in ["oui","non"] and reponse == "oui":
                score_bot,score_user,nbe_manche = initialisation_variable()
                repondu = True
            elif reponse in ["oui","non"] and reponse == "non":
                repondu = True
                print("Partie terminé !")
            




