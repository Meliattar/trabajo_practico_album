import numpy as np
import random
figus_total = int(input("Ingrese la cantidad tota de figuritas que tiene su album: "))
album  = [0]*figus_total
print(album)

while 0 in album:
    def comprar_figu(figus_total):
        figurita_obtenida = random.randint(0,figus_total-1)
        print(figurita_obtenida)
        album[figurita_obtenida]= 1
        print(album)
    comprar_figu(figus_total)

def esta_lleno(album):
    if 0 in album:
        return False
    return True  
print(esta_lleno(album))
