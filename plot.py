import numpy as np
import awkward as ak
import matplotlib.pyplot as plt
import mplhep as hep
import vector

def arrayLoader(f,var):
        out=np.load(f,allow_pickle=True)[()][''+str(var)+'']
        return out

dm1000='/home/yeobi97/phase2/preselection/step2/step3/step4/DM_nTuple_Mjj_nTuple.npy'
dm100='/home/yeobi97/phase2/preselection/step2/step3/step4/DM_MY100_nTuple_Mjj_nTuple.npy'
dm200='./step1DM_MY200_nTuple_Mjj_nTuple.npy'
dm300='./step1DM_MY300_nTuple_Mjj_nTuple.npy'
dm400='./step1DM_MY400_nTuple_Mjj_nTuple.npy'
dm500='./step1DM_MY500_nTuple_Mjj_nTuple.npy'
dm600='./step1DM_MY600_nTuple_Mjj_nTuple.npy'
dm700='./step1DM_MY700_nTuple_Mjj_nTuple.npy'
dm800='./step1DM_MY800_nTuple_Mjj_nTuple.npy'
dm900='./step1DM_MY900_nTuple_Mjj_nTuple.npy'


var = 'HT_PT'
Instdm1000=arrayLoader(dm1000,var)
Instdm100=arrayLoader(dm100,var)
Instdm200=arrayLoader(dm200,var)
Instdm300=arrayLoader(dm300,var)
Instdm400=arrayLoader(dm400,var)
Instdm500=arrayLoader(dm500,var)
Instdm600=arrayLoader(dm600,var)
Instdm700=arrayLoader(dm700,var)
Instdm800=arrayLoader(dm800,var)
Instdm900=arrayLoader(dm900,var)

'''
dm1000=ak.flatten(Instdm1000)
dm100=ak.flatten(Instdm100)
dm200=ak.flatten(Instdm200)
dm300=ak.flatten(Instdm300)
dm400=ak.flatten(Instdm400)
dm500=ak.flatten(Instdm500)
dm600=ak.flatten(Instdm600)
dm700=ak.flatten(Instdm700)
dm800=ak.flatten(Instdm800)
dm900=ak.flatten(Instdm900)
'''
dm1000=np.array(Instdm1000)
dm100=np.array(Instdm100)
dm200=np.array(Instdm200)
dm300=np.array(Instdm300)
dm400=np.array(Instdm400)
dm500=np.array(Instdm500)
dm600=np.array(Instdm600)
dm700=np.array(Instdm700)
dm800=np.array(Instdm800)
dm900=np.array(Instdm900)
'''
STAK=[zz,wz,ww,ttz,ttw,sl,fh]
CO = ['lightgreen','yellow','beige','dodgerblue','grey','orange','blue']
ED = ['black','black','black','black','black','black','black']
label=['ZZ','WZ','WW',r'$t\bar{t}$ + Z',r'$t\bar{t}$ + W',r'$t\bar{t}$ (1$\ell$)',r'$t\bar{t}$ (FH)']
'''
wht_dm=np.ones(dm1000.shape)*0.0004305 *3000000/100000
wht_dm100=np.ones(dm100.shape)*0.12*3000000/100000
wht_dm200=np.ones(dm200.shape)*0.04032*3000000/100000
wht_dm300=np.ones(dm300.shape)*0.01712*3000000/100000
wht_dm400=np.ones(dm400.shape)*0.0007852*3000000/100000
wht_dm500=np.ones(dm500.shape)*0.004157*3000000/100000
wht_dm600=np.ones(dm600.shape)*0.002406*3000000/100000
wht_dm700=np.ones(dm700.shape)*0.001473*3000000/100000
wht_dm800=np.ones(dm800.shape)*0.0009431*3000000/100000
wht_dm900=np.ones(dm900.shape)*0.0006282*3000000/100000


'''
wht_fh=np.ones(fh.shape)*210.534*3000000/10000000
wht_sl=np.ones(sl.shape)*211*3000000/10000000
wht_ttw=np.ones(ttw.shape)*0.3664*3000000/10000000
wht_ttz=np.ones(ttz.shape)*0.6428*3000000/10000000
wht_ww=np.ones(ww.shape)*68.3*3000000/10000000
wht_wz=np.ones(wz.shape)*26.16*3000000/10000000
wht_zz=np.ones(zz.shape)*9.841*3000000/10000000

WHT=[wht_zz,wht_wz,wht_ww,wht_ttz,wht_ttw,wht_sl,wht_fh]
'''

RANGE = (0,1000)
BIN = 100

import mplhep as hep
plt.style.use(hep.style.CMS)
plt.rcParams["figure.figsize"]=(10,10)
plt.yscale('log')
plt.xlim(0,1000)
plt.ylim(1e-02,1e+10)
plt.hist(dm1000,weights=wht_dm,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 1 TeV')
plt.hist(dm900,weights=wht_dm900,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.9 TeV')
plt.hist(dm800,weights=wht_dm800,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.8 TeV')
plt.hist(dm700,weights=wht_dm700,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.7 TeV')
plt.hist(dm600,weights=wht_dm600,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.6 TeV')
plt.hist(dm500,weights=wht_dm500,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.5 TeV')
plt.hist(dm400,weights=wht_dm400,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.4 TeV')
plt.hist(dm300,weights=wht_dm300,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.3 TeV')
plt.hist(dm200,weights=wht_dm200,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.2 TeV')
plt.hist(dm100,weights=wht_dm100,range=RANGE,bins=BIN,histtype='step',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.1 TeV')
plt.xlabel('HT')
plt.ylabel('Number of Events / '+str(int(max(RANGE)/BIN))+' GeV')
plt.legend()
plt.show()









'''
plt.hist(STAK,weights=WHT,range=RANGE,bins=BIN,stacked=True,color=CO,histtype='stepfilled',label=label)
plt.hist(STAK,weights=WHT,range=RANGE,bins=BIN,stacked=True,color=ED,histtype='step')
plt.hist(dm1000,weights=wht_dm,range=RANGE,bins=BIN,histtype='step',color='red',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 1 TeV')
plt.hist(dm100,weights=wht_dm100,range=RANGE,bins=BIN,histtype='step',color='indigo',linewidth=2.5,label='$m$$_{X_{D}}$ = 10 GeV\n$m$$_{V}$ = 0.1 TeV')
plt.xlabel('Mjjj [GeV]')
plt.ylabel('Number of Events / '+str(int(max(RANGE)/BIN))+' GeV')
plt.legend(fontsize=15)
plt.show()
'''
