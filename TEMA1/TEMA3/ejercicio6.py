def comprar_producto(inventario,producto):
    if producto in inventario:
        inventario[producto]-=1
        if inventario[producto]== 0:
            inventario.pop(producto)
            print(f"se vendio la ultima unidad de {producto}")
        else:
            print(f"quedan {inventario[producto]}unidades de {producto}")
    else:
        print(f"No hay {producto} en el inventario ") 
inventario={"manzanas":5,
            "bananas":2 ,
            "naranjas":6,
            "peras":4}     

### Bucle infinito y stop para detener bucle
while True:
    producto=input("ingrese el nombre del producto que desea comprar o escriba Stop para finalizar")
    if producto=="stop":
        break 
    comprar_producto(inventario,producto)
print("inventario final:",inventario)