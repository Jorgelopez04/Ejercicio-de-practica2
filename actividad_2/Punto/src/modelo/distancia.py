import math
class distancia:


    def __init__(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return distancia
        