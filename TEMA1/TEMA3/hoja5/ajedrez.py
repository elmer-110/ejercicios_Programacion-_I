tablero=[[{} for _ in range(8)]for _ in range(8)]    ### list comprehension 



for i in range(2):
    tablero[0][i]={"ficha":"Peon",
                    "color":"negro",
                    "movida":False}

def mover_pieza(x_orig ,y_orig,x_dest,y_dest):
    if "ficha" in tablero[x_orig][y_orig]and not[x_dest][y_dest]  :   # esta verifica si en la casilla de origen hay una ficha
                                                                      # y en la casilla de destino verifica si esta vacía para realizar el mov.

#ahora se realizara el movimiento:
    
        tablero[x_dest][y_dest]=tablero[x_orig][y_orig]    ## la ficha de destino se convierte en la ficha de origen para el sig mov
        tablero[x_orig][y_orig]={}    ## la ficha movida desdel origen se convierte en una casilla vacia , por tanto un dicc vacio 
    
    else:
        print("movimiento invalido")

def imprimir_tablero():
    for fila in tablero:
        for celda in fila:
            if celda:
                print(f"|{celda["ficha"][0]}{celda["color"][0]}|",end="")
            else:
                print("|     |",end="")
        print("\n----------------------------")
def salir():
    print("hasta luego...")
    
imprimir_tablero()
mover_pieza(0,1,1,0) ### casilla de origen (x,y) casilla de destino (x,y)=(x,y;x,y)
print("\ndespues del movimiento:")
imprimir_tablero()

while True:
    print("Elige una opción:")
    print("1-imprimir el tablero:")
    print("2-Salir del juego")
    
    
    opcion=input("Ingresa la opción deseada")
    if opcion=="1":
        imprimir_tablero()
    elif opcion=="2":
        salir()
        break
    else:
        print("opcion invalida")
        
        