def capital(cadena):
    nueva_cadena=""
    for i in range(len(cadena)):
        if cadena[i-1]==" " or i==0:
            nueva_cadena=nueva_cadena+(cadena[i].upper())
        else:
            nueva_cadena=nueva_cadena+cadena[i]
    return nueva_cadena

a="olvidaste descongelar el pollo"
print(capital(a))

