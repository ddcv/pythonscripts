import itertools
from itertools import groupby
from operator import itemgetter
import numpy as np
import math


def DP(Input,W,n):
	#Initialize
	A = np.zeros((n,W))
	for i in range(1,n):
		for x in range(W):
			if Input[i][1] > x:
				A[i,x] = A[i-1,x]
			else:
				A[i,x] = max(A[i-1,x], A[i-1, x-Input[i][1] ] + Input[i][0] )
	
	return A


def DPbig(Input,W,n):
	A = [0]*W
	Anext = [0]*W
	for i in range(1,n):
		for x in range(W):
			if Input[i][1] > x:
				Anext[x] = A[x]
			else:
				Anext[x] = max(A[x], A[ x-Input[i][1] ] + Input[i][0] )
			A = Anext
		print i
	
	return Anext
