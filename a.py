i = 0

while i < 3:
    i += 1
    print(i)


import numpy as np
import random

figus_total = int(input("Ingrese la cantidad tota de figuritas que tiene su album: "))
album = [0]*figus_total
compradas = 0
while 0 in album:
    def comprar_figu(figus_total):
        figurita_obtenida = random.randint(0,figus_total)
        print(figurita_obtenida)
        compradas += 1
        print(compradas)
    comprar_figu(figus_total)
    

   