import itertools
from itertools import groupby
from operator import itemgetter
#import unionfind
# To run, provide: Array C
#					initial value of 0 for pivloc
#Divide Algorithm


def prim(G,s,graphdata):
	#Initialize
	n = int(graphdata[0])		# # of nodes
	m = len(G)			# # of edges
	print m
	X = {}
	X[s] = 1
	T = []
	#Main Loop
	while len(X) < n:
		validset = []
		for i in range(0,m):				#Among all edges (v,w) in E 
			if int(G[i][0]) in X.keys():			#v in X
				if int(G[i][1]) not in X.keys():		# w not in X, 
					Gvalid = map(int, G[i])
					Gvalid.append(i)
					validset.append(Gvalid) 	# add to validset under consideration
			elif int(G[i][1]) in X.keys():			#v in X
				if int(G[i][0]) not in X.keys():		# w not in X, 
					Gvalid = map(int, G[i])
					Gvalid.append(i)
					validset.append(Gvalid) 	# add to validset under consideration
		e = min(validset, key = itemgetter(2))

		T.append(e)
		if e[0] not in X.keys():			#v in X
			X[e[0]] = 1
		elif e[1] not in X.keys():
			X[e[1]] = 1

	#
	return T

def kruskal(G,s,graphdata,clusterbit):
	#Initialize
	n = int(graphdata[0])		# # of nodes
	m = len(G)			# # of edges
	G = sorted(G, key = itemgetter(2) )
	T = G
	uf = unionfind(n)
	i = 0
	graphsize = n
	while i<m:
		print graphsize
		if graphsize > clusterbit:
			if not uf.issame(G[i][0], G[i][1]): #If T[i] has no cycles
				uf.unite(G[i][0], G[i][1]) #unite unionfind
				graphsize = len(uf.groups())

		i = i+1
	return uf







def dijkstra(G,s,n):
	#Initialize
	X = [s]
	A = []
	for x in range(0,n):
		A.append(x*0)		#Computed Shortest Path Distance
	#Main Loop
	while len(X) is not n:
		min_dist = 0
		minimizer = []											#temp variable to find min distance
		for i in range(0,n):									#Among all edges (v,w) in E 
			if G[i][0][0] in X:										#v in X
				for j in range(1,len(G[i])):		
						if G[i][j][0] not in X:						# w not in X, 
							minimizer.append(tuple([A[G[i][0][0]-1] + G[i][j][1],i,j])) # minimize  A[v] + l_vw
		min_dist, min_i, min_j = min([(val, obj,obj2) for val, obj,obj2 in minimizer])#Iterate over 
															#minimizer tuple to find min distance 
															# and give index in minimizer
		wstar = G[min_i][min_j][0]								#Add w* to X
		X.append(wstar)	
		A[wstar-1] =  min_dist					#Set A[w*] := A[v*] + l_v*w*
	#Comment out if using generically
	finalout = [A[7-1],A[37-1],A[59-1],A[82-1],A[99-1],A[115-1],A[133-1],A[165-1],A[188-1],A[197-1]]
	#
	return A, finalout

class unionfind:
	def __init__(self, n):
		self.parent = list(range(1, n + 1))
	def find(self, i):
		if self.parent[i-1] != i: self.parent[i-1] = self.find(self.parent[i-1])
		return self.parent[i-1]
	def unite(self, i, j):
		i = self.find(i)
		j = self.find(j)
		if i != j: self.parent[i-1] = j
	def issame(self, i, j):
		return self.find(i) == self.find(j)
	def groups(self):
		r = range(1,len(self.parent)+1 )
		return [[j for j in r if self.issame(j, i)] for i in r if i == self.parent[i-1]]



