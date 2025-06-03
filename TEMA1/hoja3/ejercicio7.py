
#se solicita al usuario que introduzca numeros y se almacenan en una lista

numeros=[]
print("introduce numeros, uno a uno y escribe parar para terminar")
while True:
    n=input("introduce un numero: ")
    if n=="parar":
        break
    numeros.append(int(n))

#creamos un numero entero a partir de la lista de numeros
numero_entero = ""
for n in numeros:
    numero_entero+=str(n)
numero_final = int(numero_entero)*2
print("el numero formado es :",numero_final)