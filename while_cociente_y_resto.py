#Programa que calcula el cociente y el resto de dos números.

#Pedimos dividendo y divisor.
dividendo=int(input("Dividendo: "))
divisor=int(input("Divisor: "))

#Creamos una copia del dividendo.
dividendo_copia=dividendo

#Inicializamos la variable cociente.
cociente=0

#Método de las restas sucesivas: miestras el dividendo sea menor o igual que
#el divisor...
while dividendo>=divisor:
    #Modificamos el dividendo.
    dividendo=dividendo-divisor
    #Incrementamos una unidad al cociente.
    cociente+=1

#El resto...
resto=dividendo_copia-divisor*cociente

#Imprimimos por pantalla los resultados.
print(dividendo_copia,"//",divisor,"=",cociente)
print(dividendo_copia,"%",divisor,"=",resto)