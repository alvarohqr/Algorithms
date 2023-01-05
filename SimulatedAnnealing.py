import numpy as np
import random
import decimal
import time
import math

def float_range(start, stop, step):
  while start <= stop:
    yield float(start)
    start += decimal.Decimal(step)

values_rose = list(float_range(-5, 5, '0.001'))
values_himme = list(float_range(-4, 4, '0.001'))

def rosenbrock_fun(x):
    """Rosenbrock function
    Domain: -5 < xi < 5
    Global minimun: f_min(1,..,1)=0
    a, b = 1, 100
    f(x,y) = (a-x)^2 + b(y-x^2)^2
    """
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

def himmelblau_fun(x):
    """Himmelblau function
    Domain: -4 < xi < 4
    Global minimun: f_min(1,..,1)=0
    f(x,y) = (x^2 + y - 11)^2 + (x - y^2 - 7)^2
    """
    return (x[0]**2 + x[1] + 11)**2 + (x[0]+ x[1]**2 -7)**2


def get_neighbors_rose():
    respuesta = []
    for a in range(5):	
     	respuesta.append([random.choice(values_rose),random.choice(values_rose)])
    return respuesta
    
def get_cost_rose(state):
    x = float('%.3f'%(-5.0+(float(state[0])*0.001)))
    y = float('%.3f'%(-5.0+((float(state[1])*0.001))))    

    return rosenbrock_fun([x,y])

def simulated_annealing_rose(initial_state):
    initial_temp = 90
    final_temp = .1
    alpha = 0.01
    current_temp = initial_temp
    current_state = initial_state
    solution = current_state

    while current_temp > final_temp:
        neighbor = random.choice(get_neighbors_rose())
        cost_diff = get_cost_rose(current_state) - get_cost_rose(neighbor)

        if cost_diff > 0:
            solution = neighbor
        else:
            if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                solution = neighbor
        current_temp -= alpha

    return solution


def get_neighbors_himme():
    respuesta = []
    for a in range(5):	
     	respuesta.append([random.choice(values_himme),random.choice(values_himme)])
    return respuesta
    
def get_cost_himme(state):
    x = float('%.3f'%(-4.0+(float(state[0])*0.001)))
    y = float('%.3f'%(-4.0+((float(state[1])*0.001))))    

    return himmelblau_fun([x,y])

def simulated_annealing_himme(initial_state):
    initial_temp = 90
    final_temp = .1
    alpha = 0.01
    current_temp = initial_temp
    current_state = initial_state
    solution = current_state

    while current_temp > final_temp:
        neighbor = random.choice(get_neighbors_himme())
        cost_diff = get_cost_himme(current_state) - get_cost_himme(neighbor)

        if cost_diff > 0:
            solution = neighbor
        else:
            if random.uniform(0, 1) > math.exp(-cost_diff / current_temp):
                solution = neighbor
        current_temp -= alpha

    return solution


vals = []
print("""
1) Función de rosenbrock
2) Funcion de Himmelblau
""")
op = int(input("\nIngrese su opción: "))

if op == 1:
    for i in range(50):
        StartTime = time.time()
        vals.append(simulated_annealing_rose(['-5.0','-5.0']))
        print(i+1,')', 'Position: ',vals[i], 'Best: ',rosenbrock_fun(vals[i]))

if op == 2:
    for i in range(50):
        StartTime = time.time()
        vals.append(simulated_annealing_himme(['-4.0','-4.0']))
        print(i+1,')', 'Position: ',vals[i], 'Best: ',himmelblau_fun(vals[i]))

EndTime = time.time()
print("Tiempo de ejecución: ", EndTime - StartTime)

