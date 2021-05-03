
from collections import defaultdict

class Graph:

	def __init__(self, verteks):
		self.A = verteks  
		self.graph = []

	def addEdge(self, a, b, w):
		self.graph.append([a, b, w])

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

	def Kruskal(self):

		result = []
		i = 0
		e = 0

		self.graph = sorted(self.graph,key=lambda item: item[2])

		parent = []
		rank = []

		for node in range(self.A):
			parent.append(node)
			rank.append(0)

		while e < self.A - 1:

			a, b, w = self.graph[i]
			i = i + 1
			x = self.find(parent, a)
			y = self.find(parent, b)

			if x != y:
				e = e + 1
				result.append([a, b, w])
				self.union(parent, rank, x, y)

		minimumCost = 0
		print ("===== Algoritma Kruskal ===== \n")
		for a, b, weight in result:
			minimumCost += weight
			print("	%d -- %d = %d	" % (a, b, weight))
		print("\n Minimum Spanning Tree", minimumCost)

g = Graph(6)
g.addEdge(0, 1, 7)
g.addEdge(0, 3, 21)
g.addEdge(0, 4, 11)
g.addEdge(1, 2, 20)
g.addEdge(1, 3, 11)
g.addEdge(2, 3, 2)
g.addEdge(2, 5, 9)
g.addEdge(3, 4, 8)
g.addEdge(3, 5, 16)
g.addEdge(4, 5, 15)

g.Kruskal()
