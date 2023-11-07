#Programa que saca los primeros 5 múltiblos de 7 que terminan en 23.

contador=0
factor=1
multiplos=1
while contador<5:
    multiplos=factor*7
    factor+=1
    string=str(multiplos)
    if string[-1]=="3" and string[-2]=="2":
        print(multiplos)
        contador+=1