"""

Find minimum of a function (in 2D)

"""

import numpy as np
import random as rdm
import matplotlib.pyplot as plt

class Firefly():
	position = np.array([0,0])
	intensity = 1.0



def fly(fireflies, func, tmax=100,beta0=0.5,gamma=1.0,alpha=0.01,delta=0.95):

	for t in range(tmax):

		for i in range(len(fireflies)):
			moved = False
			for j in range(len(fireflies)):
				if fireflies[j].intensity<fireflies[i].intensity:
					r = np.sqrt((fireflies[i].position[0]-fireflies[j].position[0])**2.0+(fireflies[i].position[1]-fireflies[j].position[1])**2.0)
					fireflies[i].position[0] += beta0*np.exp(-1.0*gamma*(r)**2.0)*(fireflies[j].position[0]-fireflies[i].position[0]) + alpha * delta**t*(rdm.random()*2-1)
					fireflies[i].position[1] += beta0*np.exp(-1.0*gamma*(r)**2.0)*(fireflies[j].position[1]-fireflies[i].position[1]) + alpha * delta**t*(rdm.random()*2-1)
					moved = True
					fireflies[i].intensity = np.abs(func(fireflies[i].position))

			if moved == False:
				fireflies[i].position += alpha * delta**t*(rdm.random()*2-1)
				fireflies[i].intensity = np.abs(func(fireflies[i].position))
			#update intensity
			
	return fireflies

def flyGreedy(fireflies, func, tmax=100,beta0=0.5,gamma=1.0,alpha=0.01,delta=0.95):

	for t in range(tmax):

		for i in range(len(fireflies)):
			moved = False
			minj = 0
			minintensity = fireflies[i].intensity

			for j in range(len(fireflies)):
				if fireflies[j].intensity<fireflies[i].intensity:
					if minintensity > fireflies[j].intensity:
						minintensity = fireflies[j].intensity
						minj = j
						moved = True
			if moved:
				r = np.sqrt((fireflies[i].position[0]-fireflies[minj].position[0])**2.0+(fireflies[i].position[1]-fireflies[minj].position[1])**2.0)
				fireflies[i].position[0] += beta0*np.exp(-1.0*gamma*(r)**2.0)*(fireflies[minj].position[0]-fireflies[i].position[0]) + alpha * delta**t*(rdm.random()*2-1)
				fireflies[i].position[1] += beta0*np.exp(-1.0*gamma*(r)**2.0)*(fireflies[minj].position[1]-fireflies[i].position[1]) + alpha * delta**t*(rdm.random()*2-1)
				moved = True
				fireflies[i].intensity = np.abs(func(fireflies[i].position))

			if moved == False:
				fireflies[i].position += alpha * delta**t*(rdm.random()*2-1)
				fireflies[i].intensity = np.abs(func(fireflies[i].position))
			#update intensity
			
	return fireflies

def initialiseFirefly(N, xmin, xmax, ymin, ymax, func):
	fireflies = []
	for i in range(N):
		a = Firefly()
		a.position = np.array([rdm.random()*(xmax-xmin)+xmin,rdm.random()*(ymax-ymin)+ymin])
		a.intensity = np.abs(func(a.position))
		fireflies.append(a)
	return fireflies



def showFunction(func,xmin,xmax,ymin,ymax,n=50):
	R = np.zeros((n,n))
	hx = (xmax-xmin)/n
	hy = (ymax-ymin)/n

	for i in range(n):
		for j in range(n):
			R[i,j] = func((xmin+hx*i,ymin+hy*j))
	l = plt.matshow(R,cmap="RdGy", origin='lower',extent=[xmin,xmax,ymin,ymax])
	cbar = plt.colorbar(l)
	plt.show()

def showFunctionFirefly(fireflies,func,xmin,xmax,ymin,ymax,n=50):
	R = np.zeros((n,n))
	hx = (xmax-xmin)/n
	hy = (ymax-ymin)/n

	for i in range(n):
		for j in range(n):
			R[i,j] = np.abs(func((xmin+hx*i,ymin+hy*j)))
	l = plt.matshow(R,cmap="RdGy", origin='lower',extent=[xmin,xmax,ymin,ymax])
	cbar = plt.colorbar(l)

	X = [fireflies[k].position[0] for k in range(len(fireflies))]
	Y = [fireflies[k].position[1] for k in range(len(fireflies))]
	plt.plot(X,Y,"o",markersize=8,markeredgecolor="none",markerfacecolor = "black")
	print([fireflies[k].intensity for k in range(len(fireflies))])
	plt.show()





func = lambda x : (x[0]**2.0+2.0*x[1]-x[1]**2.0+3.0)/20.0
xmin, xmax, ymin, ymax = -5.0,5.0,-5.0,5.0
# showFunction(func,xmin,xmax,ymin,ymax,n=50)
N = 20

fireflies = initialiseFirefly(N, xmin, xmax, ymin, ymax, func)
showFunctionFirefly(fireflies,func,xmin,xmax,ymin,ymax,n=50)

fly(fireflies, func, tmax=500,beta0=0.5,gamma=0.0,alpha=0.1,delta=0.95)
showFunctionFirefly(fireflies,func,xmin,xmax,ymin,ymax,n=50)


