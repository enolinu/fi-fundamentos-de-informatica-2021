#Programa que calcula una exresión matemática que viene en el enunciado.

a=int(input("Introduzca la cota inferior: "))
b=int(input("Introduzca la cota superior: "))
suma=0

for i in range(a,b+1):
    suma=suma+((i**2+1)/i)

print(suma)
