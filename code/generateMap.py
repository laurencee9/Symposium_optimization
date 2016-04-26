import numpy as np
import random as rdm
import matplotlib.pyplot as plt

def generatePoints(N,size=10):
	U = np.zeros((N,2))
	for k in range(0,N):
		U[k,0] = rdm.random()*800
		U[k,1] = rdm.random()*520 
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

def showPoints(U):
	for i in range(len(U)):
		plt.plot(U[i,0],U[i,1],"o",markersize=8,markerfacecolor="white",markeredgecolor="red",markeredgewidth=2)
	plt.xticks([])
	plt.yticks([])
	plt.show()



N = 40

U = generatePoints(N)
l = file("test.txt","w")
for i in U[:,0]:
	l.write(str(i))
	l.write(", ")
l.write("] [")


for i in U[:,1]:
	l.write(str(i))
	l.write(", ")
	# 
# print(U[:,0])
# print(U[:,1])
# np.save("./salesman/geometricPosition_"+str(N)+".txt",U)
# Dict = getDistance(U)
# saveDist("./salesman/geometricDistance_"+str(N)+".txt",Dict)

# showPoints(U)