import numpy as np
import random
#figus_total = int(input("Ingrese la cantidad tota de figuritas que tiene su album: "))
figus_total = 6
n_repeticiones = 1000
#album = [0]*figus_total
#print(album)
album_6 = [0]*figus_total
#lista = [1,2,3,4,5,6,7,8,9,10]


def comprar_figu(figus_total):
        figurita_obtenida = random.randint(0,figus_total-1)
        print(figurita_obtenida)
        album_6[figurita_obtenida]= 1
        print(album_6)

def esta_lleno(album_6):
    if 0 in album_6:
        return False
    return True  
 
def cuantas_figus(figus_total):
    completas = 0
    comprar_figu(figus_total)
    completas += 1
    return completas

for ejecucion in range(n_repeticiones):
    cuantas_figus(figus_total)
  
def funcion_promedio(album_6):
    promedio = sum(album_6)/len(album_6) 
    print(promedio)

funcion_promedio(album_6)
print(cuantas_figus(figus_total)) #poner texto de "Tuviste que comprar tantas figus para llenar el album"
print(esta_lleno(album_6))