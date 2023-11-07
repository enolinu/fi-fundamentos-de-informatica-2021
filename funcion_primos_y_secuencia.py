#Función y programa que indican si un número es primo.

def es_primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    if n==1:
        return False
    return True

numero=int(input("Introduzca un número mayor que cero: "))

while numero>0:
    if es_primo(numero)==True:
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
    numero=int(input("Introduzca un número mayor que cero: "))





