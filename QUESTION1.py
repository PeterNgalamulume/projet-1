import abc
from math import pi, sqrt
from abc import ABCMeta, abstractmethod

class geometric_shapes (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calcul_du_perimetre(self):
        return

    @abc.abstractmethod
    def calcul_de_surface(self):
        return
