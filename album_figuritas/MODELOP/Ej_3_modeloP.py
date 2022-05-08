import numpy as np
import random
figus_total = int(input("Ingrese la cantidad tota de figuritas que tiene su album: "))
album = [0]*figus_total
completas = 0
print(album)

#Comprar figuritas individualmente
def comprar_figu(figus_total):
        figurita_obtenida = random.randint(0,figus_total-1)
        print(figurita_obtenida)
        album[figurita_obtenida]= 1
        print(album)


def cuantas_figus(figus_total):
    comprar_figu(figus_total)
    completas += 1


while 0 in album:
    cuantas_figus(figus_total)


def esta_lleno(album):
    if 0 in album:
        return False
    return True  
print(esta_lleno(album))


    

    

