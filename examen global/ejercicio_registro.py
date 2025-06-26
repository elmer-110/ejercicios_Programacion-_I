def registrar_participantes():
    nombres=[]
    while True:
        solicitar_nombre=input("introduzca su nombre:")
        if solicitar_nombre=="FIN":
            break
        nombres.append(solicitar_nombre)
    return(nombres)


participantes_elegidos=[]
def identificar_posiciones(participantes,participantes_elegidos):
    posiciones={}
    for elegido in participantes_elegidos:
        if elegido in participantes:
            posiciones[elegido]=participantes.index(elegido)### .index
        else:
            posiciones[elegido]=None
    return posiciones


def actualizar_registro(participantes,poscion,nuevos_participantes):
    posicion=int(input("introduce la posicion del participante a reemplazar:"))
    if 0<= posicion < len(participantes):
        nuevos_participantes=input("introduzca el nuevo nombre:")
    else:
        print("posicion no valida ")
    return 


print(registrar_participantes())
participantes=registrar_participantes()
print(identificar_posiciones(participantes,participantes_elegidos))
print(actualizar_registro(participantes,poscion,nuevos_participantes))

participantes_elegidos=["manuel","jose","miguel"]
participantes[]=


