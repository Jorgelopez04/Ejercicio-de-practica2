def media_aritmetica(lista_numeros):
    
   
    if not lista_numeros: 
        return 0

    total = sum(lista_numeros)  
    media = total / len(lista_numeros)  
    return media



lista=[1, 2, 3, 4, 5]
resultado = media_aritmetica(lista)

resultado
print(f"La media aritmética es: {resultado}")