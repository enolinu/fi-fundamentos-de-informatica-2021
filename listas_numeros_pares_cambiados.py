def numerosPares(lista):
    pares = 0
    lista_cambiados=[]
    for i in range(len(lista)):
        if isinstance(lista[i],int) and lista[i]>0 and lista[i]%2==0:
            pares+=1
            numeros_cambiados.append(lista[i])
            lista[i]=-lista[i]
    return pares

numeros = [1,2,3,4,5,6,7,8,9]
numeros_cambiados=[]
print(numerosPares(numeros))
print(numeros)
print(numeros_cambiados)
