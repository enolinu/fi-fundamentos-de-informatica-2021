#Programa que pide un numero >= que cero e imprime la suma de sus anteriores.

numero=int(input("Introduzca un número natural o cero: "))
suma=0

for i in range(numero+1):
    suma=suma+i

print("La suma de los",numero,"primeros números naturales es",suma)