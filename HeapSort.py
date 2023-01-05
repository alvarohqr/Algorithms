#HEAPSORT ARREGLO 1-n
import random
from time import perf_counter

def MAX_HEAPIFY(A, n, i):
	largest = i 
	l = 2 * i + 1	
	r = 2 * i + 2	 
	if l < n and A[largest] < A[l]:
		largest = l
	if r < n and A[largest] < A[r]:
		largest = r
	if largest != i:
		A[i], A[largest] = A[largest], A[i] 
		MAX_HEAPIFY(A, n, largest)

def BUILD_MAX_HEAPIFY(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        MAX_HEAPIFY(A, n, i)

def HEAPSORT(A):
    BUILD_MAX_HEAPIFY(A)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i] 
        MAX_HEAPIFY(A, i, 0)

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

A = rellena(talla)
n = len(A)
while tf-ti<tmin:
    A = rellena(talla)
    HEAPSORT(A)
    rep+=1
    tf=perf_counter()

print("Tiempo de medio de ejecución de heapsort: ",((tf-ti)/rep))