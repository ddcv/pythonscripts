import numpy.random as nprand
import math
	#Choose from among commented available compquicksorts for hwk problem
from compquicksort1 import compquicksort1		#first Array entry
from compquicksort2 import compquicksort2		#last Array entry
from compquicksort3 import compquicksort3		#median-of-three Array entry

f = open('QuickSort.txt','r')
myresult = [[int(i) for i in line.split()] for line in f]

#Run Algorithm
X = nprand.randint(1000,size = 9)
#print X

n = len(myresult)
Y,final = compquicksort1(myresult,0,n)
#print Y
print final
#Y,final2 = compquicksort2(myresult,0,n)
#print Y
#print final2
#Y,final3 = compquicksort3(myresult,0,n)
#print Y
#print final3
