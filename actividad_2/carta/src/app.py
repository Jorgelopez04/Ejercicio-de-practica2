from modelo.carta import carta
pinta_diamante="diamante" 
pinta_corazon="corazon" 
pinta_Trebol= "trebol"
pinta_picas="picas"
carta_prueba=carta(valor=4,pinta=pinta_diamante)

print(f"el numero de la carta que usted eligio es {carta_prueba.valor} y su pinta es de {carta_prueba.pinta}")