# -*-coding:Utf-8 -*
from labyrinthe import Labyrinthe

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.chaine = chaine

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
