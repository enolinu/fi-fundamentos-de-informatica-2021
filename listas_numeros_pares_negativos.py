def numerosPares(lista):
    pares = 0
    lista_copia=[]
    for i in range(len(lista)):
        if isinstance(lista[i],int) and lista[i]>0 and lista[i]%2==0:
            pares+=1
            lista[i]=-lista[i]
    return pares

numeros = [1,2,3,4,5,6,7,8,9]
print(numerosPares(numeros))
print(numeros)



