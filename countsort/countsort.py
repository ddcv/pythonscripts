
#Divide Algorithm
def countsort(C):
	if len(C) == 1:		  #If C is one item, return 0 for count
		return (C,0)
	n = len(C)/2		  #Otherwise, Find middle of list m
	if n % 2 == 0:	
		m = n -1		  # m If C even
	else:
		m = n			  # m If C odd
	left = C[0:m]		  # Allocate left block and subdivide
	(sleft,cleft) = countsort(left)
	right = C[m:]		  # Allocate right block and subdivide
	(sright,cright) = countsort(right)
	(D,cD) = merge(sleft,sright) # merge smallest blocks
	out = cleft + cright + cD
	return (D,out)

# Merge Algorithm
def merge(B,C):
	n = len(B) + len(C)
	i = 0
	j = 0
	out = 0
	D = [None]*n
	for k in range(n):
		if i<len(B) and (j>=len(C) or B[i] < C[j]):
			D[k] = B[i]
			i+=1
		else:
			D[k] = C[j]
			j+=1
			out += len(B)-i
	return (D,out) 		# Consider End Cases

#Run Algorithm
#X = nprand.randint(1000,size = 9)
#print X
#mergesort161(X)
#print X