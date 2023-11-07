#Función que te dice si una lista está ordenada.

def ordenada(lista):
    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            return False
    return True

a=[9,11,10,20]
b=["Ana","Juan","Teresa"]

print(ordenada(a),ordenada(b))
