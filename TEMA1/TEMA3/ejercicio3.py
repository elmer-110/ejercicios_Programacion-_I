def es_heterograma(cadena):
    caracteres_unicos=set()
    for e in cadena:
        if e in caracteres_unicos:
            return False
        caracteres_unicos.append(e)
        