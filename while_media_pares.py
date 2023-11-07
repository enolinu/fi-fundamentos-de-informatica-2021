#Programa que calcula la media de los números de una secuencia de números.
#Se dejan de introducir datos tras meter uno negativo.

#Creamos lista que almacene números introducidos.
numeros_pares=[]

#Pedimos un número.
entrada=float(input("Introduzca número:"))

#Miestras éste no sea negativo...
while entrada>=0:
    #Lo añadimos a la lista si es par.
    if entrada%2==0:
        numeros_pares.append(entrada)
    #Pedimos otro.
    entrada=float(input("Introduzca número:"))

#La media será la suma de los elementos de la lista entre su longitud.
media=sum(numeros_pares)/len(numeros_pares)

#Imprimimos por pantalla el resultado.
print("La media de",numeros_pares,"\n","es",media)
