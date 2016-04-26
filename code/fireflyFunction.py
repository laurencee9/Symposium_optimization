"""

Find minimum of a function (in 2D)

"""

import numpy as np
import random as rdm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
plt.rc('font',**{'family':'serif','serif':['Computer Modern']})
plt.rcParams['text.latex.unicode']=True
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 


class Firefly():
	position = np.array([0,0])
	intensity = 1.0



def fly(fireflies, func,beta0=0.5,gamma=1.0,alpha=0.01,delta=0.95):

	

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

def showFunctionFirefly(fireflies,func,xmin,xmax,ymin,ymax,n=50,name="a"):
	R = np.zeros((n,n))
	hx = (xmax-xmin)/n
	hy = (ymax-ymin)/n

	plt.figure(figsize=(3,3))
	for i in range(n):
		for j in range(n):
			R[i,j] = np.abs(func((xmin+hx*i,ymin+hy*j)))
	l = plt.matshow(R,cmap="Blues", origin='lower',extent=[xmin,xmax,ymin,ymax])
	# cbar = plt.colorbar(l)

	X = [fireflies[k].position[0] for k in range(len(fireflies))]
	Y = [fireflies[k].position[1] for k in range(len(fireflies))]
	plt.plot(X,Y,"o",markersize=9,markeredgecolor="none",markerfacecolor = "black")
	print([fireflies[k].intensity for k in range(len(fireflies))])
	plt.xlim([xmin,xmax])
	plt.ylim([ymin,ymax])
	plt.savefig(name)
	plt.clf()
	# plt.show()



def fourMaximum(x,y):
	if x>=0 and y>=0:
		return (np.abs(x-2.5)+np.abs(y-2.5))**0.7
	if x>=0 and y<0:
		return (np.abs(x-2.5)+np.abs(y+2.5))**0.7
	if x<0 and y>=0:
		return (np.abs(x+2.5)+np.abs(y-2.5))**0.7
	if x<0 and y<0:
		return (np.abs(x+2.5)+np.abs(y+2.5))**0.7

def update_line(temps,data,line):
	# X = data[temps]

	line.set_data([f[0] for f in data[temps]],[f[1] for f in data[temps]])
	return line,

def doExtrapolation(data,N):
	newData = []

	for t in range(len(data)*N-N):
		u = t%N
		v = t//N
		L = []
		for j in range(len(data[v])):
			
			newX = data[v][j][0] + u*(data[v+1][j][0]-data[v][j][0])/N
			newY = data[v][j][1] + u*(data[v+1][j][1]-data[v][j][1])/N

			L.append((newX,newY))
		# print(t)
		newData.append([kl for kl in L])
	return newData




# func = lambda x,y : (np.abs(x-2.5)+np.abs(y-2.5))**0.7
func = lambda x : fourMaximum(x[0],x[1])
# func = lambda x : (np.sin((x[0]**2.0+x[1]**2.0)/2.0)/((x[0]/5)**2.0+(x[1]/5.0)**2.0))*-1
# func = lambda x : (np.abs(x[0])+np.abs(x[1]))**0.7
xmin, xmax, ymin, ymax = -5.0,5.0,-5.0,5.0
# showFunction(func,xmin,xmax,ymin,ymax,n=50)
N = 100

fireflies = initialiseFirefly(N, xmin, xmax, ymin, ymax, func)
showFunctionFirefly(fireflies,func,xmin,xmax,ymin,ymax,n=50,name="fireflyout1.pdf")
tmax = 50

data = []
data.append([(f.position[0],f.position[1]) for f in fireflies])
for t in range(tmax):
	fireflies = fly(fireflies, func, beta0=0.8,gamma=5.0,alpha=0.2,delta=0.95)
	data.append([(f.position[0],f.position[1]) for f in fireflies])



# print(data[0])
showFunctionFirefly(fireflies,func,xmin,xmax,ymin,ymax,n=50,name="fireflyout2.pdf")

# extrapo = 8
# data = doExtrapolation(data,N=extrapo)
# fig1 = plt.figure()
# ax = plt.gca()
# l, = ax.plot([f[0] for f in data[0]],[f[1] for f in data[0]], 'ok',markersize=6)
# n=25
# R = np.zeros((n,n))
# hx = (xmax-xmin)/n
# hy = (ymax-ymin)/n

# for i in range(n):
# 	for j in range(n):
# 		R[i,j] = np.abs(func((xmin+hx*i,ymin+hy*j)))
# ax.matshow(R,cmap="Blues", origin='lower',extent=[xmin,xmax,ymin,ymax])

line_ani = animation.FuncAnimation(fig1, update_line, tmax*extrapo, interval=100,fargs=(data, l), blit=True)
line_ani.save('lines.mp4')
