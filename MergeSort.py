#MERGESORT ARREGLO 1-n
import random
from time import perf_counter

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
			
def rellena(talla):                     
    valores=[]                          
    for i in range(1,talla+1):          
        valores.append(i)               
    random.shuffle(valores)             
    return valores

talla=100000
tmin=3
rep=0
ti=tf=perf_counter()
vector=rellena(talla)

while tf-ti<tmin:
    vector=rellena(talla) 
    mergeSort(vector) 
    rep+=1
    tf=perf_counter()
    
print("Tiempo de medio de ejecución de mergesort: ",((tf-ti)/rep))