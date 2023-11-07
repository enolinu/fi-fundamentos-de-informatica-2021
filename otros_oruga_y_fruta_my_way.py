# El ejercicio de la oruga que come fruta (versión alternativa)

distancia_oruga=0
longitud_rama=40

for i in range(10):
    distancia_oruga+=2
    longitud_rama+=1

if distancia_oruga>=longitud_rama:
    print("¡La oruga sobrevive :)!")
else:
    print("La oruga ha muerto :(","le faltaron",longitud_rama-distancia_oruga,"cm para llegar a la fruta")


