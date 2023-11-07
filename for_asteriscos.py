#Programa imprime un número de asteriscos determinado.

numero_de_ast=int(input("Número de asteriscos a mostrar: "))
ast=""

for i in range(numero_de_ast):
    if numero_de_ast!=0:
        ast=ast+"*"
    else:
        ast=""

print(ast)