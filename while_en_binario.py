#Programa que convierte un número (natural) de formato decimal a binario.

numero=int(input("Introduzca un número natural: "))
numero_copia=numero
en_binario=""


while numero > 0:

    if numero%2==0:
        en_binario="0"+en_binario
    else:
        en_binario="1"+en_binario

    numero=numero//2

print("El número",numero_copia,"en binario es",en_binario)