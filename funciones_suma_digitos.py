#Programa que devuelve la suma de las cifras de un número

#Creamos función que devuelve la suma de las cifras de un número

def sumaDigitos(n):
    str_numero=str(n)
    suma=0
    for i in str_numero:
        cifra=int(i)
        suma=suma+cifra
    return suma

print(sumaDigitos(54))

#Programa principal

numero=int(input("Introduzca un número no negativo:"))
if numero<10:
    print(numero)
else:
    print(sumaDigitos(numero))
