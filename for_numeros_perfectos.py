#Programa que clasifica los números en perfectos, abundantes y defectivos.
#Buscar en Google lo que es eso.

numero=int(input("Introduzca un número natural: "))
suma_divisores=0
for i in range(1,numero):
    if numero%i==0:
        suma_divisores=suma_divisores+i

if suma_divisores==numero:
    print("El número",numero,"es perfecto")
elif suma_divisores>numero:
    print("El número",numero,"es abundante")
else:
    if suma_divisores==1:
        print("El número",numero,"es defectivo y primo")
    else:
        print("El número",numero,"es defectivo y NO es primo")


