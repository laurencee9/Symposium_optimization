#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-
"""
Description : Framework (Class and functions) for the implementation of 
              genetic algorithms.

Author: Guillaume St-Onge

Version 1.0

Date : 22/04/2016
"""
#--------------
#Import modules
#--------------
import numpy as np
from abc import ABCMeta
from abc import abstractmethod
from random import randint
from numpy.random import random
from numpy.random import shuffle
from numpy.random import choice
from copy import deepcopy

#-----------------
# Individual class
#-----------------

class Knapsack(object):
    """Class to identify the individual from a population with
       their genome, fitness, merging and mutating properties.  """

    def __init__(self, *args, **kwargs):
        self.genome = kwargs.get('genome', None)
        if self.genome == None:
            self.genome = np.array([randint(0,1) for i in range(args[0])])
        self.itemValue = kwargs.get('itemValue')
        self.itemWeight = kwargs.get('itemWeight')
        self.maxWeight = kwargs.get('maxWeight')
        self.fitness = self.evaluate_fitness()

    def evaluate_fitness(self):
        if np.sum(self.itemWeight*self.genome) > self.maxWeight:
            fitness = 0
        else:
            fitness = np.sum(self.itemValue*self.genome)
        return fitness

    def change_genome(self,p_genome):
        self.genome = p_genome
        self.fitness = self.evaluate_fitness()

    def merge(self,p_Knapsack):
        newGenome = deepcopy(self.genome)
        allele = randint(0,len(newGenome)-1) # determine the crossover
        for i in range(allele,len(newGenome)):
            newGenome[i] = p_Knapsack.genome[i]
        newKnapsack = deepcopy(self)
        newKnapsack.change_genome(newGenome)
        return newKnapsack

    def mutate(self):
        allele = randint(0,len(self.genome)-1)
        if self.genome[allele] == 1:
            self.genome[allele] = 0
        else:
            self.genome[allele] = 1
        self.fitness = self.evaluate_fitness()

class Salesman_path(object):
    """Class to identify the individual from a population with
       their genome, fitness, merging and mutating properties.  """

    def __init__(self, *args, **kwargs):
        self.genome = kwargs.get('genome', None)
        if self.genome == None:
            self.genome = np.arange(0,args[0])
            shuffle(self.genome)
        self.distanceDict = kwargs.get('distance')
        self.fitness = self.evaluate_fitness()

    def evaluate_fitness(self):
        totalDist = 0.
        for i in range(len(self.genome)-1):
            if self.genome[i] < self.genome[i+1]:
                totalDist += self.distanceDict[(self.genome[i],
                    self.genome[i+1])]
            else:
                totalDist += self.distanceDict[(self.genome[i+1],
                    self.genome[i])]
        fitness = 1/totalDist**2
        return fitness

    def change_genome(self,p_genome):
        self.genome = p_genome
        self.fitness = self.evaluate_fitness()

    def merge(self,p_path):
        allele = randint(0,len(self.genome)-1) # determine the crossover
        newGenome = list(self.genome[0:allele])
        for i in range(len(p_path.genome)):
            if not p_path.genome[i] in newGenome:
                newGenome.append(p_path.genome[i])
        newPath = deepcopy(self)
        newPath.change_genome(newGenome)
        return newPath

    def mutate(self):
        #swap a pair
        pair = choice(np.arange(0,len(self.genome)),2,replace = False)
        temp = self.genome[pair[0]]*1
        self.genome[pair[0]] = self.genome[pair[1]]
        self.genome[pair[1]] = temp
        self.fitness = self.evaluate_fitness()

#----------------------------
# Genetic algorithm functions
#----------------------------
def selection_proportional(p_fitnessList, p_numberOfCouples):
    normFitnessList = p_fitnessList/np.sum(p_fitnessList)
    #We select couple
    N = len(normFitnessList)
    coupleList = []
    for i in range(p_numberOfCouples):
        couple = choice(np.arange(0,N),2,replace=False,p=normFitnessList)
        coupleList.append(couple)
    return coupleList

def next_generation(p_population, p_selection_method, p_elitism = True, 
    p_mergeProbability = 0.7, p_mutateProbability = 0.5):
    N = len(p_population)
    fitnessList = np.array([x.fitness for x in p_population])
    newPopulation = []
    coupleList = p_selection_method(fitnessList, N//2)
    # Breeding
    for couple in coupleList:
        male = p_population[couple[0]]
        female = p_population[couple[1]]
        if p_mergeProbability > random():
            newPopulation.append(male.merge(female))
            newPopulation.append(female.merge(male))
        else:
            newPopulation.append(deepcopy(male))
            newPopulation.append(deepcopy(female))
    # Mutation events
    for x in newPopulation:
        if p_mutateProbability > random():
            x.mutate()
    # Elitisme
    if p_elitism:
        newPopulation.remove(newPopulation[randint(0,N-1)])
        newPopulation.append(deepcopy(p_population[np.argmax(fitnessList)]))
    return newPopulation, np.max(fitnessList)

def get_mostAdapted(p_population):
    fitnessList = np.array([x.fitness for x in p_population])
    return p_population[np.argmax(fitnessList)]


if __name__ == '__main__':
    from knapsack_dataset.p01_variables import *
    nObject = len(itemValue)
    populationSize = 500
    nGeneration = 100
    population = [Knapsack(nObject,itemValue = itemValue, itemWeight = itemWeight, 
        maxWeight = maxWeight) for i in range(populationSize)]
    maxFitnessList = []
    for j in range(nGeneration):
        population, maxFitness = next_generation(population,selection_proportional)
        maxFitnessList.append(maxFitness)

    print("genetic solution fitness : ", maxFitnessList[-1])
    print("optimal solution fitness : ", np.sum(optimalGenome*itemValue))
