def suma(n1,n2):
    suma=n1+n2
    return suma

def resta(n1,n2):
    resta=n1-n2
    return resta

def multiplicacion (n1,n2):
    multiplicacion=n1*n2
    return multiplicacion

def division (n1,n2):
    if n1<n2:
       n1,n2=n2,n1
    
    division=n1/n2
    return division



n1=float(input("ingrese un numero: "))
n2=float(input("ingrese un numero: "))


resultado_suma=suma(n1, n2)
print(resultado_suma)

resultado_resta=resta(n1, n2)
print(resultado_resta)

resultado_multiplicacion=multiplicacion(n1, n2)
print(resultado_multiplicacion)

resultado_division=division(n1, n2)
print(resultado_division)