import numpy as np
import awkward as ak
import vector
import os, sys

def npyloader(file):
	out=np.load(file,allow_pickle=True)[()]
	return out
'''
def masscalculator(vec):
	for k in range(len(jpt)):
		v1=vec[k][0]
		v2=vec[k][1]
		mjj=(v1+v2).mass
	return mjj
'''

#out = './step4/'

flist=["../step1DM_MY900_nTuple.npy_nTuple.npy_METHT.npy",
"../step1DM_MY800_nTuple.npy_nTuple.npy_METHT.npy",
"../step1DM_MY700_nTuple.npy_nTuple.npy_METHT.npy",
"../step1DM_MY600_nTuple.npy_nTuple.npy_METHT.npy",
"../step1DM_MY500_nTuple.npy_nTuple.npy_METHT.npy",
"../step1DM_MY400_nTuple.npy_nTuple.npy_METHT.npy",
"../step1DM_MY300_nTuple.npy_nTuple.npy_METHT.npy",
"../step1DM_MY200_nTuple.npy_nTuple.npy_METHT.npy"


]

for f in  flist:
	print("now running",f)
	Inst=npyloader(f)
	#mjjj=Inst['Mjjj']
	#ak.flatten(Inst['Mjjj'])
	cut = Inst['MET_PT'] > 50
	cut = ak.flatten(cut)
	mjjj = Inst['Mjjj']
	Inst['Mjjj'] = ak.from_numpy(mjjj)
	
	for key in Inst.keys():
		#Inst[key] = np.array(Inst[key])
		print(Inst[key])
		print(cut)
		print(Inst[key][cut])
		Inst[key]=Inst[key][cut]
			
	jpt=Inst['Jet_PT']
	jeta=Inst['Jet_Eta']
	jphi=Inst['Jet_Phi']
	jmass=Inst['Jet_Mass']

	Mjj=[]
	#print(jpt[:,0])
	j1 = vector.obj(pt=jpt[:,0],phi=jphi[:,0],eta=jeta[:,0],mass=jmass[:,0])
	j2 = vector.obj(pt=jpt[:,1],phi=jphi[:,1],eta=jeta[:,1],mass=jmass[:,1])
	minor = (j1+j2).mass
	Mjj = np.array(minor)
	print(str(flist),Mjj)
	print(len(jpt))
	## I/O
	
	Inst['Mjj'] = Mjj

	np.save(f.replace(".npy_nTuple.npy_METHT.npy","_").replace("../","")+'Mjj_nTuple.npy',Inst)
		
		
			
				
			
		
			 
			


 
			
	

