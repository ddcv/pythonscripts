import numpy.random as nprand

# Merge Algorithm
def merge(A,B):
	n = 2*len(A)-1
	i = 0
	j = 0
	C = [None]*n
	for k in range(n):
		if A[i] < B[j]:
			C[k] = A[i]
			i+=1
		else:
			C[k] = B[j]
			j+=1
	return C 		# Consider End Cases


# initialize random sorted sub-arrays
left = sorted(nprand.randint(1000,size = 5))
right = sorted(nprand.randint(1000,size = 5))
print(left)
print(right)
C = merge(left,right)
print C