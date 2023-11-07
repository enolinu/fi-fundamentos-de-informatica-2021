#Función que suma los divisores de un número para saber si es perfecto.

def suma_divisores(n):
    suma=0
    for i in range(1,n):
        if n%i==0:
            suma=suma+i
    return suma

umbral=int(input("Introduzca el umbral de números a mostrar: "))

print("Umbral =",umbral,"=>",end=" ")

for i in range(2,umbral+1):
    if suma_divisores(i)==i:
        print(i,end=" ")
