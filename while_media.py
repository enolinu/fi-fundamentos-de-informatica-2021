#Programa que calcula la media de una secuencia de números.
#Se dejan de introducir datos tras meter uno negativo.

#Creamos lista que almacene números introducidos.
numeros=[]

#Pedimos un número.
entrada=float(input("Introduzca número:"))

#Miestras éste no sea negativo...
while entrada>=0:
    #Lo añadimos a la lista.
    numeros.append(entrada)
    #Pedimos otro.
    entrada=float(input("Introduzca número:"))

#La media será la suma de los elementos de la lista entre su longitud.
media=sum(numeros)/len(numeros)

#Imprimimos por pantalla el resultado.
print("La media de",numeros,"\n","es",media)
