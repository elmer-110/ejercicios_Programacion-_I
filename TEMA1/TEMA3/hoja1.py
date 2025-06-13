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

columna=devolver_columna(matriz,2)
print(columna)

# Crear una matriz 3x3 mediante bucles
matriz_bucles = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(int(input(f"Introduce el valor para la posición [{i}][{j}]: ")))
    matriz_bucles.append(fila)

print("Matriz creada mediante bucles:")
for fila in matriz_bucles:
    print(fila)