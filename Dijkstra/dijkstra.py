import itertools
from itertools import groupby
# To run, provide: Array C
#					initial value of 0 for pivloc
#Divide Algorithm
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

