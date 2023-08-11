import math
class punto:


    def punto_pertenece(self, x):
        distancia_al_centro = math.sqrt((x - self.centro_x) ** 2 + (self.radio - self.radio) ** 2)
        return distancia_al_centro 