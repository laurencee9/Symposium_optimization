#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-
"""
Description : Analyse the fitness for the Knapsack problem. 

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
Dir = "knapsack_data/"
#For maxFitness
maxFitnessArray = []
for run in np.arange(1,501):
	maxFitnessList = np.loadtxt(Dir+"maxFitnessList"+str(run)+".txt")
	maxFitnessArray.append(maxFitnessList)
maxFitnessArray = np.array(maxFitnessArray).T
avgMaxFitnessList = np.array([np.mean(fitnessSlice) for fitnessSlice in maxFitnessArray])
stdMaxFitnessList = np.array([np.std(fitnessSlice) for fitnessSlice in maxFitnessArray])
np.savetxt(Dir+"avgMaxFitnessList.txt",avgMaxFitnessList)
np.savetxt(Dir+"stdMaxFitnessList.txt",stdMaxFitnessList)
#For meanFitness
avgFitnessArray = []
for run in np.arange(1,501):
	avgFitnessList = np.loadtxt(Dir+"avgFitnessList"+str(run)+".txt")
	avgFitnessArray.append(avgFitnessList)
avgFitnessArray = np.array(avgFitnessArray).T
avgAvgFitnessList = np.array([np.mean(fitnessSlice) for fitnessSlice in avgFitnessArray])
stdAvgFitnessList = np.array([np.std(fitnessSlice) for fitnessSlice in avgFitnessArray])
np.savetxt(Dir+"avgAvgFitnessList.txt",avgAvgFitnessList)
np.savetxt(Dir+"stdAvgFitnessList.txt",stdAvgFitnessList)
#For genome distribution
avgGenomeDistList = np.zeros((500,24))
for run in np.arange(1,501):
	avgGenomeDistList += np.loadtxt(Dir+"genomeDistList"+str(run)+".txt")
avgGenomeDistList /= 500
np.savetxt(Dir+"avgGenomeDistList.txt",avgGenomeDistList)

#------------------------------
#Show the evolution of fitness
#------------------------------
avgAvgFitnessList = np.loadtxt(Dir+"avgAvgFitnessList.txt")
avgMaxFitnessList = np.loadtxt(Dir+"avgMaxFitnessList.txt")
genVec = np.arange(1,len(avgAvgFitnessList)+1)
plt.semilogx(genVec, avgAvgFitnessList, lw = 3.)
plt.semilogx(genVec, avgMaxFitnessList, lw = 3.)
plt.xlim([1,500])
plt.xlabel(r"Génération")
plt.ylabel(r"Adaptation")
plt.show()
