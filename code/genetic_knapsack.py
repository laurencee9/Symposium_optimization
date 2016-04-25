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
import argparse as ap

#--------------
#Parameters
#--------------
produce_data = True
nObject = len(itemValue)
populationSize = 100
nGeneration = 500
optimalFitness = np.sum(optimalGenome*itemValue)
Dir = "knapsack_data/"

#------------------------
# Get object distribution
#------------------------
def get_object_dist(p_population):
	dist = np.zeros(len(p_population[0].genome))
	for x in p_population:
		dist += x.genome
	return dist


#-------------
#Evolution
#-------------
prs = ap.ArgumentParser(description='Produce Knapsack')
prs.add_argument('--run', '-r', type=str, nargs='?',
                 help='index for the run')
args = prs.parse_args()
run = args.run

population = [Knapsack(nObject,itemValue = itemValue, itemWeight = itemWeight, 
    maxWeight = maxWeight) for i in range(populationSize)]
maxFitnessList = []
avgFitnessList = []
genomeDistList = []
for j in range(nGeneration):
    population, maxFitness, avgFitness = next_generation(population,selection_tournament)
    maxFitnessList.append(maxFitness)
    avgFitnessList.append(avgFitness)
    genomeDistList.append(get_object_dist(population))
maxFitnessList = np.array([maxFitnessList])/optimalFitness
np.savetxt(Dir+"maxFitnessList"+str(run)+".txt",maxFitnessList)
avgFitnessList = np.array([avgFitnessList])/optimalFitness
np.savetxt(Dir+"avgFitnessList"+str(run)+".txt",avgFitnessList)
np.savetxt(Dir+"genomeDistList"+str(run)+".txt", genomeDistList)


# #------------------------------
# #Show the evolution fitness
# #------------------------------
# normFitnessList = np.loadtxt(Dir+"normFitnessList.txt")
# genVec = np.arange(1,len(normFitnessList)+1)
# plt.semilogx(genVec,normFitnessList)
# plt.semilogx(genVec, [1]*len(normFitnessList), '--')
# plt.xlim([1,200])
# plt.ylim([min(normFitnessList),1.001])
# plt.xlabel(r"Génération")
# plt.ylabel(r"Adaptation normalisée")
# plt.show()


