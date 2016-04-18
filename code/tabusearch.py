
import numpy as np


def getDistance(filepath):

	fileO = open(filepath,"r")
	Dict_distance = {}

	for line in fileO:
		a = line.split("\t")
		i = int(a[0])
		j = int(a[1])
		distance = int(a[2])
		Dict_distance[(i,j)] = distance
		Dict_distance[(j,i)] = distance
	return Dict_distance

def getInitialConfiguration(N):
	

	return range(N)

def getDistanceForConfiguration(configuration,A):
	distance = 0
	for i in range(1,len(configuration)):
		distance += A[(configuration[i-1],configuration[i])]
	return distance




def enumerateNeighborhood(configuration, A, tabuList):

	minDistance = -1 #max value
	bestConfiguration = []

	for i in range(len(configuration)):
		for j in range(i+1,len(configuration)):


			newconfiguration = [a for a in configuration]
			a = newconfiguration[i]
			newconfiguration[i] = newconfiguration[j]
			newconfiguration[j] = a


			if newconfiguration not in tabuList:

				newDistance = getDistanceForConfiguration(newconfiguration,A)
		
				if newDistance<minDistance or minDistance<0:
					bestConfiguration = [a for a in newconfiguration]
					minDistance = newDistance

			
			# else:
			
			# 	newDistance = getDistanceForConfiguration(newconfiguration,A)
			# 	#Need to improve this criteria
			# 	if newDistance<minDistance:
			# 		if newDistance<minDistance or minDistance<0:
			# 			bestConfiguration = [a for a in newconfiguration]
			# 			minDistance = newDistance


	return minDistance,bestConfiguration

def tabuSearch(A,tmax=100):

	configuration = getInitialConfiguration(50)
	tabuList = []
	for t in range(tmax):
		minDistance, bestConfiguration = enumerateNeighborhood(configuration, A , tabuList)
		
		if minDistance>0:
			tabuList.append(bestConfiguration)
			configuration = [a for a in bestConfiguration]
		else:
			print("yo")
			break

	print(configuration,getDistanceForConfiguration(configuration,A))



# A = np.array([[0,4,1],[1,1,1],[1,1,1]])
A = getDistance("distance.txt")
configuration = tabuSearch(A)

