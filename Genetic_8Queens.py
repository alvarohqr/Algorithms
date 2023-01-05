#Problema 8 Reinas con algoritmo genetico
import random

def random_cromosoma(size): 
    return [ random.randint(1, nq) for _ in range(nq) ]

def fitness(cromosoma):
    colision_h = sum([cromosoma.count(queen)-1 for queen in cromosoma])/2 #Colisión horizontal
    colision_d = 0  #Colisión diagonal

    n = len(cromosoma)
    diag_izq = [0] * 2*n
    diag_der = [0] * 2*n
    for i in range(n):
        diag_izq[i + cromosoma[i] - 1] += 1
        diag_der[len(cromosoma) - i + cromosoma[i] - 2] += 1

    colision_d = 0
    for i in range(2*n-1):
        counter = 0
        if diag_izq[i] > 1:
            counter += diag_izq[i]-1
        if diag_der[i] > 1:
            counter += diag_der[i]-1
        colision_d += counter / (n-abs(i-n+1))
    
    return int(maxFitness - (colision_h + colision_d)) 

def prob(cromosoma, fitness):
    return fitness(cromosoma) / maxFitness

def random_pick(poblacion, probs):
    prob_poblacion = zip(poblacion, probs)
    total = sum(w for c, w in prob_poblacion)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(poblacion, probs):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
        
def reproduccion(x, y): #Cruzamiento con 2 puntos
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutar(x):  #Proporciona un elemento de aleatoreidad a los individuos.
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def genetic_queen(poblacion, fitness):
    prob_mutar = random.uniform(0,1)
    new_poblacion = []
    probs = [prob(n, fitness) for n in poblacion]
    for i in range(len(poblacion)):
        x = random_pick(poblacion, probs) #Mejor cromosoma #1
        y = random_pick(poblacion, probs) #Mejor cromosoma #2
        hijo = reproduccion(x, y) #Descendencia de los mejores cromosomas
        if random.random() < prob_mutar:
            hijo = mutar(hijo)
        print_cromosoma(hijo)
        new_poblacion.append(hijo)
        if fitness(hijo) == maxFitness: break
    return new_poblacion

def print_cromosoma(chrom):
    print("Cromosoma = {},  Fitness = {}"
        .format(str(chrom), fitness(chrom)))

if __name__ == "__main__":
    nq = 8
    maxFitness = (nq*(nq-1))/2  
    poblacion = [random_cromosoma(nq) for _ in range(100)]
    
    generacion = 1

    while not maxFitness in [fitness(chrom) for chrom in poblacion]:
        print("=== Generacion {} ===".format(generacion))
        poblacion = genetic_queen(poblacion, fitness)
        print("")
        print("Fitness máximo = {}".format(max([fitness(n) for n in poblacion])))
        generacion += 1
    chrom_out = []
    print("Solución en la generación {}!".format(generacion-1))
    for chrom in poblacion:
        if fitness(chrom) == maxFitness:
            print("");
            print("Una de las soluciones: ")
            chrom_out = chrom
            print_cromosoma(chrom)
            
    tablero = []

    for x in range(nq):
        tablero.append(["x"] * nq)
        
    for i in range(nq):
        tablero[nq-chrom_out[i]][i]="Q" #Colocando las reinas en el tablero
            

    def print_tablero(tablero):
        for row in tablero:
            print (" ".join(row))
            
    print("-------Tablero-------")
    print_tablero(tablero)
