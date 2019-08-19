# -*-coding:Utf-8 -*
import fonctions

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = []
        self.grille.append(obstacles)
