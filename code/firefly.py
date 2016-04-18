
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
		distance = int(a[2])
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
	Fireflies.append(newFire)
	
	return Fireflies

def updateFireflies(fireFlyA, fireFlyB,A):
	r = fireFlyB.intensity-fireFlyA.intensity
	#on va faire 3 permutations disons
	nPermuation = r

	for n in range(nPermuation):

		index = int(np.floor(rdm.random()*len(fireFlyA.position)))

		newthing = fireFlyA.position[index]
		oldindex = fireFlyB.position.index(newthing)
		fireFlyB.position[oldindex] = fireFlyB.position[index]
		fireFlyB.position[index] = newthing
		# print("inte",getDistanceForConfiguration(fireFlyB.position,A))

	fireFlyB.intensity = getDistanceForConfiguration(fireFlyB.position,A)

	# print(fireFlyB.intensity-fireFlyA.intensity,r)



def moveFirefly(Fireflies, A):

	for i in range(len(Fireflies)):
		hasMoved = False
		for j in range(len(Fireflies)):
			if Fireflies[j].intensity < Fireflies[i].intensity:
			
				updateFireflies(Fireflies[j], Fireflies[i],A)
				Fireflies[i].intensity = getDistanceForConfiguration(Fireflies[i].position,A)
				hasMoved = True

		if hasMoved == False:
			# print
			#random walk
			index1 = int(np.floor(rdm.random()*len(Fireflies[i].position)))
			index2 = int(np.floor(rdm.random()*len(Fireflies[i].position)))

			u = Fireflies[i].position[index1]
			Fireflies[i].position[index1] = Fireflies[i].position[index2]
			Fireflies[i].position[index2] = u


def moveFireflyV2(Fireflies, A):

	for i in range(len(Fireflies)):
		hasMoved = False
		bestj = -1
		bestintensity = 20

		for j in range(len(Fireflies)):
			if Fireflies[i].intensity - Fireflies[j].intensity > bestintensity:
				bestintensity = Fireflies[j].intensity
				bestj = j

		if bestj>=0:
			# print(bestj)
			updateFireflies(Fireflies[bestj], Fireflies[i],A)
			hasMoved = True

		if hasMoved == False:
			# print("random")
			#random walk
			for l in range(0,5):
				index1 = int(np.floor(rdm.random()*len(Fireflies[i].position)))
				index2 = int(np.floor(rdm.random()*len(Fireflies[i].position)))

				u = Fireflies[i].position[index1]
				Fireflies[i].position[index1] = Fireflies[i].position[index2]
				Fireflies[i].position[index2] = u



def doFirefly(A, numberFirely, N, tmax=100):

	Fireflies = initializeFirely(numberFirely,N,A)

	for t in range(tmax):
		

		moveFireflyV2(Fireflies,A)

	for fire in Fireflies:
		print(fire.intensity)





A = getDistance("distance.txt")
numberFirely = 200
N = 50
doFirefly(A, numberFirely,  N, tmax=500)
