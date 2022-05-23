import numpy as np
import random
figus_total = int(input("Ingrese la cantidad tota de figuritas que tiene su album: "))
album = [0]*figus_total
print(album)

def comprar_figu(figus_total):
        figurita_obtenida = random.randint(0,figus_total-1)
        print(figurita_obtenida)
        album[figurita_obtenida]= 1
        print(album)

def esta_lleno(album):
    if 0 in album:
        return False
    return True  


def cuantas_figus(figus_total):
    completas = 0
    while esta_lleno(album) == False:
        comprar_figu(figus_total)
        completas += 1
    return completas

print(cuantas_figus(figus_total)) 
print(esta_lleno(album))



    

