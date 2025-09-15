from random import randint

shifumi = ["pierre", "feuille", "ciseaux"]

user= input("Veuillez entrer pierre, feuille ou ciseaux ").lower

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

if (user == "feuille" and bot == "pierre") or (user == "pierre" and bot == "ciseaux"):
    print("Vous avez gagné")