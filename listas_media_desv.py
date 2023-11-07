import math
def mediaDT(lista):
    media=sum(lista)/len(lista)
    stddev=0
    for i in lista:
        stddev = stddev + (i - media) ** 2
    stddev = (stddev / len(lista)) ** (1 / 2)
    return media, stddev

lista=[]
n=int(input("Introduzca el tamaño de la población"))
for i in range(n):
    num=int(input())
    lista.append(num)
print(mediaDT(lista))


