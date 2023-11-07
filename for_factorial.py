#Programa que pide un numero > que cero e imprime su factorial.

numero=int(input("Introduzca un número natural: "))
factorial=1

for i in range(1,numero+1):
    factorial=factorial*i

print(str(numero)+"!","=",factorial)