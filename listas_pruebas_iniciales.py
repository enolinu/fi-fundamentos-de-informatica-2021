lista1=[5,8,10]
lista2=[3,2,9,12,4]
print(len(lista1))
print(len(lista2))
print(lista1+lista2)
a=lista1+lista2
print(max(a))
print(lista1[0]+lista2[0])
print(lista1[len(lista1)-1]+lista2[len(lista2)-1])
lista1[1]=0
print(lista1)
#Pruebas iniciales de listas.

lista3=lista2
lista3[0]=7
print(lista3,lista2)

for i in lista1:
    print(i)

print("\n")

for j in range(1,len(lista2)+1):
    print(lista2[-j])

suma=0
for k in lista2:
    suma=suma+k
print(suma,sum(lista2))


