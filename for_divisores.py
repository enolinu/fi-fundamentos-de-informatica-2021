#Programa que muestra los divisores de un número.

numero=int(input("Introduzca un número natural: "))
divisores=""

print("Los divisores de",numero,"son:",end=" ")
for i in range(1,numero+1):
    if numero%i==0:
        print(i,end=" ")


