#Función que calcula la suma de los elementos de una lista numérica.

def suma(n):
    suma=0
    for i in n:
        suma=suma+i
    return suma

lista=[2,6,5,8,5]
print(suma(lista),sum(lista))