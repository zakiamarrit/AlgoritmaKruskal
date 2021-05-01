# Program Python untuk mencari algoritma kruskal
# Minimum Spanning Tree yang saling terhubung
# grafik tidak terarah dan meiliki bobot

from collections import defaultdict

# Class untuk mempresentasikan grafik


class Graph:

	def __init__(self, vertices):
		self.V = vertices  # Jumlah seluruh verteks
		self.graph = []  # default dictionary
		# untuk menyimpan grafik

	# berfungsi untuk menambahkan ujung/tepi ke grafik
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# Fungsi utilitas untuk menemukan himpunan elemen i
	# (menggunakan teknik kompresi jalur)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# Fungsi yang menggabungkan dua himpunan x dan y
	# (menggunakan gabungan berdasarkan peringkat)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Melampirkan pohon peringkat yang lebih kecil di bawah akar
		# Pohon dengan peringkat tinggi (Disatukan berdasarkan peringkat)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# Apabila rankingnya sama, maka dijadikan sebagai cabang
		# Dan tingkatan peringkatya satu
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# Fungsi utama untuk membangun algoritma MST menggunakan kruskal
		# algoritma
	def KruskalMST(self):

		result = []  # Menyimpan MST yang dihasilkan

		# Variabel indeks, digunakan untuk tepi yang diurutkan
		i = 0

		# Variabel indeks, digunakan utnuk hasil[]
		e = 0

		# Langkah 1 : sortir semua tepinya
		# Urutan tidak menurun
		# weight.
		# Diberikan grafik, lalu kita buat salinan grafiknya
		self.graph = sorted(self.graph,key=lambda item: item[2])

		parent = []
		rank = []

		# Membuat subset V dengan elemen tunggal
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Jumlah tepi yag diambil = V-1
		while e < self.V - 1:

			# Lagkah 2: Pilih tepi dan kenaikan terkecil
			# indeks untuk literasi berikutnya
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# jika termasuk tepi ini tidak
			# menyebabkan siklus, sertakan dalam hasil
			# menaikkan indeks hasil
			# untuk tepi berikutnya
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
			# Yang lain membuang tepi

		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree", minimumCost)


# Kode pengemudi
g = Graph(6)
g.addEdge(0, 1, 7)
g.addEdge(0, 2, 4)
g.addEdge(0, 3, 15)
g.addEdge(0, 5, 9)
g.addEdge(1, 3, 9)
g.addEdge(1, 5, 8)
g.addEdge(2, 4, 4)
g.addEdge(2, 3, 20)
g.addEdge(3, 5, 5)
g.addEdge(3, 4, 6)
g.addEdge(4, 5, 2)



# Pemanggil fungsi
g.KruskalMST()