import math
class distancia:


    def calcular_distancia(self, otro_punto):
        distancia_x = self.x - otro_punto.x
        distancia_y = self.y - otro_punto.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return distancia