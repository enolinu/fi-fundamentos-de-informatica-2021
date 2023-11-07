#Programa que dice si una frase es un palíndromo.

def elimina_espacios(cadena):
    nueva_cadena=""
    for i in cadena:
        if i!=" ":
            nueva_cadena=nueva_cadena+i
    return nueva_cadena

frase_con_espacios=input("Introduzca una frase")
frase=elimina_espacios(frase_con_espacios)

invertida=""

for i in frase:
    invertida=i+invertida

invertida=elimina_espacios(invertida)

if frase==invertida:
    print("La frase",frase_con_espacios,"es un palíndromo")
else:
    print("La frase",frase_con_espacios,"NO es un palíndromo")
