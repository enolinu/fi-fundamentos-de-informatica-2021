#Función que da el maximo común divisor de dos números.

def mcd(num1,num2):

    #Bucle for que recorre desde el menor de los numeros hasta el 1.
    for i in range(min(num1,num2),1,-1):

        #Si encuentra un número cuyos restos dan cero...
        if num1%i==0 and num2%i==0:

            #devuelve dicho numero, ya que se recorren de mayor a menor.
            return i

        else:
            #Si no encuentra nunguno, devuelve el 1.
            return 1

a=int(input("Primer Número: "))
b=int(input("Segundo Número: "))
print(mcd(a,b))