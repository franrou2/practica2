def goleador (diccionario):
    maximo = -1
    for nombre, (goles, *_) in diccionario.items():
        if goles > maximo:
            maximo = goles
            jugador = nombre
    return jugador, maximo   