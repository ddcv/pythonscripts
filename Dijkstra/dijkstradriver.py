import numpy.random as nprand
import math
from dijkstra import dijkstra		#Dijkstra's Shortest Path Alg.

f = open('dijkstraData.txt','r')
#f = open('test3.txt','r')
myresult = []
for line in f:
	sublist = []
	for subline in line.split():
		sublist.append(tuple(int(i) for i in subline.split(',')))
	myresult.append(sublist)

#print myresult


#myresult = [[int(i) for i in line.split()] for line in f]
#print myresult
#Run Algorithm
#X = nprand.randint(1000,size = 9)
#print X

n = len(myresult)
#print n
A,final = dijkstra(myresult,1,n)
print final
#print A
