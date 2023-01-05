import random 
import decimal
import time

def float_range(start, stop, step):
  while start <= stop:
    yield float(start)
    start += decimal.Decimal(step)

def generate_rosenbrock():
    solution = []
    val_rand = list(float_range(-5, 5, '0.001'))
    x = val_rand[random.randint(0,10001)]
    y = val_rand[random.randint(0,10001)]
    """Rosenbrock function
    Domain: -5 < xi < 5
    Global minimun: f_min(1,..,1)=0
    a, b = 1, 100
    f(x,y) = (a-x)^2 + b(y-x^2)^2
    """
    rosenbrock = (1-x)**2 + 100*(y-x**2)**2
    solution.append(rosenbrock)
    solution.append(x)
    solution.append(y)
    return solution
    
def generate_himme():
    solution = []
    val_rand = list(float_range(-4, 4, '0.001'))
    x = val_rand[random.randint(0,8001)]
    y = val_rand[random.randint(0,8001)]
    """Himmelblau function
    Domain: -4 < xi < 4
    Global minimun: f_min(1,..,1)=0
    f(x,y) = (x^2 + y - 11)^2 + (x - y^2 - 7)^2
    """
    himme = (x**2 + y - 11)**2 + (x - y**2 - 7)**2
    solution.append(himme)
    solution.append(x)
    solution.append(y)
    return solution

def evaluate_rose(current_solution, new_solution): 
    x, y = current_solution, new_solution
    rose_x = (1-x[1])**2 + 100*(x[2]-x[1]**2)**2
    rose_y = (1-y[1])**2 + 100*(y[2]-y[1]**2)**2
    if rose_x < rose_y:
        return (rose_x, x[1], x[2])
    else:
        return (rose_y, y[1], y[2])

def evaluate_himme(current_solution, new_solution): 
    x, y = current_solution, new_solution
    himme_x = (x[1]**2 + x[2] - 11)**2 + (x[1] + x[2]**2 - 7)**2
    himme_y = (y[1]**2 + y[2] - 11)**2 + (y[1] + y[2]**2 - 7)**2
    if himme_x > himme_y:
        return (himme_x, x[1], x[2])
    else:
        return (himme_y, y[1], y[2])

def mutate_solution_rose(val):
    val_rand = list(float_range(0, 1, '0.01'))
    x = val_rand[random.randint(0,100)]
    y = val_rand[random.randint(0,100)]
    val[1] = val[1] + x
    val[2] = val[2] + y
    if val[1] > 5 :
        val[1] = 5
    elif val[1] < -5:
        val[1]= -5
    if val[2] > 5:
        val[2] = 5
    elif val[2] < -5:
        val[2] = -5

def mutate_solution_himme(val):
    val_rand = list(float_range(0, 1, '0.01'))
    x = val_rand[random.randint(0,100)]
    y = val_rand[random.randint(0,100)]
    val[1] = val[1] + x
    val[2] = val[2] + y
    if val[1] > 4 :
        val[1] = 4
    elif val[1] < -4:
        val[1]= -4
    if val[2] > 4:
        val[2] = 4
    elif val[2] < -4:
        val[2] = -4
print("""
1) Función de Rosenbrock
2) Funcion de Himmelblau
""")
op = int(input("\nIngrese su opción: "))

if op == 1:
    
    x = generate_rosenbrock()
    y = generate_rosenbrock() 
    best = evaluate_rose(x,y) 
     
    for i in range(0, 100): 
        StartTime = time.time() 
        if best[0] == 0:
            break
     
        new_solution = list(best) 
        mutate_solution_rose(new_solution) 
        
        best = evaluate_rose(best, new_solution)
        print(i+1, ')' ,'Best score so far: ' ,best[0], ',' , 'Solution x: ',best[1], ',' , 'Solution y: ', best[2])

elif op == 2:
    x = generate_himme()
    y = generate_himme() 
    best = evaluate_himme(x,y)  
     
    for i in range(0, 100): 
        StartTime = time.time() 
        if best[0] == 0:
            break
     
        new_solution = list(best) 
        mutate_solution_himme(new_solution) 
        
        best = evaluate_himme(best, new_solution)
        print(i+1, ')' ,'Best score so far: ' ,best[0], ',' , 'Solution x: ',best[1], ',' , 'Solution y: ', best[2])

endTime = time.time()
print("Tiempo de ejecución: ", endTime - StartTime)
