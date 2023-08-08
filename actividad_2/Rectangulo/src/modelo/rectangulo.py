class rectangulo:
    def __init__(self,esquina_i,esquina_d):
        self.esquina_i=esquina_i
        self.esquina_d=esquina_d

    def calcular_perimetro(self):
        lado_horizontal = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        lado_vertical = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return 2 * (lado_horizontal + lado_vertical)

    def calcular_area(self):
        lado_horizontal = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        lado_vertical = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return lado_horizontal * lado_vertical

    def es_cuadrado(self):
        lado_horizontal = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        lado_vertical = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return lado_horizontal == lado_vertical
    

rectangulo1 = rectangulo((0,0),(4,3))
print (rectangulo1) 