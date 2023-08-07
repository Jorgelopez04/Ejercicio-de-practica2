import math 
def area_circulo(radio):
    area=math.pi *(radio**2)
    
    return area


radio=float(input("ingrese el valor del radio: "))

area=area_circulo(radio)
print(area)

