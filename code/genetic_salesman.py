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


#--------------
#Parameters
#--------------

populationSize = 500
nGeneration = 100

#-------------
#Evolution
#-------------
population = [Knapsack(nObject,itemValue = itemValue, itemWeight = itemWeight, 
    maxWeight = maxWeight) for i in range(populationSize)]
maxFitnessList = []
for j in range(nGeneration):
    population, maxFitness = next_generation(population,selection_proportional)
    maxFitnessList.append(maxFitness)

print("genetic solution fitness : ", maxFitnessList[-1])
print("optimal solution fitness : ", np.sum(optimalGenome*itemValue))