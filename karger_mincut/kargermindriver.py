import numpy.random as nprand
import math
from kargermincut import kargermincut		#Karger's Random Contraction Alg.

f = open('kargerMinCut.txt','r')
myresult = [[int(i) for i in line.split()] for line in f]
print myresult
#Run Algorithm
#X = nprand.randint(1000,size = 9)
#print X

#n = len(myresult)
#final = kargermincut(myresult,0,n)
#print Y
#print final
#Y,final2 = compquicksort2(myresult,0,n)
#print Y
#print final2
#Y,final3 = compquicksort3(myresult,0,n)
#print Y
#print final3