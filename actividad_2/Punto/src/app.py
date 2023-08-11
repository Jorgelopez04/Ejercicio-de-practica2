from modelo.punto import punto
from modelo.mover import mover
from modelo.distancia import distancia
from modelo.mostrar import mostrar

punto1 = punto(5, 2)
punto2 = punto(3, 4)


punto1.mostrar()


punto2.mover(9, 7)


distancia = punto1.distancia(punto2)
print(f"La distancia entre los puntos es: {distancia}")

