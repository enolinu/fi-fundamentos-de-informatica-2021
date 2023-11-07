#Función que hace la suma de los divisoresde un número para saber si es perfecto

def suma_divisores(n):
    suma=0
    for i in range(1,n):
        if n%i==0:
            suma=suma+i
    return suma

numero=int(input("Introduzca un número natural mayor que uno"))

if suma_divisores(numero)==numero:
    print("El número",numero,"es perfecto")
else:
    print("El número",numero,"NO es perfecto")