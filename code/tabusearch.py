
import numpy as np
import matplotlib.pyplot as plt
import random as rdm



def getDistance(filepath):

	fileO = open(filepath,"r")
	Dict_distance = {}

	for line in fileO:
		a = line.split("\t")
		i = int(a[0])
		j = int(a[1])
		distance = float(a[2][:-2])
		Dict_distance[(i,j)] = distance
		Dict_distance[(j,i)] = distance

	# print(Dict_distance)
	return Dict_distance

def getInitialConfiguration(N):
	

	return rdm.sample(range(N),N)

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

def tabuSearch(A,tmax=100,N=20):

	configuration = getInitialConfiguration(N)
	tabuList = []
	distance_flow = []

	veryBest = getDistanceForConfiguration(configuration,A)
	veryBestConfi = 0

	for t in range(tmax):
		minDistance, bestConfiguration = enumerateNeighborhood(configuration, A , tabuList)
		distance_flow.append(minDistance)
		if veryBest>minDistance:
			veryBest = minDistance
			veryBestConfi = [a for a in bestConfiguration]
		if minDistance>0:
			tabuList.append(bestConfiguration)
			configuration = [a for a in bestConfiguration]
		else:
			print("yo")
			break

	# print(configuration)
	return configuration, distance_flow, veryBest, veryBestConfi

def showPoints(U,configuration):

	plt.figure(figsize=(5.5,5))
	X = [U[configuration[i],0] for i in range(len(configuration))]
	Y = [U[configuration[i],1] for i in range(len(configuration))]
	plt.plot(X,Y,"-",linewidth=8,color="#0075FF")

	for i in range(len(U)):
		plt.plot(U[i,0],U[i,1],"o",markersize=12,markerfacecolor="white",markeredgecolor="#0075FF",markeredgewidth=4)
	

	plt.xticks([])
	plt.yticks([])
	plt.xlim([-0.5,10.5])
	plt.ylim([-0.5,10.5])
	plt.savefig("salesman_tabu_n20.pdf",bbox_inches='tight')
	plt.show()


def showEvolution(distance_flow):
	plt.plot(distance_flow)
	plt.show()

# A = np.array([[0,4,1],[1,1,1],[1,1,1]])
NSales = 20
tmax=200

A = getDistance("./salesman/geometricDistance_"+str(NSales)+".txt")
Distance = [0.0]*200
for i in range(100):
	# print(i)
	configuration, distance_flow, veryBest, veryBestConfi = tabuSearch(A,N=NSales,tmax=tmax)
	Distance = [Distance[i]+distance_flow[i]/100.0 for i in range(len(distance_flow))]
	# Y.append(veryBest)
np.savetxt("N_20_distance",Distance)
# np.save("N_20_tabu_best",Y)
# U = np.load("./salesman/geometricPosition_"+str(NSales)+".txt.npy")

# print(veryBest)
# showPoints(U,veryBestConfi)
# showPoints(U,veryBestConfi)
# showEvolution(distance_flow)



