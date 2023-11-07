def transpose(m):
    result = []
    #Recorrer las columnas.
    for j in range(len(m[0])):
        row = []
        #Recorrer las filas.
        for i in range(len(m)):
            #Meter en la variable fila, la nueva fila cambiada.
            row.append(m[i][j])
        #Añadir las filas al resultado.
        result.append(row)
    m.clear()
    m.extend(result)

m = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
transpose(m)
print(m)


