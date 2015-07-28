# To run, provide: Array C
#Divide Algorithm
def compquicksort3(C,l,r):
	if l<r:
		count = r-1-l
		(C,pivloc) = partition(C,l,r) #Partition Subroutine
		(C,cleft) = compquicksort3(C,l,pivloc) # Allocate left 
		(C,cright) = compquicksort3(C,pivloc+1,r) # and right recursions
		out = count + cleft + cright
		return (C,out)
	else:
		return C,0

#Partition Subroutine
def partition(C,l,r):
	i = l + 1
	pivloc = choosepivot(C,l,r)			# Key pivot Choice line
	pivot = C[pivloc]
	C[l],C[pivloc] = C[pivloc],C[l]	#swapping pivot into position
	for j in range(l+1,r):
		if C[j]< pivot:
			C[i],C[j] = C[j],C[i]
			i+=1
	C[l],C[i-1] = C[i-1],C[l]
	return (C,i-1)

def choosepivot(C,l,r):
	n = len(C)/2		  #Otherwise, Find middle of list m
	if n % 2 == 0:	
		m = n -1		  # m If C even
	else:
		m = n			  # m If C odd
	medlist = [l,m,r-1]
	pivplace = medianFast(C[l],C[m],C[r-1])
	pivloc = medlist[pivplace]
	return pivloc

def medianFast(a,b,c):
	if a > b: 
		if b > c: 
			return 1
		elif a > c:
			return 2
		else:
			return 0
	else:
		if b < c: 
			return 1
		elif a > c:
			return 0
		else:
			return 2
