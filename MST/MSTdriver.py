import numpy.random as nprand
import math
from operator import itemgetter
from MST import prim		#Prim's MST Algorithm

f = open('edges.txt','r')
graphdata = f.readline().rstrip('\n').split(' ')		#read first line to get graph data, strip newline, and put data into 2-element list


Input = []
for line in f:
	sublist = line.rstrip('\n').split(' ')				# Remove newline character and split 2-column row into 2-element list
	Input.append(sublist)						# Append 3-element rowlist to Input list

print graphdata

T = prim(Input,1,graphdata)

mstsum = [sum(i) for i in zip(*T)]

print mstsum

