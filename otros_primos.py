#Programa que muestra los números primos entre 1 y el límite establecido.

def es_primo(n):
    if n==1:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

numero=int(input("Introduzca límite superior: "))

for i in range(1,numero+1):
    if es_primo(i)==True:
        print(i)

