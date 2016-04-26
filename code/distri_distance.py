"""

PLot distirbution

"""
import pylab as P
import numpy as np
import random as rdm
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import inset_axes
from scipy.stats import norm

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
YGene = np.loadtxt("./guillaume/minDistanceDist.txt")
# print(YGene)
YRandom = np.load("N_20_random_best.npy")
meanTabu = np.mean(Ytabu)
meanFirefly = np.mean(Yfirefly)
meanRandom = np.mean(YRandom)


ntabu, binstabu, patches = plt.hist(Ytabu,bins=range(20,80,2), cumulative=True, histtype="step",normed=True)
nfire, binsfire, patches = plt.hist(Yfirefly,bins=range(20,80,2), cumulative=True, histtype="step",normed=True)
ngene, binsgene, patches = plt.hist(YGene,bins=range(20,80,2), cumulative=True, histtype="step",normed=True)

plt.clf()

fig = plt.figure(figsize=(10,5))
plt.hist(Ytabu,bins=range(20,80,2),normed=True,alpha=1.0,facecolor="#FF9600",edgecolor="white",label="Tabou")
plt.hist(Yfirefly,bins=range(20,80,2),normed=True,alpha=0.5,facecolor='#0074C0',edgecolor="white",label="Lucioles")
plt.hist(YGene,bins=range(20,80,2),normed=True,alpha=0.5,facecolor='green',edgecolor="white",label=r"G\'en\'etique")
n,bins,sigma = plt.hist(YRandom,bins=range(80,140,2),normed=True,alpha=0.6,facecolor='black',edgecolor="white",label=r"Al\'eatoire")
# print(YRandom)
sigma = np.std(YRandom)
mu = np.mean(YRandom)


print(norm.cdf(np.min(Ytabu),mu,sigma))
print(norm.cdf(np.min(Yfirefly),mu,sigma))
print(norm.cdf(np.min(YGene),mu,sigma))
# print(mu,sigma)
y = P.normpdf( bins, mu, sigma)
l = P.plot(bins, y, 'k--', linewidth=1.5)


ax = plt.gca()

ax.set_xlabel("Distance",fontsize=25)
ax.set_ylabel(r"Distribution",fontsize=25)
leg =plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=34, mode="expand", borderaxespad=0.,fontsize=20)
frame = leg.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('none')
h=0.05
ax.set_yticks(np.arange(0.0,0.2+h,h))

inset_axes = inset_axes(ax, 
                    width="50%", # width = 30% of parent_bbox
                    height=2.0, # height : 1 inch
                    loc=1)


plt.plot(range(20,78,2),ntabu,linewidth=3,color="#FF9600")
plt.plot(range(20,78,2),nfire,linewidth=3,color="#0074C0",alpha=0.5)
plt.plot(range(20,78,2),ngene,linewidth=3,color="green",alpha=0.5)
plt.xlim([30,50])
plt.ylim([-0.001,1.001])
plt.yticks(np.arange(0.0,1.1,0.3))
plt.ylabel("Cumulative",fontsize=20)
#line
# ax = plt.gca()
# plt.plot([meanTabu,meanTabu],ax.get_ylim(),"--k",linewidth=2)
# plt.plot([meanFirefly,meanFirefly],ax.get_ylim(),"--k",linewidth=2)
# ax.annotate(r'$\langle \text{tabou}\rangle$', xy=(meanTabu-2,ax.get_ylim()[1]*1.2), annotation_clip=False, xycoords='data',fontsize=20,rotation=60)
# ax.annotate(r'$\langle \text{lucioles}\rangle$', xy=(meanFirefly-2,ax.get_ylim()[1]*1.24), annotation_clip=False, xycoords='data',fontsize=20,rotation=60)

# plt.savefig("distri_distance22.pdf",bbox_inches="tight")
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





