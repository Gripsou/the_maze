# -*-coding:Utf-8 -*

"""This files contains the main code of the game, run it to begin the game """

import os
import pickle
from fonctions import affichage, init_game, move
from carte import Carte
from labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []
nb_cartes = 0
nb_saves = 0
for nom_fichier in os.listdir("cartes"):
        nb_cartes += 1
        if nom_fichier.endswith(".txt"):
                chemin = os.path.join("cartes", nom_fichier)
                nom_carte = nom_fichier[:-3].lower()
                with open(chemin, "r") as fichier:
                        contenu = fichier.read()
                        # Création d'une carte, à compléter
                        map_jeu = Carte(nom_carte, contenu)
                        cartes.append(map_jeu)

# On affiche les cartes existantes
affichage()

for file in os.listdir():
        if file == "partie_save":
                nb_saves += 1
                continuer_partie = input(
                    "There's a saved game, do you wan't to continue it ? (Y / N) : ")
                continuer_partie = continuer_partie.upper()
                while (continuer_partie != 'Y' and continuer_partie != 'N'):
                        continuer_partie = input("Please answer (Y) or (N)")
                        continuer_partie = continuer_partie.upper()
                if(continuer_partie == "Y"):
                        with open(file, 'rb') as partie_en_cours:
                                mon_depickler = pickle.Unpickler(
                                    partie_en_cours)
                                partie = mon_depickler.load()
                                print("We open the saved game")
                else:
                        nb_saves = 0


print("Available mazes : ")
for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))

#Si il y a une partie sauvegardée on l'affiche

if nb_saves == 0 :
        i = 0
        largeur = 1
        the_game = init_game(cartes)
        print(the_game.grille)
        listed_game = list(the_game.grille)
        while listed_game[i] != '\n':
                i += 1
                largeur += 1
else : 
        the_game = partie
        listed_game = the_game
        print(''.join(the_game))
        

position_sortie = 0
robot_position = 0

while(listed_game[position_sortie] != 'U'):
        position_sortie += 1
while(listed_game[robot_position] != 'X'):
        robot_position += 1

user_input = input("Enter a direction \n > ")
user_input = user_input.upper()

while (user_input != 'Q') :
        current_game = move(user_input, listed_game, largeur)

        with open('partie_save', 'wb') as saved:
                mon_pickler = pickle.Pickler(saved)
                mon_pickler.dump(current_game)
        print(''.join(current_game))
        robot_position = 0
        while(listed_game[robot_position] != 'X'):
                robot_position += 1
        if(robot_position != position_sortie):
                user_input = input("Enter a direction \n > ")
                user_input = user_input.upper()
        else:
                print("You won the game ! Congratulation")
                exit(0)

