#Función que devuelve la suma de los elementos de una lista elevados a "n".

def suma_potencias(lista,n):
    lista_aux=[]
    for i in range(len(lista)):
        lista_aux.append(lista[i]**n)
    suma=sum(lista_aux)
    return(suma)

datos=[2,4,6]
print(suma_potencias(datos,2))
