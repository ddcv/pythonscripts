import itertools
from itertools import izip
import bisect
from bisect import bisect_left
from bisect import bisect_right

# To run, provide: Array C
#					initial value of 0 for pivloc
#Divide Algorithm
def sum2(A,n):
	#Create hash table
	it = range(1,n+1)
	Asort = sorted(A)
	H = dict(zip(A,it))
	print len(H)
	distinct = {}
#	count = 0
	for x in H:
#		count+=1
#		print count
		xlow = -(x + 10000)
		xhigh = -(x - 10000)
		
		leftindex = bisect_left(Asort,xlow) #Leftbound
		rightindex = bisect_right(Asort,xhigh) #rightbound
		for y in Asort[leftindex:rightindex]:
			if y is not x:
				t = x+y
				#print t
				if t not in distinct:
					distinct[t] = 1
				
		
	return len(distinct)

def find_left(a,x):
	"Find leftmost item greater than or equal to x"
	i = bisect_left(a,x)
	if i != len(a):
		return a[i]
	raise ValueError

def find_right(a,x):
	"find rightmost value less than or equal to x"
	i = bisect_right(a,x)
	if i:
		return a[i-1]
	raise ValueError