#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-
"""
Description : Script for the Knapsack problem using genetic algorithm

Author: Guillaume St-Onge

Version 1.0

Date : 23/04/2016
"""
#-----------------------
#Import modules and data
#-----------------------
import numpy as np
from genetic_framework import *
import matplotlib.pyplot as plt
from knapsack_data.p08_variables import *

#--------------
#Parameters
#--------------
produce_data = False
nObject = len(itemValue)
populationSize = 500
nGeneration = 200
optimalFitness = np.sum(optimalGenome*itemValue)
Dir = "knapsack_data/p08"

#-------------
#Evolution
#-------------
if produce_data:
	population = [Knapsack(nObject,itemValue = itemValue, itemWeight = itemWeight, 
	    maxWeight = maxWeight) for i in range(populationSize)]
	maxFitnessList = []
	for j in range(nGeneration):
	    population, maxFitness = next_generation(population,selection_tournament)
	    maxFitnessList.append(maxFitness)
	print("genetic solution fitness : ", maxFitnessList[-1])
	print("optimal solution fitness : ", optimalFitness)
	normFitnessList = np.array([maxFitnessList])/optimalFitness
	np.savetxt(Dir+"normFitnessList.txt",normFitnessList)

#------------------------------
#Show the evolution fitness
#------------------------------
normFitnessList = np.loadtxt(Dir+"normFitnessList.txt")
genVec = np.arange(1,len(normFitnessList)+1)
plt.semilogx(genVec,normFitnessList)
plt.semilogx(genVec, [1]*len(normFitnessList), '--')
plt.xlim([1,200])
plt.ylim([min(normFitnessList),1.001])
plt.xlabel(r"Génération")
plt.ylabel(r"Adaptation normalisée")
plt.show()


