import math
from modelo.circulo import circulo
from modelo.area import area
from modelo.perimetro import perimetro


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


