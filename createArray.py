#Algoritmo de  genere un arreglo con los números de 1 a n

import random

def rellena(talla):                     
    valores = []                        #O(1)   Se inicializa una lista vacia
    for i in range(1,talla+1):          #O(n)   Ciclo for para generar el arreglo ordenado de 1 a n
        valores.append(i)               #O(1)   valores=[1,2,3,...n]
    random.shuffle(valores)             #O(1)   Función para desordenarlos de forma aleatoria
    return valores                      #O(1)   
    
                                        #Por lo tanto T(n)=O(n)

talla=int(input("Ingrese la talla (longitud) del arreglo: "))
vector=rellena(talla)
print("El vector es: ",vector)