#Programa que imprime los múltiplos de 3 menores que 100

multiplos=0

for i in range(100+1):
    multiplos=(3*i)+3
    print(3*i)
    if multiplos>100:
        break