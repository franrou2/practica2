from inciso2 import goleador
def promedio_de_goles_del_goleador (diccionario, cantidad_de_partidos):
     capocannoniere,_= goleador (diccionario)
     cantidad_goles_goleador = diccionario[capocannoniere][0]
     promedio = cantidad_goles_goleador / cantidad_de_partidos
     return promedio