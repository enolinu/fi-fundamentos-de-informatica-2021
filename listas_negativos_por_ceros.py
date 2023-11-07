#Función que cambia los negativos de una lista por ceros.

def pon_ceros(lista):
    contador=0
    for i in range(len(lista)):
        if lista[i]<0:
            lista[i]=0
            contador+=1
    return contador

datos=[3,-4,5,7,-1,8]
print(pon_ceros(datos))
print(datos)