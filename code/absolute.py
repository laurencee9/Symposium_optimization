#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-
"""
Description : Plot the absolute value function

Author: Guillaume St-Onge

Version 1.0

Date : 24/06/2016
"""
#--------------
#Import modules
#--------------
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
plt.rc('font',**{'family':'serif','serif':['Computer Modern']})
plt.rcParams['text.latex.unicode']=True
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 


plt.figure(figsize=(6,4))
x = np.linspace(-1,1, 10000)
plt.plot(x,np.abs(x), linewidth=2,color="#FF7431")

plt.xlabel(r"$x$",fontsize=20)
plt.ylabel(r"$|x|$",fontsize=20)
plt.xlim([-1,1])
plt.savefig("absolute_function.pdf",bbox_inches="tight")
# plt.tight_layout()
# plt.show()