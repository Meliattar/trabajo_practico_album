import numpy as np 
import random 

figus_paquete = 0
figus_total = int(input("Ingrese cuantas figuritas tiene su album en total: "))
album = [0]*figus_total

def generar_paquete(figus_total, figus_paquete):
    while figus_paquete != 5: 
        figurita_obtenida = random.randint(0,figus_total)
        print(figurita_obtenida)
        album[figurita_obtenida]= 1
        print(album)
        figus_paquete += 1
generar_paquete(figus_total,figus_paquete)