usuarios={
    "12345678-A":{
        "nombre":"matias",
        "edad":"30",
        "altura":"160"
    },
    "87654321-B": {
    "nombre": "Sara",
    "edad": 28,
    "altura": 160
    },
    "56781234-C": {
    "nombre": "Paula",
    "edad": 31,
    "altura": 162
    },
    "43218765-D": {
    "nombre": "Pablo",
    "edad": 28,
    "altura": 172
    },
    "23456789-E": {
    "nombre": "Luis",
    "edad": 33,
    "altura": 180
    },
    "98765432-F": {
    "nombre": "Ana",
    "edad": 25,
    "altura": 165
    },
    "34567890-G": {
    "nombre": "David",
    "edad": 29,
    "altura": 175
    },
    "76543210-H": {
    "nombre": "Carla",
    "edad": 27,
    "altura": 168
    }
}
        
def comprobar_datos_diccionario(d):
    
    #esto verifica si la variable es un diccionario
    if not isinstance(d,dict):
        print("el dato proporcionado no es un diccionario")
        return False
# ahora se verificara si el diccionario tiene 8 elementos
    if len(d)<8:    ## la funcion len comprueba el numero de pares clave-valor dentro del diccionario en este caso 8
        print("el diccionario tiene menos de 8 elementos ")
        return False 
    for dni,datos in d.items():
        if len (datos)!=3:
            print(f"el usuario{dni} no tiene 3 claves")
            return False
    return True


def buscar_usuarios(d):
    dni_nombre_largo=""
    max_nombre_largo=0
    dni_mayor_edad=""
    max_edad=0
    for dni, datos in d.items():
        # con esto se verifica si este nombre mas largo que el actual mas largo 
    
        if len(datos["nombre"])>max_nombre_largo:
            max_nombre_largo=len(datos["nombre"])
            dni_nombre_largo=dni
            
        # con esto se verifica  si esta edad es mayor que la actual mayor
        
        if datos["edad"] > max_edad:
            max_edad=datos ["edad"]
            dni_mayor_edad=dni
    return dni_nombre_largo,dni_mayor_edad



## ahora llamamos a la funcion para comprobar los datos 
if comprobar_datos_diccionario(usuarios):
    #si los datos son correctos , buscamos a los usuarios  según las condicones 
    usuario_nombre_largo,usuario_mayor_edad=buscar_usuarios(usuarios)
    print(f"DNI del usuario con el nombre más largo :{usuario_nombre_largo}")
    print(f"DNI del usuario con la edad más mayor :{usuario_mayor_edad}")
else:
    ###si hay algun error , el programa debe finalizar  asi que no hacemos nada más
    pass
    
        