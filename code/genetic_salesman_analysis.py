#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-
"""
Description : Analyse the distance / shortest path for the salesman
			  problem. 

Author: Guillaume St-Onge

Version 1.0

Date : 25/04/2016
"""
#----------------
#Import Modules 
#----------------
import numpy as np
import matplotlib.pyplot as plt
from os import listdir

#----------------
#Analyse data set
#----------------
Dir = "salesman_data/"
distanceArray = []
shortestShortestPathRun = 0
shortestShortestPath = 100.
minDistanceDist = []
for run in np.arange(1,101):
	distanceList = np.loadtxt(Dir+"distanceList"+str(run)+".txt")
	minDistanceDist.append(distanceList[-1])
	distanceArray.append(distanceList)
	if distanceList[-1] < shortestShortestPath:
		shortestShortestPath = distanceList[-1]
		shortestShortestPathRun = run
distanceArray = np.array(distanceArray).T
avgDistanceList = np.array([np.mean(distanceSlice) for distanceSlice in distanceArray])
stdDistanceList = np.array([np.std(distanceSlice) for distanceSlice in distanceArray])
np.savetxt("to_edward/avgDistanceList.txt",avgDistanceList)
np.savetxt("to_edward/stdDistanceList.txt",stdDistanceList)
np.savetxt("to_edward/minDistanceDist.txt",minDistanceDist)


#------------------------------
#Show the evolution of distance
#------------------------------
genVec = np.arange(1,len(avgDistanceList)+1)
plt.semilogx(genVec,avgDistanceList)
plt.xlim([1,500])
plt.xlabel(r"Génération")
plt.ylabel(r"Distance minimale")
plt.show()


#-------------------------------
#Show the shortest shortest path
#-------------------------------
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
	plt.savefig("to_edward/salesman_genetic_n20.pdf",bbox_inches='tight')
	plt.show()

shortestPath = np.loadtxt(Dir+"shortestPath"+str(shortestShortestPathRun)+".txt")
position = np.load("salesman/geometricPosition_20.txt.npy")
showPoints(position,shortestPath)