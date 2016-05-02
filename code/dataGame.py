import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import inset_axes
from scipy.stats import norm

plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
plt.rc('font',**{'family':'serif','serif':['Computer Modern']})
plt.rcParams['text.latex.unicode']=True
plt.rcParams['axes.linewidth'] = 1
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 


X = [99.2737448134/840.0, 46.2177337383/840.0, 120.045368228/840.0, 721.212527429/840.0, 143.540197661/840.0, 571.776370434/840.0, 598.126366262/840.0, 52.115941352/840.0, 42.0417736644/840.0, 538.741292385/840.0, 518.263481391/840.0, 175.365846421/840.0, 175.70652408/840.0, 509.487904781/840.0, 665.220546953/840.0, 107.843690692/840.0, 250.572810286/840.0, 348.2325276/840.0, 700.317947042/840.0, 204.30380195/840.0, 71.2228867334/840.0, 69.1649534744/840.0, 167.664070007/840.0, 704.333028349/840.0, 62.667805421/840.0, 468.002140249/840.0, 673.483206803/840.0, 27.7030413392/840.0, 676.982104859/840.0, 409.041472308/840.0, 311.060650468/840.0, 469.016219537/840.0, 760.052660047/840.0, 418.631829301/840.0, 170.458711362/840.0, 84.7865298883/840.0, 2.10817852813/840.0, 260.881608219/840.0, 721.24024426/840.0, 674.855593939/840.0]
Y = [413.89742215/520.0, 438.789689817/520.0, 384.84428207/520.0, 221.231401317/520.0, 460.034796674/520.0, 423.445591388/520.0, 363.78246882/520.0, 362.845977451/520.0, 459.012119514/520.0, 499.648279021/520.0, 256.729353652/520.0, 263.598711876/520.0, 171.529593994/520.0, 212.115976035/520.0, 408.300863372/520.0, 264.153691021/520.0, 365.890211866/520.0, 391.23662671/520.0, 139.097490435/520.0, 49.0149379327/520.0, 135.818792046/520.0, 372.189666315/520.0, 22.2073475458/520.0, 470.192164411/520.0, 303.99162489/520.0, 384.276077105/520.0, 218.485369279/520.0, 4.29410560891/520.0, 505.685655293/520.0, 393.866678316/520.0, 103.5628732/520.0, 22.9617359038/520.0, 342.742692415/520.0, 180.135332476/520.0, 70.0089350245/520.0, 39.0610218328/520.0, 7.33945030114/520.0, 228.317160901/520.0, 344.087021138/520.0, 87.929330981/520.0]

datapoints = "ipaddata.txt"
filename = "ipad_data.txt"

def getSolutions(filename):
	fileO = open(filename,"r")
	players = []

	for line in fileO:
		a = line.split("\t")
		name = a[0]
		score = float(a[1])

		order = [int(i) for i in a[2].split(",")[:-1]]
		players.append({"name":name,"score":score,"order":order})
	return players

def plotSolutions(player,X,Y,rank):

	fig = plt.figure(figsize=(5.5,5))
	XLine = [X[i] for i in player["order"]]
	YLine = [1.0-Y[i] for i in player["order"]]
	plt.plot(XLine,YLine,linewidth=8,color="#0075FF")

	plt.plot(X,[1.0-uu for uu in Y],"o",markersize=12,markerfacecolor="white",markeredgecolor="#0075FF",markeredgewidth=4)
	plt.xlim([-0.05,1.00])
	plt.ylim([-0.05,1.00])
	plt.yticks([])
	plt.xticks([])
	ax = plt.gca()
	# ax.annotate(player["name"] +" - "+"%.2f"%player["score"], xy=(0.02, 1.02), xycoords='axes fraction',fontsize=25,fontweight='bold')
	plt.savefig("../Pres_symposium/figures/airdrop_player_"+rank+".pdf",bbox_inches='tight')
	# plt.show()

def doDistribution(players):
	Ytabu = np.load("ipad_tabu_best.npy")
	YRandom = np.load("humain_random.npy")
	Yhumain = [i["score"] for i in players]

	ntabu, binstabu, patches = plt.hist(Ytabu,bins=np.arange(20,80,0.5), cumulative=True, histtype="step",normed=True)
	nhumain, binshumain, patches = plt.hist(Yhumain,bins=np.arange(20,80,0.5), cumulative=True, histtype="step",normed=True)
	nrandom, binsrandom, patches = plt.hist(YRandom,bins=np.arange(20,200,1), cumulative=True, histtype="step",normed=True)

	plt.clf()

	fig = plt.figure(figsize=(10,5))


	plt.hist(Ytabu,bins=5,normed=True, alpha=1.0,facecolor='#FF9600',edgecolor="white",label="Tabou")
	plt.hist(Yhumain,bins=5,normed=True, alpha=1.0,facecolor='#0074C0',edgecolor="white",label="Humain")
	plt.hist(YRandom,bins=20,normed=True, alpha=1.0,facecolor='gray',edgecolor="white",label=r"Al\'eatoire")


	ax = plt.gca()
	ax.set_xlabel("Distance",fontsize=25)
	ax.set_ylabel(r"Distribution",fontsize=25)
	leg =plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
	           ncol=34, mode="expand", borderaxespad=0.,fontsize=20)
	frame = leg.get_frame()
	frame.set_facecolor('white')
	frame.set_edgecolor('none')
	h=0.2
	# ax.set_yticks(np.arange(0.0,1.0+h,h))
	from mpl_toolkits.axes_grid.inset_locator import inset_axes
	inset_axes = inset_axes(ax, 
	                    width="50%", # width = 30% of parent_bbox
	                    height=2.0, # height : 1 inch
	                    loc=1)

	plt.plot(np.arange(20,80-0.5,0.5),ntabu,linewidth=3,color="#FF9600")
	plt.plot(np.arange(20,80-0.5,0.5),nhumain,linewidth=3,color="#0074C0",alpha=1.0)

	sigma = np.std(YRandom)
	mu = np.mean(YRandom)


	print(norm.cdf(np.mean(Yhumain),mu,sigma))
	plt.xlim([30,80])
	plt.ylim([-0.001,1.001])
	plt.yticks(np.arange(0.0,1.1,0.3))
	plt.ylabel("Cumulative",fontsize=20)

	plt.savefig("../Pres_symposium/figures/distribution_human.pdf",bbox_inches='tight')
	# plt.show()

# 1. Plot the three best solutions
players = getSolutions(filename)
plotSolutions(players[0],X,Y,"1")
plotSolutions(players[1],X,Y,"2")
plotSolutions(players[-1],X,Y,"3")

# #2. Take the output here for the plot
print('\\textbf{'+players[0]["name"]+"} & "+'\\textbf{'+players[1]["name"]+"} &"+'\\textbf{'+players[-1]["name"]+"}\\\\")
print("%.2f"%players[0]["score"]+"&"+"%.2f"%players[1]["score"]+"&"+"%.2f"%players[-1]["score"]+"\\\\")

#3. Do a distribution
doDistribution(players)



