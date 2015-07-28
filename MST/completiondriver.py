
from completionschedule import completionschedule	#Greedy Algorithm for computing Completion Time
from completionschedule import completionsum		#Compute sum of weighted completion times according to schedule

f = open('jobs.txt','r')
n = int(f.readline().rstrip('\n'))					#print firstline

Input = []
for line in f:
	sublist = line.rstrip('\n').split(' ')				# Remove newline character and split 2-column row into 2-element list
	Input.append(sublist)						# Append 2-element rowlist to Input list

##### Question # 1: Difference Calculation

min_Sched = completionschedule(Input,'difference',n)	#min_wC = minimum sum of weighted completion times
						# Valid selections include:
						# difference: orders schedule by weight - length
						# ratio : orders schedule by ratio of weight/length
min_wC = completionsum(min_Sched,n)
print min_wC

##### Question # 2: Ratio Calculation

Input = []
f = open('jobs.txt','r')
n = int(f.readline().rstrip('\n'))					#print firstline
for line in f:
	sublist = line.rstrip('\n').split(' ')				# Remove newline character and split 2-column row into 2-element list
	Input.append(sublist)						# Append 2-element rowlist to Input list


min_Sched = completionschedule(Input,'ratio',n)	#min_wC = minimum sum of weighted completion times
						# Valid selections include:
						# difference: orders schedule by weight - length
						# ratio : orders schedule by ratio of weight/length
min_wC = completionsum(min_Sched,n)
print min_wC

