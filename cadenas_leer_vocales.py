def leerVocales(cadena):
    cadena_copia=""
    for i in cadena:
        if i in "aA":
            cadena_copia=cadena_copia+"4"
        elif i in "eE":
            cadena_copia=cadena_copia+"3"
        elif i in "iI":
            cadena_copia=cadena_copia+"1"
        elif i in "oO":
            cadena_copia=cadena_copia+"0"
        else:
            cadena_copia=cadena_copia+i
    return cadena_copia

cadena_copia=""
frase="de vuelta en el internet de los años 80"
frase=leerVocales(frase)
print(frase)

