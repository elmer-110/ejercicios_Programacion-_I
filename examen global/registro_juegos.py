def registrar_inventario_juegos():
    inventario=[]
    while True:
        titulo=input("introduzca el nombre del videojuego")
        if titulo.upper()=="FIN":
            break
        plataforma=input("introduzca la plataforma de juego:")
        while True:
            precio_coste=float(input("precio de compra:"))
            if precio_coste<0:
                print("el precio no puede ser menor a 0 ")
            break
    #comprobar stock
        while True:
            cantidad=int(input("cantidad en stock:"))
            if cantidad<0:
                print("no puede haber menos que 0 en stock")
            break
        juego={
            "titulo":titulo,
            "plataforma":plataforma,
            "precio_coste":precio_coste,
            "cantidad":cantidad
        }
            
        inventario.append(juego)
    return inventario
inventario=registrar_inventario_juegos()
print(inventario)

def actualizar_precios_juegos(inventario, margen):
    for juego in inventario:
        coste = juego["precio_coste"]
        venta = coste * (1 + margen / 100)
        juego["precio_venta"] = round(venta, 2)

def generar_reporte_inventario(inventario):
    print("\n--- REPORTE INVENTARIO VIDEOJUEGOS ---\n")
    total_general = 0.0

    for juego in inventario:
        titulo = juego["título"]
        platf = juego["plataforma"]
        coste = juego["precio_coste"]
        venta = juego.get("precio_venta", 0.0)
        cantidad = juego["cantidad"]
        valor_stock = round(venta * cantidad, 2)
        total_general += valor_stock

        print(f"Título        : {titulo}")
        print(f"Plataforma    : {platf}")
        print(f"Precio Coste  : {coste:.2f} €")
        print(f"Precio Venta  : {venta:.2f} €")
        print(f"Cantidad      : {cantidad}")
        print(f"Valor Stock   : {valor_stock:.2f} €")
        print("-" * 40)

    print(f"Valor TOTAL INVENTARIO: {total_general:.2f} €")


inventario = registrar_inventario_juegos()
actualizar_precios_juegos(inventario, 25)    # margen del 25 %
generar_reporte_inventario(inventario)
