import numpy as np
import matplotlib.pyplot as plt



plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
plt.rc('font',**{'family':'serif','serif':['Computer Modern']})
plt.rcParams['text.latex.unicode']=True
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 


YTabu = np.loadtxt("./N_20_distance")
YFire = np.loadtxt("N_20_time_firefly")
YGene = np.loadtxt("./guillaume/avgDistanceList.txt")

plt.figure(figsize=(6,4))

plt.plot(YTabu,label="Tabou",linewidth=2,color="#FF7431")
plt.plot(YFire,label="Lucioles",linewidth=2,color="black")
plt.plot(YGene,label=r"G\'en\'etique",linewidth=2,color="#2C74FF")
plt.xscale("log")

leg =plt.legend(loc=1,fontsize=20)
frame = leg.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('none')
for legobj in leg.legendHandles:
    legobj.set_linewidth(8.0)

plt.xlabel(r"temps",fontsize=20)
plt.ylabel("Distance moyenne",fontsize=20)
plt.yticks(range(30,120,20))
plt.savefig("speedtest.pdf",bbox_inches="tight")
# plt.show()