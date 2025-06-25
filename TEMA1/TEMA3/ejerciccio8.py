def crear_diccionarios(dic1,dic2):
    dic_unido={}
    #se une todas las claves de los diccionarios 1 y 2

    todas_las_claves=set(dic1.keys()).union(dic2.keys())
    for clave in todas_las_claves:
        if clave in dic1 and clave in dic2:
            dic_unido[clave]=[dic1[clave],dic2[clave]]
        elif clave in dic1:
            dic_unido[clave]=dic1[clave]
        else:

            dic_unido=[clave]=dic2[clave]
        
    return dic_unido
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 4, 'c': 3, 'd': 5}

print(crear_diccionarios(diccionario1, diccionario2))