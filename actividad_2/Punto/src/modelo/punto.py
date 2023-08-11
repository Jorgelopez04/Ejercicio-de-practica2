import math


class punto:

      def __init__(self, x, y):
        self.x = x
        self.y = y
    
      def mostrar(self):
            print(f"Coordenadas del punto: ({self.x}, {self.y})")
    
      def mover(self, n_x, n_y):
            self.x = n_x
            self.y = n_y
            print(f"El punto se ha movido a: ({self.x}, {self.y})")
    
      def distancia(self, otro_punto):
            distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
            return distancia


punto1 = punto(1, 2)
punto2 = punto(4, 6)


punto1.mostrar()


punto2.mover(7, 8)


distancia = punto1.distancia(punto2)
print(f"La distancia entre los puntos es: {distancia}")


       
         
 
    

  

  

    