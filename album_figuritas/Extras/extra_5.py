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

    
def funcion_promedio(lista):
    promedio = sum(lista)/len(lista) 
    print(promedio)

print(cuantos_paquetes(figus_total, figus_paquete))

def funcion_4 ():
    promedios = []
    n_repeticiones = 100
    i=0
    while i < n_repeticiones:
        promedios.append(cuantos_paquetes(669,figus_paquete))
        i += 1
    print(funcion_promedio(promedios))
    print (promedios)
    
    for recorrido in range(1,len(promedios)):
        for posicion in range(len(promedios)-recorrido):
            if promedios[posicion] > promedios[posicion + 1]:
                temp = promedios[posicion]
                promedios[posicion] = promedios[posicion + 1]
                promedios[posicion + 1] = temp

    print("lista ordenada")
    print(promedios)
    cantidad = len(promedios)/2
    if cantidad % 2 != 0:
        return(promedios[cantidad])

    return(promedios[int(cantidad- 1)] + promedios[int(cantidad)]) /2
      

print(funcion_4())
