import random
no_vocales = "BCDFGHJKLMNPARSTVWXYZ"
vocales = "AEIOU"

lista_no_vocales = list(no_vocales)
lista_vocales = list(vocales)

for i in range(100):
    letra_1 = lista_no_vocales[random.randint(0, len(lista_no_vocales))-1]
    letra_2 = lista_vocales[random.randint(0, len(lista_vocales)-1)]
    letra_3 = lista_no_vocales[random.randint(0, len(lista_no_vocales)-1)]
    letra_4 = lista_vocales[random.randint(0, len(lista_vocales)-1)]
    print(letra_1+letra_2+letra_3+letra_4, end=" ")

#VUWU