import itertools
from itertools import izip
import heapq
# To run, provide: Array C
#					initial value of 0 for pivloc
#Divide Algorithm
def medianmain(A,n):
	#Create hash table
	k = 1
	heaplow = []
	heaphigh = []
	heapq.heappush(heaphigh,A[0])
	median = [A[0]]
	for i in range(1,n):
		k +=1
		if abs(A[i]) > min(heaphigh):
			heapq.heappush(heaphigh,A[i])
		else:
			heapq.heappush(heaplow,-A[i])
		if k%2 == 0:
			if len(heaphigh) != len(heaplow):
				if len(heaphigh) >len(heaplow):
					heapq.heappush(heaplow,-heapq.heappop(heaphigh))
				else:
					heapq.heappush(heaphigh,-heapq.heappop(heaplow))
			median.append(-min(heaplow))	
		else:
			if len(heaphigh) > len(heaplow):
				median.append(min(heaphigh))
			else:
				median.append(-min(heaplow))
	return sum(median)%10000