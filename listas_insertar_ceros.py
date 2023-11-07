#Función que inserta un cero antes de cada número negativo de una lista.

def inserta_ceros(lista):
    for i in range(len(lista)-1,0,-1):
        if lista[i]<0:
            lista.insert(i,0)

a=[1,-4,5,6,-7,4,-3]

print(a)
inserta_ceros(a)
print(a)
