def mezclar_diccionarios(dic1,dic2,dic3):
    diccionario_mezclado={}
    for d in [dic1,dic2,dic3]:
        diccionario_mezclado.update(d)   # se agregan los elementos de los otros diccionarios
    return diccionario_mezclado

diccionario1={
    "comida1":"patatas",
    "comida2":"olivas"
}
diccionario2={
"comida3":"sandwich"

}
diccionario3={
    "comida4":"pechugas",
    "comida5":"esparragos"
}
resultado=mezclar_diccionarios(diccionario1,diccionario2,diccionario3)
print(resultado)