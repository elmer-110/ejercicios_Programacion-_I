def registrar_participantes():
    nombres=[]
    while True:
        solicitar_nombre=input("introduzca su nombre:")
        if solicitar_nombre=="FIN":
            break
        nombres.append(solicitar_nombre)

print(registrar_participantes())
