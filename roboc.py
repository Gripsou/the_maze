# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu. Exécutez-le avec Python pour lancer le jeu. """

import os
import pickle
from fonctions import *
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
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))

#Si il y a une partie sauvegardée on l'affiche

for file in os.listdir():
        if file == "partie_save":
                nb_saves += 1
                continuer_partie = input("Il y a une partie sauvegardée souhaitez vous la continuer ? (Y / N) : ")
                continuer_partie.upper()
                if(continuer_partie == "Y"):    
                        with open(file, 'rb') as partie_en_cours:
                                mon_depickler = pickle.Unpickler(partie_en_cours)
                                partie = mon_depickler.load()
                                print("On ouvre la partie saved")
                else: 
                        nb_saves = 0

if nb_saves == 0 :
        the_game = init_game(cartes)
        print(the_game.grille)
        listed_game = list(the_game.grille)
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

user_input = input("Entrez une direction : \n > ")
user_input = user_input.upper()

while (user_input != 'Q') :
        current_game = move(user_input, listed_game)

        with open('partie_save', 'wb') as saved:
                mon_pickler = pickle.Pickler(saved)
                mon_pickler.dump(current_game)
                print("Debug : Partie saved !")
        print(''.join(current_game))
        while(listed_game[robot_position] != 'X'):
                robot_position += 1
        if(robot_position != position_sortie):
                user_input = input("Entrez une direction : \n > ")
                user_input = user_input.upper()
        else:
                print("Vous avez gagné félicitation")
                exit(0)

