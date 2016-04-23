"""

Find minimum of a function (in 2D)

"""

import numpy as np
import random as rdm
import matplotlib.pyplot as plt



from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
plt.rc('font',**{'family':'serif','serif':['Computer Modern']})
plt.rcParams['text.latex.unicode']=True
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=15) 
plt.rc('ytick', labelsize=15) 


class Info():
	xmin = 0.0
	xmax = 0.0
	ymin = 0.0
	ymax = 0.0
	hx = 0.1
	hy = 0.1
	func = 0
	idxmax=0
	idymax=0

	def __init__(self,_xmin,_xmax,_ymin,_ymax,_func,_hx,_hy):
		self.func=_func
		self.xmin=_xmin
		self.xmax=_xmax
		self.ymin=_ymin
		self.ymax=_ymax
		self.hx=_hx
		self.hy=_hy
		self.idxmax = (xmax-xmin)/hx
		self.idymax = (ymax-ymin)/hy
		return

	def getFunc(self,idx,idy):
		x = xmin+hx*idx
		y = ymin+hy*idy
		return func(x,y)

def fourMaximum(x,y):
	if x>=0 and y>=0:
		return (np.abs(x-2.5)+np.abs(y-2.5))**0.7
	if x>=0 and y<0:
		return (np.abs(x-2.5)+np.abs(y+2.5))**0.7
	if x<0 and y>=0:
		return (np.abs(x+2.5)+np.abs(y-2.5))**0.7
	if x<0 and y<0:
		return (np.abs(x+2.5)+np.abs(y+2.5))**0.7

def moveTabu(position,value,info, tabu):

	bool1 = True
	bestValue = 0
	bestPosition = 0

	for i in [-1,1]:
		for j in [-1,1]:
			if position[0]+i>=0 and position[0]+i<info.idxmax and position[1]+j>=0 and hy*(position[1]+j)+ymin<info.ymax:
				if (position[0]+i,position[1]+j) not in tabu:
					newValue = info.getFunc(position[0]+i,position[1]+j)

					if bool1:
						bestValue = newValue
						bestPosition = (position[0]+i,position[1]+j)
						bool1 = False
					else:
						if newValue<bestValue:
							bestValue = newValue
							bestPosition = (position[0]+i,position[1]+j)
		
	if bool1:
		choixX = [-1,1]
		choixY = [-1,1]

		i = rdm.choice(choixX)
		j = rdm.choice(choixY)

		while position[0]+i<0 or position[0]+i>info.idxmax or position[1]+j<0 or position[1]+j>info.idymax:
			i = rdm.choice(choixX)
			j = rdm.choice(choixY)
		a = (position[0]+i,position[1]+j)
		return False,a,info.func(position[0]+i,position[1]+j)
	else:
		return bool1,bestPosition,bestValue



def intialiseVector(info):

	position = (int(np.floor(info.idxmax*rdm.random())),int(np.floor(info.idymax*rdm.random())))
	intensity = np.abs(func(position[0],position[1]))
	
	return position,intensity


def showPlot(info,position):
	n = 100
	R = np.zeros((n,n))
	hx = (info.xmax-info.xmin)/n
	hy = (info.ymax-info.ymin)/n

	for i in range(n):
		for j in range(n):
			R[i,j] = func(info.xmin+hx*i,info.ymin+hy*j)

	plt.figure()
	ax = plt.gca()
	l = ax.matshow(R,cmap="RdGy", origin='lower',extent=[info.xmin,xmax,ymin,info.ymax])
	plt.plot(info.xmin+info.hx*position[0],info.ymin+info.hy*position[1],"ok",markersize=10)

	print(info.xmin+info.hx*position[0],info.ymin+info.hy*position[1],info.func(info.xmin+info.hx*position[0],info.ymin+info.hy*position[1]))
	cbar = plt.colorbar(l)
	plt.show()

def showPlotTrajectory(info,tabu,bestPosition):
	n = 100
	R = np.zeros((n,n))
	hx = (info.xmax-info.xmin)/n
	hy = (info.ymax-info.ymin)/n

	for i in range(n):
		for j in range(n):
			R[i,j] = func(info.xmin+hx*i,info.ymin+hy*j)

	plt.figure(figsize=(4,4))
	ax = plt.gca()
	l = ax.matshow(R,cmap="Blues", origin='lower',extent=[info.xmin,xmax,ymin,info.ymax])
	X = [info.xmin+info.hx*tabu[i][0] for i in range(len(tabu))]
	Y = [info.xmin+info.hx*tabu[i][1] for i in range(len(tabu))]
	plt.plot(X,Y,"-",linewidth=3,color="k")
	plt.plot([X[0]],[Y[0]],"o",markersize=10,markerfacecolor="white",markeredgecolor="#FF2D19",markeredgewidth=3)
	plt.plot([X[-1]],[Y[-1]],"o",markersize=10,color="white",markeredgecolor="#AFCC14",markeredgewidth=3)
	# plt.plot(info.xmin+info.hx*bestPosition[0],info.ymin+info.hy*bestPosition[1],"o",markersize=10,color="black")
	plt.ylim([ymin,ymax])
	plt.xlim([xmin,xmax])

	# print(info.xmin+info.hx*position[0],info.ymin+info.hy*position[1],info.func(info.xmin+info.hx*position[0],info.ymin+info.hy*position[1]))
	# cbar = plt.colorbar(l)
	plt.savefig("tabusearchfunction.pdf")

	plt.show()

def show3dplot(info):
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	hx = 0.4
	hy = 0.4
	X = np.arange(info.xmin, info.xmax, hx)
	Y = np.arange(info.ymin,info.ymax, hy)
	X, Y = np.meshgrid(X, Y)
	Z = np.sin(X)
	for i in range(Z.shape[0]):
		for j in range(Z.shape[1]):
			Z[i,j] = info.func(X[i,j],Y[i,j])
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
	plt.xlim([info.xmin,info.xmax])
	plt.show()

def show3dplotTrajectory(info,tabu):
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	plt.hold(True)

	X = [info.xmin+info.hx*tabu[i][0] for i in range(len(tabu))]
	Y = [info.xmin+info.hx*tabu[i][1] for i in range(len(tabu))]
	Z = [info.func(X[i],Y[i])-0.05 for i in range(len(tabu))]
	ax.plot(X,Y,Z,linewidth=2,color="black")

	hx = 0.4
	hy = 0.4
	X = np.arange(info.xmin, info.xmax+hx, hx)
	Y = np.arange(info.ymin,info.ymax+hy, hy)
	X, Y = np.meshgrid(X, Y)
	Z = np.sin(X)
	for i in range(Z.shape[0]):
		for j in range(Z.shape[1]):
			Z[i,j] = info.func(X[i,j],Y[i,j])
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, antialiased=False,cmap=cm.coolwarm,linewidth=0,alpha=1)

	


	plt.xlim([info.xmin,info.xmax])
	ax = plt.gca()
	ax.set_zticks([])


	plt.show()

# func = lambda x,y : (np.abs(x)+np.abs(y))**0.7*np.exp(-0.05*np.abs(x))*np.exp(-0.05*np.abs(y))
#Reste coincer
func = lambda x,y : (np.sin((x**2.0+y**2.0)/2.0)/((x/5)**2.0+(y/5.0)**2.0))*-1
# func = lambda x,y : np.sin((x**2.0+y**2.0)/20.0)
# func = lambda x,y : fourMaximum(x,y)

xmin, xmax, ymin, ymax,hx,hy = -5.0,5.0,-5.0,5.0,0.05,0.05

info = Info(xmin, xmax, ymin, ymax,func,hx,hy)

tmax = 2000

position,value = intialiseVector(info)
tabu = [position]

bestValue = value
bestPosition = position

for t in range(tmax):
	bool1,position,value = moveTabu(position,value,info,tabu)
	tabu.append(position)
	if value < bestValue:
		bestValue = value
		bestPosition = position
	if bool1:
		print("break")
		break


show3dplotTrajectory(info,tabu)

