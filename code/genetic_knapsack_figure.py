#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-
"""
Description : Script to produce figure for the data of genetic knapsack problem

Author: Guillaume St-Onge

Version 1.0

Date : 25/04/2016
"""
#--------------
#Import modules
#--------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from knapsack_data.p08_variables import *
Dir = "knapsack_data/"

plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
plt.rc('font',**{'family':'serif','serif':['Computer Modern']})
plt.rcParams['text.latex.unicode']=True
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 

# #------------------------------
# #Show the evolution of fitness
# #------------------------------
# avgAvgFitnessList = np.loadtxt(Dir+"avgAvgFitnessList.txt")
# avgMaxFitnessList = np.loadtxt(Dir+"avgMaxFitnessList.txt")
# genVec = np.arange(1,len(avgAvgFitnessList)+1)

# plt.figure(figsize=(6,4))
# plt.semilogx(genVec, avgAvgFitnessList, 
# 	linewidth=2,color="#FF7431", label = "Moyenne")
# plt.semilogx(genVec, avgMaxFitnessList, 
# 	linewidth=2,color="#2C74FF", label = "Maximale")


# leg =plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#            ncol=2, mode="expand", borderaxespad=0.,fontsize=20)
# frame = leg.get_frame()
# frame.set_facecolor('white')
# frame.set_edgecolor('none')
# for legobj in leg.legendHandles:
#     legobj.set_linewidth(8.0)

# plt.xlabel(r"Génération",fontsize=20)
# plt.ylabel("Adaptation normalisée",fontsize=20)
# plt.xlim([1,500])
# plt.savefig("knapsack_adaptation.pdf",bbox_inches="tight")
# # plt.tight_layout()
# # plt.show()


#----------------------------------------
# Animation of the genomic distribution
#----------------------------------------
def update_bars(t,data,bars):
	for i in range(len(bars)):
		j = optimalOrder[i]
		bars[i].set_height(data[t][j])

	# line.set_data(np.arange(1,25), [data[t][i] for i in optimalOrder] )
	return bars,

def interpolate(data,n):
	newData = []
	for i in range(len(data)-1):
		varData = (data[i+1]-data[i])/n
		for j in range(n):
			newData.append(data[i]+j*varData)
	return newData


# Import data
distList = np.loadtxt(Dir+"genomeDistList1.txt")

# Interpolate
distList = np.array(interpolate(distList,5))/100

# Determine optimal order for the objects
optimalOrder = [i for i in range(len(optimalGenome)) if optimalGenome[i] == 1]
for i in range(len(optimalGenome)):
	if not i in optimalOrder:
		optimalOrder.append(i)

# Fake dist		
# distList = np.array([[0.5 + np.random.normal(0,scale = 0.05) for i in range(24)]])

# Init frame
fig1 = plt.figure(figsize=(10,4))
ax = plt.gca()
bars = ax.bar(np.arange(1,25),[distList[0][i] for i in optimalOrder], 
	width = 1, color="#2C74FF", edgecolor = 'w', alpha = 0.7)
ax.set_ylim([0,1])
ax.set_xlim([1,24])
ax.get_xaxis().set_ticks([])
ax.set_ylabel("Distribution", fontsize=20)
ax.set_xlabel("Génome", fontsize=20)

plt.savefig("genome_dist.pdf",bbox_inches="tight")


# # animate
# bars_ani = animation.FuncAnimation(fig1, update_bars, len(distList), 
# 	interval=8,fargs=(distList, bars), repeat = False)
# # bars_ani.save('genome_dist.mp4') #Version Edward
# plt.show()
# bars_ani.save('genome_dist.mp4', writer = "avconv", bitrate = 1000,
# 	fps = 40, dpi = 100)