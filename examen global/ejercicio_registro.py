def registrar_participantes():
    nombres=[]
    while True:
        solicitar_nombre=input("introduzca su nombre:")
        if solicitar_nombre=="FIN":
            break
        nombres.append(solicitar_nombre)
    return(nombres)
print(registrar_participantes())

participantes_elegidos=[]
def identificar_posiciones(participantes,participantes_elegidos):
    nombres

