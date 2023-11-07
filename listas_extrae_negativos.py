#Función que extrae los negativos de una lista y devuelve otra con los negativos

def extrae_negativos(lista):
    lista_negativos=[]
    for elemento in lista:
        if elemento<0:
            lista_negativos.append(elemento)
    for elemento in lista:
        if elemento<0:
            lista.remove(elemento)
    return lista_negativos

a=[10,11,-7,4.5,-2,-2,6.3,8,-1]
print(extrae_negativos(a))
print(a)
