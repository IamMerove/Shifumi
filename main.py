from random import randint

shifumi = ["pierre", "feuille", "ciseaux"]
score_bot = 0
score_user= 0
nbe_manche = 0

while nbe_manche < 3:
    user= input("Veuillez entrer pierre, feuille ou ciseaux ").lower()
    print(user)

    if user not in shifumi:
        print("Veuillez rentrer pierre, feuille ou ciseaux")
        exit()

    nbe_aleatoire = randint(0,2) 

    bot = shifumi[nbe_aleatoire]
    print(f"L'adversaire a joué {bot}")
    print(f"Vous avez joué {user}")

    if user == bot:
        print("Egalité")

    if (user == "pierre" and bot == "feuille") or ( user == "ciseaux" and bot == "pierre"):
        print("Vous avez perdu")
        score_bot += 1

    if (user == "feuille" and bot == "pierre") or (user == "pierre" and bot == "ciseaux"):
        print("Vous avez gagné")
        score_user += 1

    nbe_manche +=1
    print(f"Score: user {score_user} - {score_bot} bot")