"""

PLot distirbution

"""

import numpy as np
import random as rdm
import matplotlib.pyplot as plt



from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
plt.rc('font',**{'family':'serif','serif':['Computer Modern']})
plt.rcParams['text.latex.unicode']=True
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 





Ytabu = np.load("N_20_tabu_best.npy")
Yfirefly = np.load("N_20_firefly_best.npy")


plt.figure(figsize=(7,4))
plt.hist(Ytabu,bins=range(20,80,2),normed=True,alpha=1.0,facecolor="#FF9600",edgecolor="white",label="Tabou")
plt.hist(Yfirefly,bins=range(20,80,2),normed=True,alpha=0.5,facecolor='#0074C0',edgecolor="white",label="Lucioles")

plt.xlabel("Distance",fontsize=25)
plt.ylabel(r"Distribution",fontsize=25)
leg = plt.legend(loc=1,fontsize=20)
frame = leg.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('none')
h=0.05
plt.yticks(np.arange(0.0,0.2+h,h))

plt.savefig("distri_distance.pdf",bbox_inches="tight")
plt.show()


#CUMULATIVE
# YTabuSorted = sorted(YTabuSorted)
# YfireflyCumu = [np.sum(Yfirefly[:i]) for i in range(len(Yfirefly))]
# plt.figure(figsize=(7,4))
# plt.plot(YtabuCumu)
# plt.plot(Yfirefly)
# plt.hist(Ytabu,bins=range(20,80,2),normed=True,alpha=1.0,facecolor="#FF9600",edgecolor="white",label="Tabou")
# plt.hist(Yfirefly,bins=range(20,80,2),normed=True,alpha=0.5,facecolor='#0074C0',edgecolor="white",label="Lucioles")

# plt.xlabel("Distance",fontsize=25)
# plt.ylabel(r"Distribution",fontsize=25)
# # leg = plt.legend(loc=1,fontsize=20)
# # frame = leg.get_frame()
# # frame.set_facecolor('white')
# # frame.set_edgecolor('none')
# plt.show()





