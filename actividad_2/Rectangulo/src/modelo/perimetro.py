class perimetro:

    def calcular_perimetro(self):
        lado_horizontal = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        lado_vertical = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return 2 * (lado_horizontal + lado_vertical)
