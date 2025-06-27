def registrar_inventario():
    inventario=[]
    while True:
        titulo= input("introduzca un titulo de un libro:")
        if titulo.upper()=="FIN":
            break
        autor=input("introduzca el autor del libro:")
        
        precio=float(input("introduzca un precio de compra:"))
        libro={"titulo":titulo,"autor":autor,"precio":precio}
        inventario.append(libro)
    return inventario
print (registrar_inventario())

def actualizacion_de_precios(inventario):
    for libro in inventario:
        precio_compra = libro.get("precio", 0)
        libro["precio_venta"] = round(precio_compra * 1.30, 2)
    return inventario




def generar_reporte_inventario(inventario):
    print("\n--- REPORTE DE INVENTARIO ---")
    for libro in inventario:
        print(f"Título: {libro['título']}")
        print(f"Autor: {libro['autor']}")
        print(f"Precio Compra: {libro['precio']:.2f} €")
        print(f"Precio Venta: {libro.get('precio_venta', 0):.2f} €")
        print("-" * 30)
inventario_libros=registrar_inventario()
actualizar_precios=(inventario_libros())
generar_reporte_inventario(inventario_libros)
        
        
