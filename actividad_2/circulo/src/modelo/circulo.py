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


mi_circulo = circulo(4, 10)


area = mi_circulo.area()
perimetro = mi_circulo.calcular_perimetro()

print("Área:", area)
print("Perímetro:", perimetro)


x_punto = 6

pertenece = mi_circulo.punto_pertenece(x_punto)

if pertenece:
    print(f"El punto ({x_punto}) pertenece al círculo.")
else:
    print(f"El punto ({x_punto}) no pertenece al círculo.")