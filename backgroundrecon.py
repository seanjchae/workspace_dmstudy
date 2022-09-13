import numpy as np
import awkward as ak
import vector
from itertools import combinations
import matplotlib.pyplot as plt
import mplhep as hep

f="./FH_2_nTuple.npy"
#f="1l_2_nTuple.npy"
#f="TTW_nTuple.npy"
#f="TTZ_nTuple.npy"
#f="./WW_nTuple.npy"
#f="./WZ_nTuple.npy"
#f="./ZZ_nTuple.npy"

njpt=np.load(f,allow_pickle=True)[()]['normalJet_PT']
njeta=np.load(f,allow_pickle=True)[()]['normalJet_Eta']
njphi=np.load(f,allow_pickle=True)[()]['normalJet_Phi']
njmass=np.load(f,allow_pickle=True)[()]['normalJet_Mass']
bjpt=np.load(f,allow_pickle=True)[()]['BJet_PT']
bjeta=np.load(f,allow_pickle=True)[()]['BJet_Eta']
bjphi=np.load(f,allow_pickle=True)[()]['BJet_Phi']
bjmass=np.load(f,allow_pickle=True)[()]['BJet_Mass']

'''
njpt=ak.flatten(normalJet_PT)
bjpt=ak.flatten(BJet_PT)

plt.hist(njpt,range=(0,100),bins=100,histtype='step',color='blue')
plt.hist(bjpt,range=(0,100),bins=100,histtype='step',color='red')
plt.legend()
plt.show()
'''

vec_w1=[]
vec_w2=[]


for i in range(len(njpt)):
	if len(njpt[i]) ==4:
		q0=vector.obj(pt=njpt[i,0],phi=njphi[i,0],eta=njeta[i,0],mass=njmass[i,0])
		q1=vector.obj(pt=njpt[i,1],phi=njphi[i,1],eta=njeta[i,1],mass=njmass[i,1])
		q2=vector.obj(pt=njpt[i,2],phi=njphi[i,2],eta=njeta[i,2],mass=njmass[i,2]) 
		q3=vector.obj(pt=njpt[i,3],phi=njphi[i,3],eta=njeta[i,3],mass=njmass[i,3])

		cand=[q0,q1,q2,q3]

		comb=list(combinations(cand,2))

		temp=0
		khi=[]

		for j in range(len(comb)):
			v1=comb[j][0]
			v2=comb[j][1]
			v3=comb[-1-j][0]
			v4=comb[-1-j][1]
			M1=(v1+v2).mass
			M2=(v3+v4).mass
			mw=80.379
			G=7
			khi.append(((M1-mw)**2/G + (M2-mw)**2/G)/2)
			temp=temp+1

			if j >2:
				break

		for k in range(temp):
			if khi[k] ==min(khi):
				vec_w1.append(comb[k][0]+comb[k][1])
				vec_w2.append(comb[-1-k][0]+comb[-1-k][1])
		#if i%10000==0:
			#print(i)	
	
	elif len(njpt[i]) ==5:
		q0=vector.obj(pt=njpt[i,0],phi=njphi[i,0],eta=njeta[i,0],mass=njmass[i,0])
		q1=vector.obj(pt=njpt[i,1],phi=njphi[i,1],eta=njeta[i,1],mass=njmass[i,1])
		q2=vector.obj(pt=njpt[i,2],phi=njphi[i,2],eta=njeta[i,2],mass=njmass[i,2])
		q3=vector.obj(pt=njpt[i,3],phi=njphi[i,3],eta=njeta[i,3],mass=njmass[i,3])
		q4=vector.obj(pt=njpt[i,4],phi=njphi[i,4],eta=njeta[i,4],mass=njmass[i,4])
		
		cand=[q0,q1,q2,q3,q4]

		comb=list(combinations(cand,2))
		
		temp=0
		khi=[]

		for j in range(len(comb)):
			v1=comb[j][0]
			v2=comb[j][1]
			v3=comb[-1-j][0]
			v4=comb[-1-j][1]
			M1=(v1+v2).mass
			M2=(v3+v4).mass
			mw=80.379
			G=7
			khi.append(((M1-mw)**2/G + (M2-mw)**2/G)/2)
			temp=temp+1

			if j > 5:
				break

		for k in range(temp):
			if khi[k] == min(khi):
				vec_w1.append(comb[k][0]+comb[k][1])
				vec_w2.append(comb[-1-k][0]+comb[-1-k][1])
		
	elif len(njpt[i]) ==6 :
		q0=vector.obj(pt=njpt[i,0],phi=njphi[i,0],eta=njeta[i,0],mass=njmass[i,0])
		q1=vector.obj(pt=njpt[i,1],phi=njphi[i,1],eta=njeta[i,1],mass=njmass[i,1])
		q2=vector.obj(pt=njpt[i,2],phi=njphi[i,2],eta=njeta[i,2],mass=njmass[i,2])
		q3=vector.obj(pt=njpt[i,3],phi=njphi[i,3],eta=njeta[i,3],mass=njmass[i,3])
		q4=vector.obj(pt=njpt[i,4],phi=njphi[i,4],eta=njeta[i,4],mass=njmass[i,4])
		q5=vector.obj(pt=njpt[i,5],phi=njphi[i,5],eta=njeta[i,5],mass=njmass[i,5])

		cand=[q0,q1,q2,q3,q4,q5]
		
		comb=list(combinations(cand,2))
	
		temp=0
		khi=[]

		for j in range(len(comb)):
			v1=comb[j][0]
			v2=comb[j][1]
			v3=comb[-1-j][0]
			v4=comb[-1-j][1]
			M1=(v1+v2).mass
			M2=(v3+v4).mass
			mw=80.379
			G=7
			khi.append(((M1-mw)**2/G + (M2-mw)**2/G)/2)
			temp=temp+1

			if j > 8:
				break

		for k in range(temp):
			if khi[k] ==min(khi):
				vec_w1.append(comb[k][0]+comb[k][1])
				vec_w2.append(comb[-1-k][0]+comb[-1-k][1])

	elif len(njpt[i]) ==7:
		q0=vector.obj(pt=njpt[i,0],phi=njphi[i,0],eta=njeta[i,0],mass=njmass[i,0])
		q1=vector.obj(pt=njpt[i,1],phi=njphi[i,1],eta=njeta[i,1],mass=njmass[i,1])
		q2=vector.obj(pt=njpt[i,2],phi=njphi[i,2],eta=njeta[i,2],mass=njmass[i,2])
		q3=vector.obj(pt=njpt[i,3],phi=njphi[i,3],eta=njeta[i,3],mass=njmass[i,3])
		q4=vector.obj(pt=njpt[i,4],phi=njphi[i,4],eta=njeta[i,4],mass=njmass[i,4])
		q5=vector.obj(pt=njpt[i,5],phi=njphi[i,5],eta=njeta[i,5],mass=njmass[i,5])
		q6=vector.obj(pt=njpt[i,6],phi=njphi[i,6],eta=njeta[i,6],mass=njmass[i,6])

		cand=[q0,q1,q2,q3,q4,q5,q6]
		
		comb=list(combinations(cand,2))
		
		temp=0
		khi=[]

		for j in range(len(comb)):
			v1=comb[j][0]
			v2=comb[j][1]
			v3=comb[-1-j][0]	
			v4=comb[-1-j][1]
			M1=(v1+v2).mass
			M2=(v3+v4).mass
			mw=80.379
			G=7
			khi.append(((M1-mw)**2/G + (M2-mw)**2/G)/2)
			temp=temp+1
	
			if j > 10:	
				break

		for k in range(temp):
			if khi[k] ==min(khi):
				vec_w1.append(comb[k][0]+comb[k][1])
				vec_w2.append(comb[-1-k][0]+comb[-1-k][1])

	elif len(njpt[i]) ==8:
		q0=vector.obj(pt=njpt[i,0],phi=njphi[i,0],eta=njeta[i,0],mass=njmass[i,0])
		q1=vector.obj(pt=njpt[i,1],phi=njphi[i,1],eta=njeta[i,1],mass=njmass[i,1])
		q2=vector.obj(pt=njpt[i,2],phi=njphi[i,2],eta=njeta[i,2],mass=njmass[i,2])
		q3=vector.obj(pt=njpt[i,3],phi=njphi[i,3],eta=njeta[i,3],mass=njmass[i,3])
		q4=vector.obj(pt=njpt[i,4],phi=njphi[i,4],eta=njeta[i,4],mass=njmass[i,4])
		q5=vector.obj(pt=njpt[i,5],phi=njphi[i,5],eta=njeta[i,5],mass=njmass[i,5])
		q6=vector.obj(pt=njpt[i,6],phi=njphi[i,6],eta=njeta[i,6],mass=njmass[i,6])
		q7=vector.obj(pt=njpt[i,7],phi=njphi[i,7],eta=njeta[i,7],mass=njmass[i,7])

		cand=[q0,q1,q2,q3,q4,q5,q6,q7]

		comb=list(combinations(cand,2))
		
		temp=0
		khi=[]
		
		for j in range(len(comb)):
			v1=comb[j][0]
			v2=comb[j][1]
			v3=comb[-1-j][0]
			v4=comb[-1-j][1]
			M1=(v1+v2).mass
			M2=(v3+v4).mass
			mw=80.379
			G=7
			khi.append(((M1-mw)**2/G + (M2-mw)**2/G)/2)
			temp=temp+1

			if j > 14:
				break

		for k in range(temp):
			if khi[k] ==min(khi):
				vec_w1.append(comb[k][0]+comb[k][1])
				vec_w2.append(comb[-1-k][0]+comb[-1-k][1])
			
m1=[]
m2=[]
for i in range(len(vec_w1)):
	m1.append(vec_w1[i].mass)
	m2.append(vec_w2[i].mass)


	
vec_t1=[]
vec_t2=[]

for i in range(len(bjpt)):
	b0=vector.obj(pt=bjpt[i,0],phi=bjphi[i,0],eta=bjeta[i,0],mass=bjmass[i,0])
	b1=vector.obj(pt=bjpt[i,1],phi=bjphi[i,1],eta=bjeta[i,1],mass=bjmass[i,1])

	cand=[b0,b1,vec_w1[i],vec_w2[i]]
	comb=list(combinations(cand,2))

	temp=0
	chi=[]

	for j in range(len(comb)):
		v1=comb[j][0]
		v2=comb[j][1]
		v3=comb[-1-j][0]
		v4=comb[-1-j][1]
		M1=(v1+v2).mass
		M2=(v3+v4).mass
		mt=172.76
		G=10
		chi.append((((M1-mt)/G)**2)+((M2-mt)/G)**2)
		temp=temp+1
		if j > 2:
			break

	for k in range(temp):
		if chi[k] ==min(chi):
			vec_t1.append(comb[k][0]+comb[k][1])
			vec_t2.append(comb[-1-k][0]+comb[-1-k][1])
	if i%10000==0:
		print(i)
t1=[]
t2=[]

for i in range(len(vec_t1)):	
	t1.append(vec_t1[i].mass)
	t2.append(vec_t2[i].mass)

t1=np.array(t1)
t2=np.array(t2)

out=np.concatenate((t1,t2))

np.save('/home/yeobi97/phase2/workspace/reconstruction/FHreconarray',out)
#np.save('/home/yeobi97/phase2/workspace/reconstruction/SLreconarray',out)
#np.save('/home/yeobi97/phase2/workspace/reconstruction/TTWreconarray',out)
#np.save('/home/yeobi97/phase2/workspace/reconstruction/TTZreconarray',out)
#np.save('/home/yeobi97/phase2/workspace/reconstruction/WWreconarray',out)
#np.save('/home/yeobi97/phase2/workspace/reconstruction/WZreconarray',out)
#np.save('/home/yeobi97/phase2/workspace/reconstruction/ZZreconarray',out)

#plt.figure(figsize=(8,8))
#bins = np.linspace(0,50,100)
#plt.hist(t1, range=(0,500), bins=100, histtype='step',linewidth=2,color='blue')
#plt.hist(t2, range=(0,500), bins=100, histtype='step', linewidth=2, color='red')
#plt.show()
#plt.savefig('nTuplereconresult')
#import mplhep as hep
#plt.style.use(hep.style.CMS)
#plt.rcParams["figure.figsize"]=(8,8)
#plt.xlim(0,500)
#plt.hist(out,range=(0,500),bins=100,histtype='step',color='blue')
#plt.hist(out,range=(0,500),bins=100,histtype='step',color='red')
#plt.xlabel('M$_{jjj}$ [GeV]')
#plt.ylabel('Arb. Unit / 5 GeV')
#plt.legend()
#plt.savefig('nTuplebackgroundreconstructionresult')
#plt.show()
