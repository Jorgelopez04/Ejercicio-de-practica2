import math 

class circulo:

    def __init__(self,radio,centro):
        self.radio=radio
        self.centro=centro

    def area(self,radio):
        area= math.pi*radio**2
        return area
    
    def perimetro(self):
        perimetro=2*math.pi* self.radio
        return perimetro
    

    #def punto(seslf,punto):
        distancia = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia <= self.radio