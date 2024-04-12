# la funcion recibe las listas con datos y crea un diccionario cuya clave son los nombres de los jugadorxs y el valor una tupla con sus estadisticas
def lista_unica(names, goals, goals_avoided, assists):
    lista_nombres = names.split(", ")
    dictionary = {}
    for i in range(len(lista_nombres)):
        nombre = lista_nombres[i]
        goles = goals[i]
        goles_evitados = goals_avoided[i]
        asistencias = assists[i]
        dictionary[nombre] = (goles, goles_evitados, asistencias)
    return dictionary