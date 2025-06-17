def es_heterograma(cadena):
    caracteres_unicos=set()
    for e in cadena:
        if e in caracteres_unicos:
            return False
        caracteres_unicos.add(e)
    return True


palabra=input("Introduzca una palabra:")
if es_heterograma(palabra):
    print(f"La palabra {palabra}, es un heterograma")
else:
    print(f"La palabra {palabra} no es un heterograma")