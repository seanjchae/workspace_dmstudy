import numpy as np
import awkward as ak
import matplotlib.pyplot as plt

fh=np.load('FHreconarray.npy')
sl=np.load('Semileptonic1array.npy')
ttw=np.load('TTWreconarray.npy')
ttz=np.load('TTZreconarray.npy')
ww=np.load('WWreconarray.npy')
wz=np.load('WZreconarray.npy')
zz=np.load('ZZreconarray.npy')
dmsig=np.load('outsavedmsignewB.npy')

STAK=[dmsig,fh,sl,ttw,ttz,ww,wz,zz]
wht_dm=np.ones(dmsig.shape)*0.0004305 *3000000/100000
wht_fh=np.ones(fh.shape)*210.534*3000000/10000000
wht_sl=np.ones(sl.shape)*211*3000000/10000000
wht_ttw=np.ones(ttw.shape)*0.3664*3000000/10000000
wht_ttz=np.ones(ttz.shape)*0.6428*3000000/10000000
wht_ww=np.ones(ww.shape)*68.3*3000000/10000000
wht_wz=np.ones(wz.shape)*26.16*3000000/10000000
wht_zz=np.ones(zz.shape)*9.841*3000000/10000000
WHT=[wht_dm,wht_fh,wht_sl,wht_ttw,wht_ttz,wht_ww,wht_wz,wht_zz]
label=['DMsig','TT~FH','TT~SL','TTW','TTZ','WW','WZ','ZZ']

import mplhep as hep
plt.style.use(hep.style.CMS)
plt.rcParams["figure.figsize"]=(10,8)
plt.yscale('log')
plt.xlim(0,1000)
plt.hist(STAK,weights=WHT,range=(0,1000),bins=100,histtype='step',label=label)
plt.xlabel('M$_{jjj}$ [GeV]')
plt.ylabel('normalized_unit')
plt.legend()
plt.show()
