## Shifumi 
Version "finale"" avec plusieurs manches

🎮 Shifumi - Jeu Pierre Feuille Ciseaux

Ce projet est une implémentation simple du jeu Pierre-Feuille-Ciseaux en Python, où un utilisateur affronte un bot pendant 3 manches.

📝 Description

L'utilisateur joue contre l'ordinateur (bot) en choisissant entre :

pierre

feuille

ciseaux

Le bot choisit aléatoirement une des trois options. Le gagnant de chaque manche est déterminé selon les règles classiques :

Pierre bat Ciseaux

Ciseaux bat Feuille

Feuille bat Pierre

À la fin des 3 manches, le score est comparé pour déclarer un gagnant. Il est ensuite proposé à l'utilisateur de rejouer ou quitter.

🚀 Fonctionnalités

Entrée utilisateur avec validation

Choix aléatoire du bot

Calcul des scores

Annonce du gagnant

Option pour recommencer une partie

💻 Utilisation
Prérequis

Python 3.x installé

Exécution

Lancer le script avec :

python shifumi.py

Exemple de partie
Veuillez entrer pierre, feuille ou ciseaux:
> pierre
L'adversaire a joué ciseaux
Vous avez joué pierre
Vous avez gagné
Score: user 1 - 0 bot


Après 3 manches :

Vous avez gagné
Recommencer la partie ? oui/non

🧠 Structure du code

initialisation_variable() : Initialise les scores et le nombre de manches

check_winner(user, bot, score_user, score_bot) : Compare les choix pour déterminer le gagnant d'une manche

Boucle principale : Gère le déroulement du jeu, les entrées et les résultats

📦 À améliorer

Interface graphique (Tkinter / PyQt)

Mode multijoueur

Score cumulé sur plusieurs parties

Gestion des erreurs plus poussée

📄 Licence

Projet libre d'utilisation à des fins pédagogiques ou personnelles.