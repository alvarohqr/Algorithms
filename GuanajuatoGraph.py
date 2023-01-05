'''
Seleccionar un estado de la republica y generar un grafo con las localidades de más de 20,000 habitantes.
Ejemplo: https://es.wikipedia.org/wiki/Anexo:Localidades_de_Jalisco_por_poblaci%C3%B3n

Utilizar como arista las carreteras que existan entre ciudades.
(Pueden usar maps.google.com ó https://es.wikipedia.org/wiki/Carreteras_de_M%C3%A9xico)

Utilizar como peso la distancia en km entre las ciudades.
(Igual maps.google.com)

Generar un arbol de esparcimiento mínimo para el conjunto de ciudades / carreteras.

Representarlo en tabla o gráficamente.

Determinar la distancia más larga entre las ciudades del estado en el arbol de esparcimiento mínimo.

Estados válidos: Jalisco, Estado de Mexico, Guanajuato, San Luis Potosí, Puebla, Michoacan, Oaxaca, Chiapas
'''

from collections import defaultdict
class Graph:

	def __init__(self,vertices): 

		self.V = vertices 

		self.graph = defaultdict(list)
		self.grafo = []

	def addEdge(self,u,v,w): 
	    self.graph[u].append([v,w])
	    self.grafo.append([u,v,w])


	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	def KruskalMST(self):

		result = [] 
		i, e = 0, 0
		
		self.grafo = sorted(self.grafo, key=lambda item: item[2])

		parent = []
		rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		while e < self.V - 1:

			u, v, w = self.grafo[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)

		minimumCost = 0
		print ("\n Aristas \t Peso")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d \t %d" % (u, v, weight))
	
	def topologicalSortUtil(self,v,visited,stack): 

		visited[v] = True
        #Recursión para todos los vertices adyacentes al previamente visitado
		if v in self.graph.keys(): 
			for node,weight in self.graph[v]: 
				if visited[node] == False: 
					self.topologicalSortUtil(node,visited,stack) 

		stack.append(v) 
		

	def longestPath(self, s): 

		visited = [False]*self.V #vertices no visitados
		stack =[] 

		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(s,visited,stack) 

		dist = [-1000000000000000000] * (self.V) # Inicializando todos los vertices a
		dist[s] = 0                       # una distancia de menos infinito.      
		
		while stack: 

			i = stack.pop() 

			for node,weight in self.graph[i]: 
				if dist[node] < dist[i] + weight: 
					dist[node] = dist[i] + weight 

		for i in range(self.V): 
			print (ciudades[i],')',"%d" %dist[i]) if dist[i] != -100000000000000 else "Inf",
	
	
		
# Driver code

print(""" 
    0)León de los Aldama, 1)Irapuato, 2)Celaya, 3)Salamanca, 4Silao 
    5Guanajuato, 6)Valle de Santiago, 7)San Francisco , 8)Cortazar, 9)San Miguel de Allende
    10Dolores, 11)Acambaro, 12)Uriangato, 13)San Luis, 14Purisima 
    15Moroleón, 16)Santa Cruz, 17)Penjamo, 18)Salvatierra, 19)Centro Familiar 
    20)Marfil, 21)San Felipe, 22)Apaseo el Alto, 23)Abasolo, 24)Villagrán 
    25)Apaseo el Grande, 26)Yuriria, 27)Comonfor,  28)San José de Iturbide, 29)Romita, 30_Jaral
    """)
    
ciudades = ["León de los Aldama", "Irapuato", "Celaya", "Salamanca", "Silao", 
        "Guanajuato", "Valle de Santiago", "San Francisco" , "Cortazar", "San Miguel de Allende",
        "Dolores", "Acambaro", "Uriangato", "San Luis", "Purisima", 
        "Moroleón", "Santa Cruz", "Penjamo", "Salvatierra", "Centro Familiar",
        "Marfil", "San Felipe", "Apaseo el Alto", "Abasolo", "Villagrán", 
        "Apaseo el Grande", "Yuriria", "Comonfort", "San José de Iturbide", "Romita", "Jaral"]


g = Graph(31)

g.addEdge(0,1,71), g.addEdge(0,3,92), g.addEdge(0,1,71)
g.addEdge(0,3,92), g.addEdge(0,4,35), g.addEdge(0,7,22)
g.addEdge(0,19,8.5), g.addEdge(0,14,25)

g.addEdge(1,2,68), g.addEdge(1,3,22), g.addEdge(1,4,38)
g.addEdge(1,8,56), g.addEdge(1,17,52), g.addEdge(1,23,33)
g.addEdge(1,25,83)

g.addEdge(2,3,42), g.addEdge(2,4,102), g.addEdge(2,8,21)
g.addEdge(2,9,50), g.addEdge(2,10,95), g.addEdge(2,11,74)
g.addEdge(2,18,40), g.addEdge(2,21,142),g.addEdge(2,22,25)
g.addEdge(2,24,22), g.addEdge(2,25,16), g.addEdge(2,26,67)
g.addEdge(2,27,26), g.addEdge(2,30,40) 

g.addEdge(3,4,58)

g.addEdge(4,5,23), g.addEdge(4,6,76), g.addEdge(4,7,74)
g.addEdge(4,8,87), g.addEdge(4,10,76), g.addEdge(4,13,127)
g.addEdge(4,20,18), g.addEdge(4,21,66), g.addEdge(4,22,122)
g.addEdge(4,24,80), g.addEdge(4,25,113),g.addEdge(4,29,13)

g.addEdge(5,9,76), g.addEdge(5,10,54), g.addEdge(5,13,105)
g.addEdge(5,16,77), g.addEdge(5,20,5.1),g.addEdge(5,29,36)

g.addEdge(6,8,33), g.addEdge(6,12,34), g.addEdge(6,15,41)
g.addEdge(6,17,65), g.addEdge(6,23,42), g.addEdge(6,26,30)
g.addEdge(6,30,15)

g.addEdge(7,14,5), g.addEdge(7,19,28), g.addEdge(8,18,35)
g.addEdge(8,22,44), g.addEdge(8,24,9.2),g.addEdge(8,30,20)

g.addEdge(9,11,122), g.addEdge(9,16,72), g.addEdge(9,18,89)
g.addEdge(9,21,92), g.addEdge(9,26,116), g.addEdge(9,27,26)

g.addEdge(10,11,163), g.addEdge(10,13,49), g.addEdge(10,18,129)
g.addEdge(10,20,59), g.addEdge(10,21,53), g.addEdge(10,26,156)
g.addEdge(10,27,66), g.addEdge(10,29,90)

g.addEdge(11,15,61), g.addEdge(11,18,33), g.addEdge(11,21,215)
g.addEdge(11,22,66), g.addEdge(11,25,84), g.addEdge(11,26,58)
g.addEdge(11,27,99)

g.addEdge(12,15,2.8), g.addEdge(12,17,99), g.addEdge(12,26,103)

g.addEdge(13,20,109), g.addEdge(13,28,40)

g.addEdge(14,19,27)

g.addEdge(15,17,99), g.addEdge(15,23,76)

g.addEdge(16,24,15)

g.addEdge(17,23,25)

g.addEdge(18,21,188), g.addEdge(18,26,28), g.addEdge(18,27,65)
g.addEdge(18,30,40)

g.addEdge(20,24,89)

g.addEdge(21,27,117)

g.addEdge(22,24,45), g.addEdge(22,25,15), g.addEdge(22,30,63)

g.addEdge(24,25,36) ,g.addEdge(24,30,28)

print("Grafo carreteras de Guanajuato:\n", g.grafo)

print("\nMST:")
g.KruskalMST()
src=0
print ("\nCamino mas largo desde: ",ciudades[src]) 
g.longestPath(src) 