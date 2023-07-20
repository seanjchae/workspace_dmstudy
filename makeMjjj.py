import numpy as np
import awkward as ak
import vector
from itertools import combinations
import tqdm

def npyLoader(file):
	out = np.load(file,allow_pickle=True)[()]
	return out

def chisqCalculator(comb,nPart,mass,rate):
	khi = []
	for j in range(len(comb)):
		v1=comb[j][0]
		v2=comb[j][1]
		v3=comb[-1-j][0]
		v4=comb[-1-j][1]
		M1=(v1+v2).mass
		M2=(v3+v4).mass
		mw=mass
		G=rate
		khi.append(((M1-mw)**2/G + (M2-mw)**2/G)/2)

		if j > (nPart*(nPart-1)/2) -1:
			break

	for k in range(len(khi)):
		if khi[k] == min(khi):
			v1 = comb[k][0]+comb[k][1]
			v2 = comb[-1-k][0]+comb[-1-k][1]
	return v1, v2



### Definition of Input files
flist = ["./step1DM_MY900_nTuple.npy",
"./step1DM_MY800_nTuple.npy",
"./step1DM_MY700_nTuple.npy",
"./step1DM_MY600_nTuple.npy",
"./step1DM_MY500_nTuple.npy",
"./step1DM_MY400_nTuple.npy",
"./step1DM_MY300_nTuple.npy",
"./step1DM_MY200_nTuple.npy"
]



for f in flist:
	print("now running", f)
	Inst = npyLoader(f)
	cut = ak.num(Inst['normalJet_PT']) > 3
	#cut2= Inst['MET_PT'] > 50
	for key in Inst.keys():
		Inst[key] = Inst[key][cut]
	#for key in Inst.keys():
		#Inst[key]=Inst[key][cut2]
	njpt = Inst['normalJet_PT']
	njeta = Inst['normalJet_Eta']
	njphi = Inst['normalJet_Phi']
	njmass=Inst['normalJet_Mass']
	bjpt=Inst['BJet_PT']
	bjeta=Inst['BJet_Eta']
	bjphi=Inst['BJet_Phi']
	bjmass=Inst['BJet_Mass']

	Mjjj = []
	
	
	### Eventloop
	for idx in range(len(njpt)):
		
		cand = []
		for j in range(len(njpt[idx])):
			cand.append(vector.obj(pt=njpt[idx,j],phi=njphi[idx,j],eta=njeta[idx,j],mass=njmass[idx,j]))
		comb=list(combinations(cand,2))
		nPart = len(njpt[idx])
		
		v1,v2 = chisqCalculator(comb,nPart,80.379,7)
		b0 = vector.obj(pt=bjpt[idx,0],phi=bjphi[idx,0],eta=bjeta[idx,0],mass=bjmass[idx,0])
		b1 = vector.obj(pt=bjpt[idx,1],phi=bjphi[idx,1],eta=bjeta[idx,1],mass=bjmass[idx,1])
		cand = [b0,b1,v1,v2]
		comb=list(combinations(cand,2))
		nPart = len(cand)
		t1,t2 = chisqCalculator(comb,nPart,172.76,10)
	
		m1 = np.array(t1.mass)
		m2 = np.array(t2.mass)
		Mjjj.append([m1,m2])
		if idx % 1000 == 0:
			print("now ", idx,"th events")
	Inst['Mjjj'] = np.array(Mjjj)

	np.save("./step3/"+f+"_nTuple", Inst)
