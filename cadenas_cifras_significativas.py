#Programa que imprime las cifras de un número ordenados de la menos a la más
#significativa.

numero=int(input("Introduzca un número >= que 0: "))

numero=str(numero)
numero_ordenado=""

for i in numero:
    numero_ordenado=i+" "+numero_ordenado

print("Sus cifras de la menos a la más significativa: ",numero_ordenado)

