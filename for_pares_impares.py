#Programa que dice el carácter par o impar de cada número de un intervalo.
#(Dice si cada número es par o impar)

cota_inferior=int(input("Introduzca la cota inferior: "))
cota_superior=int(input("Introduzca la cota superior: "))

for i in range(cota_inferior,cota_superior+1):
    if i%2==0:
        print(i,"(par)")
    else:
        print(i,"(impar)")

