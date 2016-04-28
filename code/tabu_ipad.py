
import numpy as np
import matplotlib.pyplot as plt
import random as rdm


X = [99.2737448134/840.0, 46.2177337383/840.0, 120.045368228/840.0, 721.212527429/840.0, 143.540197661/840.0, 571.776370434/840.0, 598.126366262/840.0, 52.115941352/840.0, 42.0417736644/840.0, 538.741292385/840.0, 518.263481391/840.0, 175.365846421/840.0, 175.70652408/840.0, 509.487904781/840.0, 665.220546953/840.0, 107.843690692/840.0, 250.572810286/840.0, 348.2325276/840.0, 700.317947042/840.0, 204.30380195/840.0, 71.2228867334/840.0, 69.1649534744/840.0, 167.664070007/840.0, 704.333028349/840.0, 62.667805421/840.0, 468.002140249/840.0, 673.483206803/840.0, 27.7030413392/840.0, 676.982104859/840.0, 409.041472308/840.0, 311.060650468/840.0, 469.016219537/840.0, 760.052660047/840.0, 418.631829301/840.0, 170.458711362/840.0, 84.7865298883/840.0, 2.10817852813/840.0, 260.881608219/840.0, 721.24024426/840.0, 674.855593939/840.0]
Y = [413.89742215/520.0, 438.789689817/520.0, 384.84428207/520.0, 221.231401317/520.0, 460.034796674/520.0, 423.445591388/520.0, 363.78246882/520.0, 362.845977451/520.0, 459.012119514/520.0, 499.648279021/520.0, 256.729353652/520.0, 263.598711876/520.0, 171.529593994/520.0, 212.115976035/520.0, 408.300863372/520.0, 264.153691021/520.0, 365.890211866/520.0, 391.23662671/520.0, 139.097490435/520.0, 49.0149379327/520.0, 135.818792046/520.0, 372.189666315/520.0, 22.2073475458/520.0, 470.192164411/520.0, 303.99162489/520.0, 384.276077105/520.0, 218.485369279/520.0, 4.29410560891/520.0, 505.685655293/520.0, 393.866678316/520.0, 103.5628732/520.0, 22.9617359038/520.0, 342.742692415/520.0, 180.135332476/520.0, 70.0089350245/520.0, 39.0610218328/520.0, 7.33945030114/520.0, 228.317160901/520.0, 344.087021138/520.0, 87.929330981/520.0]


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

def getDistanceIpad(X,Y,sizeX,sizeY):
	Dict_distance = {}
	for i in range(0,len(X)):
		for j in range(len(X)):
			distance = np.sqrt(((X[i]-X[j])*sizeX)**2.0+((Y[i]-Y[j])*sizeY)**2.0)/100.0
			Dict_distance[(i,j)] = distance
			Dict_distance[(j,i)] = distance
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
def updateTabuList(tabu,newObject,size):
	if len(tabu)<size:
		tabu.append(newObject)
	else:
		tabu.append(newObject)
		del tabu[0]
	return tabu


def tabuSearch(A,tmax=100,N=20,memory=50):

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
			updateTabuList(tabuList,bestConfiguration,size=memory)
			configuration = [a for a in bestConfiguration]
		else:
			print("yo")
			break

	# print(configuration)
	return configuration, distance_flow, veryBest, veryBestConfi

def showPoints(U,configuration):

	plt.figure(figsize=(5.5,5))
	X = [U[configuration[i],0] for i in range(len(configuration))]
	Y = [1.0-U[configuration[i],1] for i in range(len(configuration))]
	plt.plot(X,Y,"-",linewidth=8,color="#0075FF")

	for i in range(len(U)):
		plt.plot(U[i,0],1.0-U[i,1],"o",markersize=12,markerfacecolor="white",markeredgecolor="#0075FF",markeredgewidth=4)
	

	plt.xticks([])
	plt.yticks([])
	# plt.xlim([-0.5,1.5])
	# plt.ylim([-0.5,1.5])
	plt.savefig("best_tabu_of_all.pdf",bbox_inches='tight')
	plt.show()


def showEvolution(distance_flow):
	plt.plot(distance_flow)
	plt.show()

# A = np.array([[0,4,1],[1,1,1],[1,1,1]])
NSales = 40
tmax=10000
sizeX = 1004
sizeY=668
#Size retina
# sizeX = 1346
# sizeY = 924

A = getDistanceIpad(X,Y,sizeX,sizeY)
# Y2 = []
# configuration, distance_flow, veryBest, veryBestConfi = tabuSearch(A,N=NSales,tmax=tmax,memory=200)
# print(veryBest)
# print(veryBestConfi)

# bestofall = 1000.0
# bestofallconf = []
# for i in range(50):
# 	configuration, distance_flow, veryBest, veryBestConfi = tabuSearch(A,N=NSales,tmax=tmax)
# 	Y2.append(veryBest)
# 	if veryBest<bestofall:
# 		bestofall = veryBest
# 		bestofallconf = [a for a in veryBestConfi]
# 	print(veryBest)
# # print(Y)

# np.save("ipad_tabu_best",Y2)
# print(bestofallconf,bestofall)

U = np.zeros((NSales,2))
U[:,0] = X
U[:,1] = Y


# configuration, distance_flow, veryBest, veryBestConfi = tabuSearch(A,N=NSales,tmax=tmax)
# print(veryBest)
showPoints(U,[36, 27, 35, 31, 39, 18, 3, 26, 5, 9, 28, 23, 32, 38, 14, 6, 10, 13, 37, 12, 11, 2, 4, 16, 17, 29, 25, 33, 30, 19, 22, 34, 20, 15, 24, 7, 21, 0, 1, 8])
# showPoints(U,veryBestConfi)
# showEvolution(distance_flow)

# 46.094189530303815, [36, 27, 35, 20, 15, 24, 7, 21, 4, 16, 17, 29, 25, 5, 9, 28, 23, 14, 6, 13, 31, 39, 18, 26, 3, 32, 38, 10, 33, 37, 30, 19, 22, 34, 12, 11, 2, 0, 1, 8]
# L = [39, 18, 26, 3, 32, 38, 14, 23, 28, 9, 5, 6, 25, 29, 17, 16, 4, 8, 1, 0, 2, 21, 7, 24, 15, 11, 37, 12, 20, 36, 27, 35, 22, 34, 19, 30, 31, 33, 13, 10]
# print(getDistanceForConfiguration(L,A))