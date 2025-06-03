v1=[1,2,3]
v2=[4,5,6]

#se comprueba que los vectores tengan el mismo tamaño
if len(v1) == len(v2):
#producto escalar de dos vectores
    producto_escalar = 0
    for i in range(len(v1)):
        producto_escalar += v1[i] * v2[i]
    print(f"El producto escalar de los vectores {v1} y {v2} es: {producto_escalar}")

else:
    print("Los vectores no tienen el mismo tamaño, no se puede calcular el producto escalar.")