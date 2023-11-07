def esPrimo(n):
    if n<2:
        return "NO ES PRIMO"

    for i in range(n-1,1,-1):
        if n%i==0 and i!=1 and n!=i:
            return "NO ES PRIMO"
        else:
            return "ES PRIMO"

numero=int(input("Introduzca un número natural: "))
print("El número",numero,esPrimo(numero))
