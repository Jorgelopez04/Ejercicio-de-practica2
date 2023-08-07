from random import randint

def completar_matriz(n):
    matriz=[]
    
    for i in range(n):
        fila=[]
        
        for j in range (n):
            fila.append(randint(1,10))
            
        matriz.append(fila)
        
    return matriz


resultado= completar_matriz(5)
print(resultado)