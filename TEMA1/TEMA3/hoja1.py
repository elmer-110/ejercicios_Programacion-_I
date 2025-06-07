def devolver_columna(matriz,num_col):
    if len(matriz)!=3 or len(matriz[0])!=3 or len(matriz[1])!=3 or len(matriz[2])!=3:
        return "La matriz no es 3x3"
    columna = []
    for fila in matriz:
        columna.append(fila[num_col])
    return columna

matriz=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

columna=devolver_columna(matriz, 1)
print(columna)
