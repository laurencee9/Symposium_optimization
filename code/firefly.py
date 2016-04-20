
import numpy as np
import random as rdm

class Firefly():
	position = []
	intensity = 0.0



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
	return Dict_distance

def getDistanceForConfiguration(configuration,A):
	distance = 0
	for i in range(1,len(configuration)):
		distance += A[(configuration[i-1],configuration[i])]
	return distance



def initializeFirely(numberFirely,N,A):
	Fireflies = []
	a = range(N)
	for i in range(numberFirely):
		newFire = Firefly()
		newFire.position = rdm.sample(a,N)
		newFire.intensity = getDistanceForConfiguration(newFire.position,A)
		Fireflies.append(newFire)

	# newFire = Firefly()
	# newFire.position = [25, 38, 46, 45, 4, 34, 6, 0, 21, 9, 10, 17, 47, 13, 48, 32, 16, 11, 18, 19, 7, 5, 44, 30, 39, 20, 26, 15, 35, 40, 23, 8, 3, 33, 2, 42, 36, 12, 29, 24, 31, 1, 27, 43, 28, 22, 41, 37, 14, 49]
	# newFire.intensity = getDistanceForConfiguration(newFire.position,A)
	# Fireflies.append(newFire)
	
	return Fireflies

def updateFireflies(fireFlyA, fireFlyB,A, beta0=0.5, gamma=1.0, alpha=5, delta=0.95):

	# Move B in direction of A

	#hamming distance
	r = 0
	G = []
	for i in range(len(fireFlyA.position)):
		if fireFlyA.position[i]!=fireFlyB.position[i]:
			r += 1
			G.append(i)
	# print(r)
	#on va faire 3 permutations disons
	nPermuation = int(rdm.random()*r*gamma)
	# nPermuation = int((beta0*np.exp(-1.0*gamma*r*r)))

	# print(nPermuation)
	for n in range(nPermuation):
		
		index = G[int(np.floor(rdm.random()*len(G)))]


		newthing = fireFlyA.position[index]
		oldindex = fireFlyB.position.index(newthing)
		fireFlyB.position[oldindex] = fireFlyB.position[index]
		fireFlyB.position[index] = newthing

	fireFlyB.intensity = getDistanceForConfiguration(fireFlyB.position,A)




def moveFirefly(Fireflies, A, t,beta0=0.5, gamma=1.0, alpha=5, delta=0.95):

	for i in range(len(Fireflies)):
		hasMoved = False

		for j in range(len(Fireflies)):

			if Fireflies[j].intensity < Fireflies[i].intensity:
			
				updateFireflies(Fireflies[j], Fireflies[i],A, beta0=beta0, gamma=gamma, alpha=alpha, delta=delta)
				Fireflies[i].intensity = getDistanceForConfiguration(Fireflies[i].position,A)
				hasMoved = True

		if hasMoved == False:
			#random walk
			for asd in range(int(alpha*delta**t*rdm.random())):
				index1 = int(np.floor(rdm.random()*len(Fireflies[i].position)))
				index2 = int(np.floor(rdm.random()*len(Fireflies[i].position)))
				u = Fireflies[i].position[index1]
				Fireflies[i].position[index1] = Fireflies[i].position[index2]
				Fireflies[i].position[index2] = u
				Fireflies[i].intensity = getDistanceForConfiguration(Fireflies[i].position,A)


def doFirefly(A, numberFirely, N, tmax=100,beta0=0.5, gamma=1.0, alpha=5, delta=0.95):

	Fireflies = initializeFirely(numberFirely,N,A)

	for t in range(tmax):

		moveFirefly(Fireflies,A,t,beta0=beta0, gamma=gamma, alpha=alpha, delta=delta)

	for fire in Fireflies:
		print(fire.intensity)





A = getDistance("geometricDistance.txt")
numberFirely = 40
N = 20
doFirefly(A, numberFirely,  N, tmax=100, beta0=3.0, gamma=0.2, alpha=6, delta=0.95)
