# Programa que pide un entero y muestra si es primo o no.
# Enol M. Soto 21-oct-2021

numero=(int(input("Número Entero: ")))
es_primo=True
for divisor in range(2,numero):
    #se mira si tiene divisor exacto.
    if numero%divisor==0:
        #se encontró un divisor exacto.
        es_primo=False
        break

#aqui ya se sabe si es primo o no.

if es_primo==True:
    print("El número", numero, "es primo")
else:
    print("El número", numero, "NO es primo")

#También se puede expresar:

print("El número", numero, "es primo" if es_primo==True else "NO es primo")