def factorial (num):
    factorial=1
    x=1
    if num>=0:
        
        while x <=num:
            factorial= factorial*x
            x+=1
        
        
    return factorial


numero=float(input("ingrese un numero: "))
resultado=factorial(numero)
print(resultado)