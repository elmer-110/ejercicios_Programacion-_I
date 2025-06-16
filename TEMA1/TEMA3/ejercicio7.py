def apariciones_caracteres(cadena):
    repeticiones={}
    for e in cadena:
     if e in repeticiones:
      repeticiones[e]+=1
     else:
        repeticiones[e]=1
    return repeticiones
      
cadena=input("introduzca una palabra:")
apariciones=apariciones_caracteres(cadena)
print(apariciones)