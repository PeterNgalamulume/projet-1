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

    

"""classes de carrees et triangles rectangles"""
#1°
class Carre(Rectangle):
    def __init__(self, coté):
        Rectangle.__init__(self,coté,coté)

#2°
class Triangle_rectangle(Triangle):
    def __init__(self, basis, height):
        Triangle.__init__(self,height,basis,height,cotéc=sqrt(basis**2+height**2))



class FormeGeometriqueExploite():#C'est la classe qui exploite

    def __init__(self, arg):
        pass
    
    def RectangleA(longueur,largeur): 
        self.Rectangle = Rectangle(longueur,largeur)
        print("Le périmètre du rectangle est ",self.Rectangle.perimetre(),"mètres")
        print("La surface du rectangle est ",self.Rectangle.surface(),"mètres carré")
        pass

    def CercleA(rayon):
        self.Circle = Cercle(rayon)
        print("Le périmètre du cercle est",self.Circle.perimetre(),"mètres")
        print("La surface du cercle",self.Circle.surface(),"mètres carré")
        pass

    def TriangleA(cotéa, cotéb, cotéc):
        self.myTriangle = Triangle(cotéa, cotéb, cotéc)
        print("Le périmètre du triangle est ",self.myTriangle.perimetre(),"mètres")
        print("La surface du triangle est ",self.myTriangle.surface(),"mètres carré")
        pass

    def CarreA(coté):
        self.mySquare = Carre(coté)
        print("Le périmètre du carré est ",self.mySquare.perimetre(),"mètres")
        print("La surface du carré est ",self.mySquare.surface(),"mètres carré")
        pass

    def RectangleTriangleA(basis,height):
        self.myRecTriangle = RecTriangle(3,4)
        print("Le périmètre du triangle rectangle est ",self.myRecTriangle.perimetre(),"mètres")
        print("La surface du triangle rectangle est ",self.myRecTriangle.surface(),"mètres carré")
        pass
