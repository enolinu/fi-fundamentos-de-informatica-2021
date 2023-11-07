#Cálculo de la suma de los n primeros números enteros donde
#n se pide por teclado
#Enol M. Soto 14-oct-2021

#se pide el número de valores
n=int(input("Suma ¿de cuantos valores?"))

suma=0 # inicialización de la suma
for i in range(1,n+1):
    print(i)
    suma=suma+i #se añade el entero a la suma

#se muestran los resultados
print("la suma de los",n,"primeros numeros enteros es",suma)
