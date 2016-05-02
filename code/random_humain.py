
import numpy as np
import matplotlib.pyplot as plt
import random as rdm

X = [99.2737448134/840.0, 46.2177337383/840.0, 120.045368228/840.0, 721.212527429/840.0, 143.540197661/840.0, 571.776370434/840.0, 598.126366262/840.0, 52.115941352/840.0, 42.0417736644/840.0, 538.741292385/840.0, 518.263481391/840.0, 175.365846421/840.0, 175.70652408/840.0, 509.487904781/840.0, 665.220546953/840.0, 107.843690692/840.0, 250.572810286/840.0, 348.2325276/840.0, 700.317947042/840.0, 204.30380195/840.0, 71.2228867334/840.0, 69.1649534744/840.0, 167.664070007/840.0, 704.333028349/840.0, 62.667805421/840.0, 468.002140249/840.0, 673.483206803/840.0, 27.7030413392/840.0, 676.982104859/840.0, 409.041472308/840.0, 311.060650468/840.0, 469.016219537/840.0, 760.052660047/840.0, 418.631829301/840.0, 170.458711362/840.0, 84.7865298883/840.0, 2.10817852813/840.0, 260.881608219/840.0, 721.24024426/840.0, 674.855593939/840.0]
Y = [413.89742215/520.0, 438.789689817/520.0, 384.84428207/520.0, 221.231401317/520.0, 460.034796674/520.0, 423.445591388/520.0, 363.78246882/520.0, 362.845977451/520.0, 459.012119514/520.0, 499.648279021/520.0, 256.729353652/520.0, 263.598711876/520.0, 171.529593994/520.0, 212.115976035/520.0, 408.300863372/520.0, 264.153691021/520.0, 365.890211866/520.0, 391.23662671/520.0, 139.097490435/520.0, 49.0149379327/520.0, 135.818792046/520.0, 372.189666315/520.0, 22.2073475458/520.0, 470.192164411/520.0, 303.99162489/520.0, 384.276077105/520.0, 218.485369279/520.0, 4.29410560891/520.0, 505.685655293/520.0, 393.866678316/520.0, 103.5628732/520.0, 22.9617359038/520.0, 342.742692415/520.0, 180.135332476/520.0, 70.0089350245/520.0, 39.0610218328/520.0, 7.33945030114/520.0, 228.317160901/520.0, 344.087021138/520.0, 87.929330981/520.0]


def getDistanceIpad(X,Y,sizeX,sizeY):
	Dict_distance = {}
	for i in range(0,len(X)):
		for j in range(len(X)):
			distance = np.sqrt(((X[i]-X[j])*sizeX)**2.0+((Y[i]-Y[j])*sizeY)**2.0)/100.0
			Dict_distance[(i,j)] = distance
			Dict_distance[(j,i)] = distance
	return Dict_distance


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

# A = np.array([[0,4,1],[1,1,1],[1,1,1]])

NSales = 40
tmax=1000
sizeX = 1004
sizeY=668


A = getDistanceIpad(X,Y,sizeX,sizeY)
Y2 = []


Y = [0.0]*50000
for i in range(0,50000):
	U = randomSearch(A,N=NSales,n=1)
	Y[i] = U[0]
	# print Y[i]

np.save("humain_random",Y)

# U = np.load("./salesman/geometricPosition_"+str(NSales)+".txt.npy")

# print(veryBest)
# showPoints(U,[])
# showPoints(U,veryBestConfi)
# showEvolution(distance_flow)



