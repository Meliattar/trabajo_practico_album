import numpy as np 
import random 

figus_paquete = 5
figus_total = (int(input("Ingrese la cantidad total de figuritas de su album: ")))
def generar_paquete(figus_total, figus_paquete):
    i = 0
    paquetes = []
    while i < figus_paquete: 
        paquetes.append(random.randint(0,figus_total-1))
        i +=1
    return paquetes

def esta_lleno(album):
    if 0 in album:
        return False
    return True

def cuantos_paquetes(figus_total, figus_paquete):
    album = [0]*figus_total
    paquetes = 0
    while esta_lleno(album) == False:
        paquetes += 1
        paquete = generar_paquete(figus_total, figus_paquete)
        for indice in paquete:
            album[indice]=1
    print (album)    
    return paquetes 
print(cuantos_paquetes(figus_total,figus_paquete))

    