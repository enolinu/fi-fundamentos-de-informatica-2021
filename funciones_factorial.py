#Función para obtener el factorial de un número.

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial

numero=int(input("Introduzca un número natural: "))
print("El factorial de",numero,"es",factorial(numero))