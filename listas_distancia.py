#Función que devuelve la distancia entre dos listas.

def distancia(lista1,lista2):
    dif_longitudes=len(lista1)-len(lista2)
    elementos=0
    for i in lista1:
        if i not in lista2:
            elementos+=1
    distancia=dif_longitudes+elementos
    return distancia

print(distancia([1.9,1.4,1.2,0,1.7],[1.7,1.4,0.1,0,1.7]))
