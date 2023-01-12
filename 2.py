import abc
from math import pi, sqrt
from abc import ABCMeta, abstractmethod

class geometric_shapes (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calcul_perimetre(self):
        return

    @abc.abstractmethod
    def calcul_surface(self):
        return

"""trois classes heritant de la classe de base definie ci-haut"""
#1°
class Rectangle (geometric_shapes):
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def calcul_perimetre(self):
        return 2*(self.longueur+self.largeur)
    
    def calcul_surface(self):
        return self.longueur * self.largeur


#2°
class cercle(geometric_shapes):
    def __init__(self,rayon):
        self.rayon = rayon

    def calcul_perimetre(self):
        return 2*pi*self.rayon
    
    def calcul_surface(self):
        return pi*self.rayon*self.rayon


#3°
class Triangle(geometric_shapes):
    def __init__(self, hauteur, cotéa, cotéb, cotéc):
        self.hauteur = hauteur
        self.cotéa= cotéa
        self.cotéb= cotéb
        self.cotéc= cotéc

    def calcul_perimetre(self):
        return self.cotéa+self.cotéb+self.base
    
    def calcul_surface(self):
        return self.hauteur * self.base / 2


