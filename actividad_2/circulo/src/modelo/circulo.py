import math 


class circulo:
    def __init__(self, centro, radio):
        self.centro_x = centro
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def punto_pertenece(self, x):
        distancia_al_centro = math.sqrt((x - self.centro_x) ** 2 + (self.radio - self.radio) ** 2)
        return distancia_al_centro 


