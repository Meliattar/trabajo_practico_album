import numpy as np 
import random 

figus_paquete = 0
figus_total = int(input("Ingrese cuantas figuritas tiene su album en total: "))
album = [0]*figus_total

def generar_paquete(figus_total, figus_paquete):
    while figus_paquete <= 5: 
        figurita_obtenida = random.randint(0,figus_total-1)
        #print(figurita_obtenida)
        figus_paquete += 1
        print(figurita_obtenida)
        return figurita_obtenida
generar_paquete(figus_total,figus_paquete)

def esta_lleno(album):
    if 0 in album:
        return False
    return True

def cuantos_paquetes(figus_total, figus_paquete):
    paquetes = 0
    while esta_lleno(album) == False:
        album[generar_paquete(figus_total, figus_paquete)] = 1
        paquetes += 1
        print (album)    
        print(esta_lleno(album))
    return paquetes
print(cuantos_paquetes(figus_total, figus_paquete))


    