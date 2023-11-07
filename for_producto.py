#Programa que multiplica dos números por el método de sumas sucesivas.

numero_1=int(input("Introduca un número >= 0: "))
numero_2=int(input("Introduca otro número >= 0: "))
producto=0

for i in range(1,numero_2+1):
    producto=producto+numero_1

print(numero_1,"x",numero_2,"=",producto)
