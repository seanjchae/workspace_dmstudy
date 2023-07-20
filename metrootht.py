import numpy as np
import awkward as ak
import vector


def npyloader(file):
	out=np.load(file,allow_pickle=True)[()]
	return out

flist=[
"./step1DM_MY900_nTuple.npy_nTuple.npy",
"./step1DM_MY800_nTuple.npy_nTuple.npy",
"./step1DM_MY700_nTuple.npy_nTuple.npy",
"./step1DM_MY600_nTuple.npy_nTuple.npy",
"./step1DM_MY500_nTuple.npy_nTuple.npy",
"./step1DM_MY400_nTuple.npy_nTuple.npy",
"./step1DM_MY300_nTuple.npy_nTuple.npy",
"./step1DM_MY200_nTuple.npy_nTuple.npy"
]


for f in flist:
	print("now running",f)
	Inst=npyloader(f)
	
	met=Inst['MET_PT']
	ht=Inst['HT_PT']
	
	MET_over_sqrt_HT=[]

	

	for i in range(len(met)):
		met_ht=met[i]/(ht[i]**(1/2))
		MET_over_sqrt_HT.append(met_ht)
		if i%1000 ==0:
			print("now",i,"th events")
	Inst['MET_over_sqrt_HT']=np.array(MET_over_sqrt_HT)
	
	np.save("./"+f+"_METHT",Inst)
	
