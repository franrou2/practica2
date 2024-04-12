def mas_influyente (diccionario):
    g_a_f = 1.5
    g_evit = 1.25
    asist = 1
    most_influential =""
    the_highest_value = 0
    for nombre, (goles, goles_evitados, asistencias) in diccionario.items():
        total = (goles * g_a_f) + (goles_evitados * g_evit) + (asistencias * asist)
        if total > the_highest_value:
            the_highest_value = total
            most_influential = nombre
    return the_highest_value, most_influential