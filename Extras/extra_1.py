#(1 punto) Utilizando funciones de numpy y lo obtenido en el ´ıtem 4, estime cu´antos paquetes debe
# comprar para tener una chance del 90% de completar el ´album.
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

#def funcion_4 ():
 #   promedios = []
#    n_repeticiones = 100
#   i=0
#    while i < n_repeticiones:
#        promedios.append(cuantos_paquetes(669,figus_paquete))
#        i += 1
#    print(funcion_promedio(promedios))
#    print (promedios)
#funcion_4()

def funcion_4():
    promedios = []
    n_repeticiones = 100
    i = 0
    while i < n_repeticiones:
        promedios.append(cuantos_paquetes(figus_total,figus_paquete))
        i += 1
    a = np.mean(promedios)
    print(a)
    while a == 90 :
        print(len(promedios))

funcion_4()