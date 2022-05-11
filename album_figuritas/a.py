print ("Ingrese el numero de veces que desea ejecutar suma(): ")
cant = int(input())       # python 3x
# cant = int(raw_input()) # python 2x

def suma ():
  a = 10
  b= 3
  print (a + b)
  
for ejecucion in range(cant):
   suma()