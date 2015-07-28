# To run, provide: Array C
#Divide Algorithm
def compquicksort2(C,l,r):
	if l<r:
		count = r-1-l
		(C,pivloc) = partition(C,l,r) #Partition Subroutine
		(C,cleft) = compquicksort2(C,l,pivloc) # Allocate left 
		(C,cright) = compquicksort2(C,pivloc+1,r) # and right recursions
		out = count + cleft + cright
		return (C,out)
	else:
		return C,0

#Partition Subroutine
def partition(C,l,r):
	i = l+1
	pivot = C[r-1]				# Key pivot Choice line
	C[l],C[r-1] = C[r-1],C[l]	#swapping pivot into position
	for j in range(l+1,r):
		if C[j]< pivot:
			C[i],C[j] = C[j],C[i]
			i+=1
	C[l],C[i-1] = C[i-1],C[l]
	return (C,i-1)
