
numero = int(input("Introduce un número natural: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(0, 1187):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    