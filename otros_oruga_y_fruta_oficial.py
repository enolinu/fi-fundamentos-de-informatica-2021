#El problema de la oruga que come fruta, versión oficial.
oruga_viva=True
fruta_alcanzada=False

distancia_recorrida=0
longitud_rama=10
distancia_a_recorrer=40
dia=1

while oruga_viva and not fruta_alcanzada:
    distancia_recorrida+=2
    distancia_a_recorrer=distancia_a_recorrer-distancia_recorrida
    if distancia_recorrida>=longitud_rama and dia<=10:
        fruta_alcanzada=True
        print("La oruga sobrevive")
    #Anochece
    longitud_rama+=1
    distancia_a_recorrer=distancia_a_recorrer+1
    dia+=1
    if dia==10 and not fruta_alcanzada:
        oruga_viva=False
        print("La oruga ha muerto")
        print("Le faltaron",longitud_rama-distancia_recorrida,"cm para llegar")






