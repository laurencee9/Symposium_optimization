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
nStop = len(position)
populationSize = 200
nGeneration = 100

#----------------------------------
#Evolution - evaluate shortest path
#----------------------------------
# population = [Salesman_path(nStop,distance=distanceDict) for i in range(populationSize)]
# maxFitnessList = []
# for j in range(nGeneration):
#     population, maxFitness = next_generation(population,selection_proportional)
#     maxFitnessList.append(maxFitness)
# print("genetic solution fitness : ", maxFitnessList[-1])
# shortestPath = get_mostAdapted(population).genome
# np.savetxt("shortestPath.txt",shortestPath)

#------------------
#Show the path
#------------------
shortestPath = np.loadtxt("shortestPath.txt")
xVec = [position[i][0] for i in shortestPath]
yVec = [position[i][1] for i in shortestPath]
plt.plot(xVec,yVec, '-')
showPoints(position)

