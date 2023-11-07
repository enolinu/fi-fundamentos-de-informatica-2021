def enBinario(numero):
    binario=""
    while numero >= 1:
        numero = numero//2
        if numero%2==0:
            binario="0"+binario
        else:
            binario="1"+binario
    return binario

num=int(input("Introduzca un número natural: "))
print(enBinario(num))
