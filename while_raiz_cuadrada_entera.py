#Programa que calcula la parte entera de la raiz cuadrada de un número.
numero=float(input("Introduzca número:"))
pruebas=0

while pruebas**2<numero:
    pruebas+=1

print(pruebas)
print(numero**0.5)
