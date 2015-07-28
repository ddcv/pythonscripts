
#Divide Algorithm
def mergesort161(C):
	if len(C) == 1:		  #If C is one item, return
		return C
	n = len(C)/2		  #Otherwise, Find middle of list m
	if n % 2 == 0:	
		m = n -1		  # m If C even
	else:
		m = n			  # m If C odd
	left = C[0:m]		  # Allocate left block and subdivide
	left = mergesort161(left)
	right = C[m:]		  # Allocate right block and subdivide
	right = mergesort161(right)
	print left
	print right
	C = merge(left,right) # merge smallest blocks
	return C

# Merge Algorithm
def merge(A,B):
	n = len(A) + len(B)
	i = 0
	j = 0
	C = [None]*n
	for k in range(n):
		if i<len(A) and (j>=len(B) or A[i] < B[j]):
			C[k] = A[i]
			i+=1
		else:
			C[k] = B[j]
			j+=1
	return C 		# Consider End Cases

#Run Algorithm
#X = nprand.randint(1000,size = 9)
#print X
#mergesort161(X)
#print X