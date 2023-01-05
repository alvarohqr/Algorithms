#PARTICLE SWARM OPTIMIZATION
from __future__ import print_function
import numpy as np
import os
import time


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
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2


def pso_rose(func, bounds, swarm_size=10, inertia=0.5, pa=1.95, ga=2.05, 
        max_vnorm=10, num_iters=100, verbose=False, func_name=None):
    bounds = np.array(bounds)
    assert np.all(bounds[:,0] < bounds[:,1]) 
    dim = len(bounds)
    X = np.random.rand(swarm_size, dim) 
    print('## Optimize:',func_name)

    def clip_by_norm(x, max_norm):
        norm = np.linalg.norm(x)
        return x if norm <=max_norm else x * max_norm / norm

    particles = X * (bounds[:,1]-bounds[:,0]) + bounds[:,0]
    velocities = X * (bounds[:,1]-bounds[:,0]) + bounds[:,0]
    personal_bests = np.copy(particles)
    personal_best_fitness = [np.inf for p in particles] 
    global_best_idx = np.argmin(personal_best_fitness)
    global_best = personal_bests[global_best_idx]
    global_best_fitness = func(global_best)
    history = {'particles':[], 
               'global_best_fitness':[], 
               'global_best':[[np.inf, np.inf] for i in range(num_iters)],
               'obj_func': func_name,}

    for i in range(num_iters):
        StartTime = time.time()
        history['particles'].append(particles)
        history['global_best_fitness'].append(global_best_fitness)
        history['global_best'][i][0] = global_best[0]
        history['global_best'][i][1] = global_best[1]

        if verbose: print('iter# {}:'.format(i), end='')
        for p_i in range(swarm_size):
            fitness = func(particles[p_i])
            if fitness < personal_best_fitness[p_i]:
                personal_bests[p_i] = particles[p_i] 
                personal_best_fitness[p_i] = fitness 
                
        if np.min(personal_best_fitness) < global_best_fitness:
            global_best_idx = np.argmin(personal_best_fitness)
            global_best = personal_bests[global_best_idx]
            global_best_fitness = func(global_best)

        m = inertia * velocities
        acc_local = pa * np.random.rand() * (personal_bests - particles)
        acc_global = ga * np.random.rand() * (global_best - particles)

        velocities = m + acc_local + acc_global
        velocities = clip_by_norm(velocities, max_vnorm)

        particles = particles + velocities
        EndTime = time.time()

        if verbose:
            print(' Fitness:{:.6f}, Position:{}, Velocity:{}, Time:{:.9f}'.format(global_best_fitness, global_best, np.linalg.norm(velocities), EndTime - StartTime))

    return history

def pso_himme(func, bounds, swarm_size=10, inertia=0.5, pa=1.95, ga=2.05, 
        max_vnorm=10, num_iters=100, verbose=False, func_name=None):
    bounds = np.array(bounds)
    assert np.all(bounds[:,0] < bounds[:,1]) 
    dim = len(bounds)
    X = np.random.rand(swarm_size, dim) 
    print('## Optimize:',func_name)

    def clip_by_norm(x, max_norm):
        norm = np.linalg.norm(x)
        return x if norm <=max_norm else x * max_norm / norm

    particles = X * (bounds[:,1]-bounds[:,0]) + bounds[:,0]
    velocities = X * (bounds[:,1]-bounds[:,0]) + bounds[:,0]
    personal_bests = np.copy(particles)
    personal_best_fitness = [np.inf for p in particles] 
    global_best_idx = np.argmin(personal_best_fitness)
    global_best = personal_bests[global_best_idx]
    global_best_fitness = func(global_best)
    history = {'particles':[], 
               'global_best_fitness':[], 
               'global_best':[[np.inf, np.inf] for i in range(num_iters)],
               'obj_func': func_name,}

    for i in range(num_iters):
        StartTime = time.time()
        history['particles'].append(particles)
        history['global_best_fitness'].append(global_best_fitness)
        history['global_best'][i][0] = global_best[0]
        history['global_best'][i][1] = global_best[1]

        if verbose: print('iter# {}:'.format(i), end='')
        for p_i in range(swarm_size):
            fitness = func(particles[p_i])
            if fitness > personal_best_fitness[p_i]:
                personal_bests[p_i] = particles[p_i] 
                personal_best_fitness[p_i] = fitness 
                
        if np.min(personal_best_fitness) > global_best_fitness:
            global_best_idx = np.argmin(personal_best_fitness)
            global_best = personal_bests[global_best_idx]
            global_best_fitness = func(global_best)

        m = inertia * velocities
        acc_local = pa * np.random.rand() * (personal_bests - particles)
        acc_global = ga * np.random.rand() * (global_best - particles)

        velocities = m + acc_local + acc_global
        velocities = clip_by_norm(velocities, max_vnorm)

        particles = particles + velocities
        EndTime = time.time()

        if verbose:
            print(' Fitness:{:.6f}, Position:{}, Velocity:{}, Time:{:.9f}'.format(global_best_fitness, global_best, np.linalg.norm(velocities), EndTime - StartTime))

    return history

print("""
1) Función de rosenbrock
2) Funcion de Himmelblau
""")
op = int(input("\nIngrese su opción: "))

if op == 1:
    history = pso_rose(himmelblau_fun, bounds=[[-4,4],[-4,4]], swarm_size=30, inertia=0.5, num_iters=50, verbose=1, func_name='Rosenbrock Function')
    print('global best:',history['global_best'][-1], ', global best position:', history['global_best'][-1])
    
    
if op == 2:
    history = pso_himme(rosenbrock_fun, bounds=[[-5,5],[-5,5]], swarm_size=30, inertia=0.5, num_iters=50, verbose=1, func_name='Himmelblau Function')
    print('global best:',history['global_best_fitness'][-1], ', global best position:', history['global_best'][-1])
