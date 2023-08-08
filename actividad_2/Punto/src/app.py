from modelo.punto import punto
from modelo.mover import mover
from modelo.distancia import distancia
from modelo.mostrar import mostrar

#punto1 = punto(3, 4)
#3punto1=mover(n_x=6, n_y=8)  
#punto2 = punto(1, 1)
#desplazamiento = punto1.distancia(punto2)
#print("Distancia entre los puntos:", desplazamiento.distancia) 

p_original=punto(x=5,y=3)
print(f"las coordenadas del punto son ({p_original.x} , {p_original.y})")


otro_punto=mover (n_x=7,n_y=8)
print(f"las nuevas coordenadas son ({otro_punto.n_x} , {otro_punto.n_y})")

distancia_entre_puntos=distancia(5,3)
print("Distancia entre los puntos:", distancia_entre_puntos)

