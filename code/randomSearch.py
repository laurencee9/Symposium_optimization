
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




def randomSearch(A,N=20,n=2000):
	U = [0]*n
	for i in range(n):
		configuration = getInitialConfiguration(N)
		U[i] = getDistanceForConfiguration(configuration,A)

	return U

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


def getDistanceIpad(X,Y,sizeX,sizeY):
	Dict_distance = {}
	for i in range(0,len(X)):
		for j in range(len(X)):
			distance = np.sqrt(((X[i]-X[j])*sizeX)**2.0+((Y[i]-Y[j])*sizeY)**2.0)/100.0
			Dict_distance[(i,j)] = distance
			Dict_distance[(j,i)] = distance
	return Dict_distance



# A = np.array([[0,4,1],[1,1,1],[1,1,1]])
NSales = 50
tmax=50

A = getDistance("./salesman/geometricDistance_"+str(NSales)+".txt")

# Y = [0.0]*10000
# for i in range(0,10000):
# 	U = randomSearch(A,N=20,n=1)
# 	Y[i] = U[0]
	# print Y[i]

# np.save("N_20_random_best",Y)
# np.save("N_20_tabu_best",Y)
U = np.load("./salesman/geometricPosition_"+str(NSales)+".txt.npy")

# print(veryBest)
showPoints(U,[])
# showPoints(U,veryBestConfi)
# showEvolution(distance_flow)



