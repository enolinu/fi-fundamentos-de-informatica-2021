#Programa que calcula una exresión matemática (un sumatorio creo).

suma=0

for i in range(1,100+1):
    suma=suma+((i**2+1)/i)

print(suma)
