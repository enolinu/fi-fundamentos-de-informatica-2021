lado1=float(input("Lado 1: "))
lado2=float(input("Lado 2: "))
lado3=float(input("Lado 3: "))

if lado1+lado2<=lado3:
    print("EL TRIÁNGILO ESPECIFICADO NO EXISTE")
elif lado2+lado3<=lado1:
    print("EL TRIÁNGILO ESPECIFICADO NO EXISTE")
elif lado1+lado3<=lado2:
    print("EL TRIÁNGILO ESPECIFICADO NO EXISTE")
else:
    print("EL TRIÁNGULO ESPECIFICADO EXISTE")
