def elementosComunes(lista1,lista2):
    resultado=[]
    for i in lista1:
        if i in lista2 and i not in resultado:
            resultado.append(i)
    return resultado

l1=[1,2,3,4,5,6]
l2=[3,1,5,8,4,6,3]
print(elementosComunes(l1,l2))