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
import argparse as ap
distanceDict = loadDist("salesman/geometricDistance_20.txt")
position = np.load("salesman/geometricPosition_20.txt.npy")

#----------------
#Fixed parameters
#----------------
nStop = len(position)
populationSize = 50
nGeneration = 500
Dir = "salesman_data/"

#----------------------------------
#Evolution - evaluate shortest path
#----------------------------------
prs = ap.ArgumentParser(description='Produce shortest path')
prs.add_argument('--run', '-r', type=str, nargs='?',
                 help='index for the run')
args = prs.parse_args()

population = [Salesman_path(nStop,distance=distanceDict) for i in range(populationSize)]
maxFitnessList = []
for j in range(nGeneration):
    population, maxFitness, avgFitness = next_generation(population,selection_tournament)
    maxFitnessList.append(maxFitness)
pathDistanceList = 1./np.array(maxFitnessList)
print("genetic solution shortest path : ", pathDistanceList[-1])
shortestPath = get_mostAdapted(population).genome
np.savetxt(Dir+"shortestPath"+args.run+".txt",shortestPath)
np.savetxt(Dir+"distanceList"+args.run+".txt",pathDistanceList)

# #------------------------------
# #Show the evolution of distance
# #------------------------------
# pathDistanceList = np.loadtxt(Dir+"distanceList1.txt")
# genVec = np.arange(1,len(pathDistanceList)+1)
# plt.semilogx(genVec,pathDistanceList)
# plt.xlim([1,200])
# plt.xlabel(r"Génération")
# plt.ylabel(r"Distance minimale")
# plt.show()


# #----------------------
# #Show the shortest path
# #----------------------
# shortestPath = np.loadtxt(Dir+"shortestPath.txt")
# xVec = [position[i][0] for i in shortestPath]
# yVec = [position[i][1] for i in shortestPath]
# plt.plot(xVec,yVec, '-')
# showPoints(position)

