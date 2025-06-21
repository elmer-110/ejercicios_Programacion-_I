matriz=[[{} for _ in range(5)] for _ in range(5)]     ## LIST COMPREHENSION
### Crea la matriz 5x5 utilizando los diccionarios vacios en las filas  y "_" porque no es necesario ni i ni j


### ahora pasamos a la parte de las coordenadas donde se rellena manualmente

matriz[1][2]={"pista":"estas lejos del tesoro"}
matriz[4][4]={"trampa":"BOOOOM"}
matriz[3][3]={"Tesoro":"10000000€"}


#### BUCLE INFINITO PARA PEDIR COORDENADAS AL USUARIO 


while True:
    x=int(input("introduzca coordenada X (0-4):"))
    y=int(input("Introduce coordenada Y (0-4):"))
   
    lugar=matriz[x][y]
    if "pista "in lugar:
        print(lugar["estas lejos del tesoro"])
    elif "trampa"in lugar:
        print(lugar["tramo"])
        print("has caido en una mina, has perdido")
        break    ### rompe el bucle porque has perdido
    
    elif "tesoro"in lugar :
        print(lugar["has ganado"])
        break               ###rompe el bucle porque has ganado 
    else :
        print("no hay nada aqui sigue buscando ")