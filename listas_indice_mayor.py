#Función que devuelve el índice del mayor término de una lista.

def indice_mayor(lista):
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
            indice=i
    return(indice)

datos=[4,2,7,1,3]
print(indice_mayor(datos))