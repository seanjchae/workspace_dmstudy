import uproot 
import awkward as ak
import vector
import numpy as np
import glob

from tqdm import tqdm

def Eagles(filepath, filetype):
	allfiles = glob.glob(filepath) #glob.glob: function that import files
	filelist =[]
	for f in allfiles:
		filelist.append(f+':Delphes')

	branches = ['JetPUPPI.PT','JetPUPPI.Eta','JetPUPPI.Phi','JetPUPPI.Mass','JetPUPPI.BTag','PuppiMissingET.MET','PuppiMissingET.Phi']

	histo ={}
	count=0

	for arrays,doc in tqdm(uproot.iterate(filelist, branches, report =True)):
		print("from : {0}, to {1} -- Entries : {2}".format(doc.start,doc.stop,len(arrays)))

		#using puppi jets
		Jet = ak.zip(
		{
			"PT" : arrays[b"JetPUPPI.PT"],
			"Eta": arrays[b"JetPUPPI.Eta"],
			"Phi": arrays[b"JetPUPPI.Phi"],
			"Mass": arrays[b"JetPUPPI.Mass"],
			"BTag": arrays[b"JetPUPPI.BTag"]
		})

		MET =ak.zip(
		{
			"PT" : arrays[b"PuppiMissingET.MET"],
			"Phi": arrays[b"PuppiMissingET.Phi"]
		})

		
		#Jet identification
		Jetid=(Jet.PT>=30)
		Jet=Jet[Jetid]

		#jet number cut
		Sel_Jet_num=ak.num(Jet.PT)>=6 # select events that have six or more jets
		Jet=Jet[Sel_Jet_num] 
		MET=MET[Sel_Jet_num]
		
		# BJet identification
		BTag=(Jet.BTag & 2) == 2 # select jets that have score 25 or more on BTag
		#print(BTag)
		#break
		BJet=Jet[BTag]
		
		# non BJet identification
		nonBTag=(Jet.BTag & 2) !=2
		normalJet=Jet[nonBTag]
		
		# number of bjet cut
		Sel_BJet_num = ak.num(BJet)>= 2 # selec events that have 2 or more b jets
		Jet=Jet[Sel_BJet_num]
		MET=MET[Sel_BJet_num]
		BJet=BJet[Sel_BJet_num]
		
		#???MET cut? //lepton veto?

		if len(histo) == 0:

			histo['Jet_PT'] = Jet.PT
			histo['Jet_Eta'] = Jet.Eta
			histo['Jet_Phi'] = Jet.Phi
			histo['Jet_Mass'] = Jet.Mass
			histo['MET_PT'] = MET.PT
			histo['MET_Phi']= MET.Phi
			histo['BJet_PT']=BJet.PT
			histo['BJet_Eta']=BJet.Eta
			histo['BJet_Phi']=BJet.Phi
			histo['BJet_Mass']=BJet.Mass
			histo['normalJet_PT']=normalJet.PT
			histo['normalJet_Eta']=normalJet.Eta
			histo['normalJet_Phi']=normalJet.Phi
			histo['normalJet_Mass']=normalJet.Mass
		else:
			
			histo['Jet_PT']=np.concatenate((histo['Jet_PT'],Jet.PT))
			histo['Jet_Phi']=np.concatenate((histo['Jet_Phi'],Jet.Phi))
			histo['Jet_Eta']=np.concatenate((histo['Jet_Eta'],Jet.Eta))
			histo['Jet_Mass']=np.concatenate((histo['Jet_Mass'],Jet.Mass))
			histo['MET_PT']=np.concatenate((histo['MET_PT'],MET.PT))
			histo['MET_Phi']=np.concatenate((histo['MET_Phi'],MET.Phi))
			histo['BJet_PT']=np.concatenate((histo['BJet_PT'],BJet.PT))
			histo['BJet_Eta']=np.concatenate((histo['BJet_Eta'],BJet.Eta))
			histo['BJet_Phi']=np.concatenate((histo['BJet_Phi'],BJet.Phi))
			histo['BJet_Mass']=np.concatenate((histo['BJet_Mass'],BJet.Mass))
			histo['normalJet_PT']=np.concatenate((histo['normalJet_PT'],normalJet.PT))
			histo['normalJet_Eta']=np.concatenate((histo['normalJet_Eta'],normalJet.Eta))
			histo['normalJet_Phi']=np.concatenate((histo['normalJet_Phi'],normalJet.Phi))
			histo['normalJet_Mass']=np.concatenate((histo['normalJet_Mass'],normalJet.Mass))


	np.save(folder+filetype+"_nTuple", histo)



label_list = ["FH_2", "1l_2", "2l_2", "TTW", "TTZ", "WW", "WZ", "ZZ"]
'''
label = ["signal_1GeV_01", "signal_1GeV_10"]
path = ["/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd_1GeV/rootfile/ttb_xd_1GeV_01*",
	"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd_1GeV/rootfile/ttb_xd_1GeV_10*"]
'''
#root file of fullhadronic/semileptonic/TTW/TTZ/WW/WZ/ZZ background events
path_list = ["/x6/spool/twkim/MC/genproductions/bin/MadGraph5_aMCatNLO/condor/TTTo4j/lheOut/rootOut/*.root",
'/x6/spool/twkim/MC/genproductions/bin/MadGraph5_aMCatNLO/condor/TTToSemilepton/lheOut/rootOut/*.root',
"/x6/spool/twkim/MC/genproductions/bin/MadGraph5_aMCatNLO/condor/TTToSemilepton/lheOut/rootOut/*.root",
"/x6/spool/twkim/MC/genproductions/bin/MadGraph5_aMCatNLO/condor/TTWToInclusive/lheOut/rootOut/*.root",
"/x6/spool/twkim/MC/genproductions/bin/MadGraph5_aMCatNLO/condor/TTZToInclusive/lheOut/rootOut/*.root",
"/x6/spool/bjpark/condor/condorplace/WW/rootOut/*.root",
"/x6/spool/bjpark/condor/condorplace/WZ/rootOut/*.root",
"/x6/spool/bjpark/condor/condorplace/ZZ/rootOut/*.root"]


	#"/x4/cms/jyshin/TT_1l/condorDelPyOut/TT_1l_*.root",
	#"/x4/cms/twkim/MCEVENTS/TT_2l_200PU_PWG2_e05.root",
        #"/x4/cms/jyshin/TT_Had/condorDelPyOut/TT_Had_*.root",
	#"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_01*",
	#"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_02*",
	#"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_03*",
        #"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_04*",
        #"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_05*",
        #"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_06*",
        #"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_07*",
        #"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_08*",
        #"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_09*",
        #"/home/sgjeong/workspace/MG5_aMC_v2_6_7/ttb_xd/rootfile/ttb_xd_10*"]


folder = '/home/yeobi97/phase2/workspace/'



for i in range(0, len(label_list)):
	Eagles(path_list[i], label_list[i])
'''

		
	
