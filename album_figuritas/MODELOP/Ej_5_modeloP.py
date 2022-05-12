import numpy as np
import random
figus_total = 6

def comprar_figu(figus_total):
        figurita_obtenida = random.randint(0,figus_total-1)
        print(figurita_obtenida)
        return figurita_obtenida
        

def esta_lleno(album):
    if 0 in album:
        return False
    return True  


def cuantas_figus(figus_total):
    album = [0]*figus_total
    completas = 0
    while esta_lleno(album) == False:
        album[comprar_figu(figus_total)] = 1
        completas += 1
    print(album)
    print(esta_lleno(album))
    
    return completas

lista = [1,2,3,4,5,6,7,8,9,10]
def funcion_promedio(lista):
    promedio = sum(lista)/len(lista) 
    print(promedio)

#funcion_promedio(lista)
print(cuantas_figus(figus_total)) #poner texto de "Tuviste que comprar tantas figus para llenar el album"

def funcion_5 ():
    promedios = []
    n_repeticiones = 1000
    i=0
    while i < n_repeticiones:
        promedios.append(cuantas_figus(6))
        i += 1
    print(funcion_promedio(promedios))
funcion_5()


