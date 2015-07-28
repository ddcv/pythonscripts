import numpy.random as nprand
import math
from countsort import countsort


f = open('IntegerArray.txt','r')
myresult = [[int(i) for i in line.split()] for line in f]

#Run Algorithm
#X = nprand.randint(1000,size = 9)
#print X

(Y,final) = countsort(myresult)
print Y
print final