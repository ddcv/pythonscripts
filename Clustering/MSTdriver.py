import numpy.random as nprand
import math
from operator import itemgetter
from MST import kruskal		#Kruskal's MST Algorithm (for clustering)
import pickle

f = open('clustering1.txt','r')
graphdata = f.readline().rstrip('\n').split(' ')		#read first line to get graph data, strip newline, and put data into 2-element list
graphdata = map(int,graphdata)


Input = []
for line in f:
	sublist = line.rstrip('\n').split(' ')				# Remove newline character and split 2-column row into 2-element list
	Input.append(map(int,sublist))						# Append 4-element rowlist to Input list

print graphdata

#T = prim(Input,1,graphdata)
uf = kruskal(Input,1,graphdata,4)
ufgroup = uf.groups()
print uf.groups()
fn = open('output.txt', 'wb')  
pickle.dump(uf.groups(), fn)
print len(uf.groups())

minspace = float("inf")
for i in range(1):
	group1 = [x for x in Input if x[0] in ufgroup[i] ]
	group2 = [x for x in group1 if x[1] not in ufgroup[i]]
	print group2
	minspacetemp = min(group2, key = itemgetter(2))
	if minspacetemp < minspace:
		minspace = minspacetemp

#mstsum = [sum(i) for i in zip(*T)]

print minspace

