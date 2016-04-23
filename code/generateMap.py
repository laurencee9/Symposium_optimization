import numpy as np
import random as rdm
import matplotlib.pyplot as plt

def generatePoints(N,size=10):
	U = np.zeros((N,2))
	for k in range(0,N):
		U[k,0] = rdm.random()*size
		U[k,1] = rdm.random()*size 
	return U

def getDistance(U):
	N = U.shape[0]
	Dist = {}
	for i in range(N):
		for j in range(i+1,N):
			Dist[(i,j)] = np.sqrt((U[i,0]-U[j,0])**2.0+(U[i,1]-U[j,1])**2.0)
	return Dist

def saveDist(filename,Dist):
	fileO = open(filename,"w")

	for edge in Dist:
		fileO.write(str(edge[0])+"\t"+str(edge[1])+"\t"+str(Dist[edge])+"\n")
	return

def loadDist(filename):
	mat = np.loadtxt(filename)
	Dist = {}
	for row in mat:
		Dist[(row[0],row[1])] = row[2]
	return Dist


def showPoints(U):
	for i in range(len(U)):
		plt.plot(U[i,0],U[i,1],"o",markersize=8,markerfacecolor="white",markeredgecolor="red",markeredgewidth=2)
	plt.xticks([])
	plt.yticks([])
	plt.show()


if __name__ == '__main__':
	N = 20
	U = generatePoints(N)
	np.savetxt("geometricPosition.txt",U)
	Dict = getDistance(U)
	saveDist("geometricDistance.txt",Dict)

	showPoints(U)