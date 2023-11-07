def numerosPares(lista):
    pares = 0
    for i in lista:
        if isinstance(i,int) and i>0 and i%2==0:
            pares+=1
    return pares

numeros = [1,2,3,4,5,6,7,8,9]
print(numerosPares(numeros))



