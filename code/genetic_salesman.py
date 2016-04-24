#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-
"""
Description : Script for the Salesman problem using genetic algorithm

Author: Guillaume St-Onge

Version 1.0

Date : 23/04/2016
"""
#-----------------------
#Import modules and data
#-----------------------
import numpy as np
from genetic_framework import *
from generateMap import *
distanceDict = loadDist("geometricDistance.txt")
position = np.loadtxt("geometricPosition.txt")

#--------------
#Parameters
#--------------
produce_data = False
nStop = len(position)
populationSize = 500
nGeneration = 1000
Dir = "salesman_data/"

#----------------------------------
#Evolution - evaluate shortest path
#----------------------------------
if produce_data:
	population = [Salesman_path(nStop,distance=distanceDict) for i in range(populationSize)]
	maxFitnessList = []
	for j in range(nGeneration):
	    population, maxFitness = next_generation(population,selection_tournament)
	    maxFitnessList.append(maxFitness)
	pathDistanceList = 1./np.array(maxFitnessList)
	print("genetic solution shortest path : ", pathDistanceList[-1])
	shortestPath = get_mostAdapted(population).genome
	np.savetxt(Dir+"shortestPath.txt",shortestPath)
	np.savetxt(Dir+"pathDistanceList.txt",pathDistanceList)

#------------------------------
#Show the evolution of distance
#------------------------------
pathDistanceList = np.loadtxt(Dir+"pathDistanceList.txt")
genVec = np.arange(1,len(pathDistanceList)+1)
plt.semilogx(genVec,pathDistanceList)
plt.xlim([1,200])
plt.xlabel(r"Génération")
plt.ylabel(r"Distance minimale")
plt.show()


#----------------------
#Show the shortest path
#----------------------
shortestPath = np.loadtxt(Dir+"shortestPath.txt")
xVec = [position[i][0] for i in shortestPath]
yVec = [position[i][1] for i in shortestPath]
plt.plot(xVec,yVec, '-')
showPoints(position)

