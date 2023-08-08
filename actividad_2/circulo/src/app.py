import math
from modelo.circulo import circulo
from modelo.area import area
from modelo.perimetro import perimetro

resultado=circulo(radio=10,centro=4)
print(f"el radio del circulo es {resultado.radio} y su centro es {resultado.centro}")

area_circulo=area(radio=10)
print("el area es",area)


perimetro_circulo=perimetro()
print("el perimetro del circulo es de ", perimetro_circulo)

