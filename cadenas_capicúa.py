#Programa que indica si un número es capicua.

numero=int(input("Introduzca un número natural: "))
numero=str(numero)
al_reves=""

for i in numero:
    al_reves=i+al_reves


if numero==al_reves:
    print("El número ",numero,"ES CAPICÚA")
else:
    print("El número",numero,"NO ES CAPICÚA")