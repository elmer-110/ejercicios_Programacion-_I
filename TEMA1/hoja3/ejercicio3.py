frutas=[]
for i in range(5):
    fruta= input(f"Introduce una fruta{i+1}: ").lower(
        frutas.append(fruta))

if "fresa" in frutas:
    indice = frutas.index("fresa")
    print(f"La fresa está en la posición {indice} de la lista.")