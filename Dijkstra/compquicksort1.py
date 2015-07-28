# To run, provide: Array C
#					initial value of 0 for pivloc
#Divide Algorithm
def compquicksort1(C,l,r):
	if l<r:
		count = r-1-l
		(C,pivloc) = partition(C,l,r) #Partition Subroutine
		(C,cleft) = compquicksort1(C,l,pivloc) # Allocate left 
		(C,cright) = compquicksort1(C,pivloc+1,r) # and right recursions
		out = count + cleft + cright
		return (C,out)
	else:
		return C,0

	
#Partition Subroutine
def partition(C,l,r):
	i = l + 1
	pivot = C[l]			# Assign pivot value
	for j in range(l+1,r):
		if C[j]< pivot:
			C[i],C[j] = C[j],C[i]
			i+=1
	C[l],C[i-1] = C[i-1],C[l]
	return (C,i-1)
