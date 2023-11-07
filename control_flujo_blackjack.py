j1=int(input("Puntuación del jugador 1: "))
j2=int(input("Puntuación del jugador 2: "))

if j1>21 and j2>21:
    print("ÁMBOS JUGADORES PIERDEN")
elif j1==21 and j2!=21:
    print("GANA EL JUGADOR 1 CON",j1,"PUNTOS")
elif j2==21 and j1!=21:
    print("GANA EL JUGADOR 2 CON",j2,"PUNTOS")
elif j1==j2:
    print("EMPATE")
elif j1>j2:
    print("GANA EL JUGADOR 1 CON",j1,"PUNTOS")
else:
    print("GANA EL JUGADOR 2 CON",j2,"PUNTOS")
