import itertools
from itertools import groupby
from operator import itemgetter
# To run, provide: Array C
#					initial value of 0 for pivloc

def completionschedule(Input, algorithm,length):

	Schedule = []
	for i in range(0,length):
		if algorithm == 'difference':
			differencevar = float(Input[i][0]) - float(Input[i][1])
			Input[i].append(differencevar)

		elif algorithm =='ratio':
			ratiovar = float(Input[i][0]) / float(Input[i][1])
			Input[i].append(ratiovar)

		Schedule.append(Input[i])

	Schedule = sorted(Schedule, key = lambda item: (float(item[2]), float(item[0])), reverse = True)

	return Schedule



def completionsum(Schedule,length):

	min_wC = 0
	Ctime = 0

	for i in range(0,length):
		Ctime = Ctime + float(Schedule[i][1])
		min_wC = min_wC + float(Schedule[i][0])*Ctime

	return min_wC
		







