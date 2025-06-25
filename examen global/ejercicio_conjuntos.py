conjunto1={1,2,3,4,5,6} ## conjunto definido anteriormente
  #se crea un conjunto vacio inicalemnte para despues añadir los numeros del usuario 
conjunto_usuario=set()


#se hace un bucle for para solicitar al usuario 4 numeros y meterlos en el conjunto antes vacio
for i in range(4):
    numero=int(input("introduzca 4 numeros:"))
    conjunto_usuario.add(numero)

## ahora comprobaremos si el conjunto de numeros del usuario es subconjunto del anterior conjunto.
if conjunto_usuario.issubset(conjunto1):
    print("el conjunto introducido es un subconjunto del conjunto inicial")
else:
    print("el conjunto introducido no es subconjunto del conjunto inical")