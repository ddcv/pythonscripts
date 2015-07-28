import numpy.random as nprand
import math
from medianmain import medianmain		#2-Sum hash algorithm

f = open('Median.txt','r')
#f = open('test2.txt','r')

myresult = [int(i.strip()) for i in f]
print "myresult loaded"
#Run Algorithm
#X = nprand.randint(1000,size = 9)
#print X

#myresult = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#myresult.reverse()

n = len(myresult)
#print n
count = medianmain(myresult,n)
print count
#print A
