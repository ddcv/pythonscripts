import numpy.random as nprand
import math
from knapsackDP import DP
from knapsackDP import DPbig

#f = open('knapsack1.txt','r')
f = open('knapsack_big.txt','r')
knapsackdata = f.readline().rstrip('\n').split(' ')					#print firstline
W = int(knapsackdata[0])
n = int(knapsackdata[1])

Input = []
for line in f:
	sublist = line.rstrip('\n').split(' ')				# Remove newline character and split 2-column row into 2-element list
	Input.append(map(int,sublist))						# Append 2-element rowlist to Input list


#maxuse_Capacity = DP(Input,W,n)
maxuse_Capacity = DPbig(Input,W,n)

print maxuse_Capacity
