import numpy as np 
import random 

figus_paquete = 0
#figus_total = int(input("Ingrese cuantas figuritas tiene su album en total: "))
figus_total =669
def generar_paquete(figus_total, figus_paquete):
    while figus_paquete <= 5: 
        figurita_obtenida = random.randint(0,figus_total-1)
        figus_paquete += 1
        print(figurita_obtenida)
        return figurita_obtenida

def esta_lleno(album):
    if 0 in album:
        return False
    return True

def cuantos_paquetes(figus_total, figus_paquete):
    album = [0]*figus_total
    paquetes = 0
    while esta_lleno(album) == False:
        album[generar_paquete(figus_total, figus_paquete)] = 1
        paquetes += 1
        return paquetes
    print (album)    
    print(esta_lleno(album))
    

lista = [1,2,3,4,5,6,7,8,9,10]
def funcion_promedio(lista):
    promedio = sum(lista)/len(lista) 
    print(promedio)

print(cuantos_paquetes(figus_total, figus_paquete))

def funcion_4 ():
    promedio = []
    n_repeticiones = 100
    i=0
    while i < n_repeticiones:
        promedio.append(cuantos_paquetes(669,figus_paquete))
        i += 1
    print(funcion_promedio(promedio))
    print (promedio)
funcion_4()
