import numpy.random as nprand
import math
from mergesort import mergesort161

#Run Algorithm
#X = nprand.randint(1000,size = 9)
X = [5,3,8, 9, 1, 7, 0, 2, 6, 4]
print X
Y = mergesort161(X)
print Y