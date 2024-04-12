def promedio_de_goles_por_partido (diccionario, cantidad_de_partidos):
    total_goles =0
    for (goles,*_) in diccionario.values():
        total_goles += goles
    promedio = total_goles / cantidad_de_partidos
    return promedio