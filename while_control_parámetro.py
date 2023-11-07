#Programa que pide un número positivo y digue pidiendo hasta que se introduzca
#el dato correcto.

#Pide por primera vez el dato...
numero=int(input("Introduzca un número positivo:"))

#Mientras no sea positivo...
while numero<=0:
    #...indica que el dato no es válido...
    print("¡DATO NO VÁLIDO!")
    #...vuelve a pedir el dato.
    numero=int(input("Introduzca un NÚMERO POSITIVO:"))

#Sale del bucle cuando el dato es correcto y lo imprime.
print("El número inroducido es el",numero)
    
