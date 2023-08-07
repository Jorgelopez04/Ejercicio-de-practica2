import math
from math import sqrt

class punto:

   def __init__(self):
    self.x = 5
    self.y = 2


    def mostrar(self,x,y):
         print(f"Coordenadas del punto: ({self.x}, {self.y})")
       
         

    def mover(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y

  

    def distancia(self, otro_punto):
        distancia_x = self.x - otro_punto.x
        distancia_y = self.y - otro_punto.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return distancia
    

    mover.nuevax=input("ingrese un valor")
    mover.nuevay=input("ingrese un valor")
  
    print(f"las nuevas coordenadas son ({mover.nueva_x},{mover.nueva_y})")