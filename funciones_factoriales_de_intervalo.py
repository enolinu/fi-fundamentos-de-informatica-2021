#Programa que muestra los factoriales de [0,k].

#Definimos una función que devuelva el factorial de un número

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial

#Bucle for que recorre los factoriales de la variable de control (y los muestra)

k=int(input("Introduzca un número natural: "))
for i in range(k+1):
    print(i,"! =",factorial(i))