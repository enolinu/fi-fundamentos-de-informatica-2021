#Programa que dado un numero indica si es primo o no.

numero=int(input("Escriba un número natural: "))

divisor=numero-1
es_primo=True

while divisor>1:
    if numero%divisor!=0:
        divisor-=1
        continue
    else:
        es_primo=False
        break

if es_primo==True and numero != 1:
    print("El número",numero,"ES PRIMO")
else:
    print("El número",numero,"NO ES PRIMO")

