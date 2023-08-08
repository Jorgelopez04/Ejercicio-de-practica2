import math

from modelo.mover import mover
from modelo.distancia import distancia
class punto:

   def __init__(self,x,y):
    self.x = x
    self.y = y

    #def mostrar(self,x,y):
        #print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self,n_x:mover,n_y:mover):
        self.n_x = n_x
        self.n_y = n_y



    def distancia(self, otro_punto):
        distancia_x = self.x - otro_punto.x
        distancia_y = self.y - otro_punto.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return distancia


       
         
 
    

  

  

    