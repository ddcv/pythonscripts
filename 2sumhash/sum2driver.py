import numpy.random as nprand
import math
from sum2 import sum2		#2-Sum hash algorithm

f = open('algo1-programming_prob-2sum.txt','r')
#f = open('test.txt','r')

myresult = [int(i.strip()) for i in f]
#print "myresult loaded"
#Run Algorithm
#X = nprand.randint(1000,size = 9)
#print X

#myresult = [1,1,2,2,3,3]

n = len(myresult)
#print n
distinctlen = sum2(myresult,n)
print distinctlen
#print count
#print A
