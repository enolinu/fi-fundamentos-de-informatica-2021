#Pedimos el primer número.
numero=int(input('Introduzca número, "0" para terminar:'))

#Contador de posiciones.
contador=1

#Variable que indica la posición del mayor.
posicion=1

#Variable que guarda el valor del mayor número.
mayor=0

#Mientras el número introducido no sea el cero...
while numero!=0:
    #...contamos una posición...
    contador+=1
    #...pedimos otro número...
    numero=int(input('Introduzca número, "0" para terminar:'))
    #...si es mayor que los anteriores se guarda en la variable.
    if numero>mayor:
        mayor=numero
        posicion=contador

#Imprimimos por pantalla los resultados.
print("El mayor es",mayor,"y se introdujo en la posición",posicion)
