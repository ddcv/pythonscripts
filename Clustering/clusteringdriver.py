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



fn = open('output.txt', 'rb')  
ufgroup = pickle.load(fn)
print ufgroup

minspace1 = float("inf")
minspace2 = float("inf")
for i in range(len(ufgroup)):
	group1 = [x for x in Input if x[0] in ufgroup[i] ]
	group2 = [x for x in group1 if x[1] not in ufgroup[i]]

	minspace1temp = min(group2, key = itemgetter(2))
	print minspace1temp
	if minspace1temp[2] < minspace1:
		minspace1 = minspace1temp[2]
for i in range(len(ufgroup)):
	group1 = [x for x in Input if x[1] in ufgroup[i] ]
	group2 = [x for x in group1 if x[0] not in ufgroup[i]]

	minspace2temp = min(group2, key = itemgetter(2))
	print minspace2temp
	if minspace2temp[2] < minspace2:
		minspace2 = minspace2temp[2]

#mstsum = [sum(i) for i in zip(*T)]

print minspace1
print minspace2
