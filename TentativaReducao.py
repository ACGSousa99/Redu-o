#GMOS

#Headers necessários:
# Epoch -> float
from astropy.nddata import CCDData
import ccdproc
import time
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from photutils import make_source_mask, Background2D, MeanBackground
from astropy.stats import SigmaClip
import os

ficheiro = "/home/luis/Desktop/ImagensFits/FitsMudado2.fits"
PastaDarks =  "/home/luis/Desktop/ImagensFits/DarksNovos/"
PastaFlats = "/home/luis/Desktop/ImagensFits/FlatsNovos/"

	
Flats = [PastaFlats + x for x in os.listdir(PastaFlats)]
FlatsLidos = [CCDData.read(X, unit='adu') for X in Flats]
mflat = ccdproc.combine(FlatsLidos,method='median')

Darks = [PastaDarks + x for x in os.listdir(PastaDarks)]
DarksLidos = [CCDData.read(X, unit='adu') for X in Darks]
mdark = ccdproc.combine(DarksLidos,method='median')


raw = CCDData.read(ficheiro, unit='adu') # LE O FICHEIRO (TEMOS DE MUDAR ALGUNS HEADERS)


#ver opcao readnoise
reducao1 = ccdproc.ccd_process(raw, dark_frame=mdark,dark_exposure = 100 * u.s,data_exposure = 240 *u.s, master_flat = mflat,readnoise=18.3*u.electron)
reducao2 = ccdproc.ccd_process(raw, dark_frame=mdark,dark_exposure = 240 * u.s,data_exposure = 240 *u.s, master_flat = mflat,readnoise=18.3*u.electron)


diferença1 = CCDData.subtract(raw,reducao1)
diferença2 = CCDData.subtract(raw,reducao2)
diferença3 = CCDData.subtract(reducao1,reducao2)


# ~ mask = make_source_mask(reducao, nsigma=3, npixels=5)
# ~ bkg = Background2D(reducao, (128, 128), filter_size=(3, 3),sigma_clip=SigmaClip(sigma=3), bkg_estimator=MeanBackground(), mask=mask, exclude_percentile=80)
# ~ final = reducao.subtract(CCDData(bkg.background,unit=u.electron),propagate_uncertainties=True,handle_meta='first_found').divide(240*u.second,propagate_uncertainties=True,handle_meta='first_found')







print(np.max(np.asarray(diferença3)))
print(np.min(np.asarray(diferença3)))

























fig,axes = plt.subplots(3,3)
ax = axes.ravel()
vmin,vmax = None,None
ax[0].set_title('Imagem Normal')
ax[0].imshow(raw,cmap='gray',vmin=vmin or np.nanpercentile(raw, 0.1),vmax=vmax or np.nanpercentile(raw, 99))
ax[1].set_title('Imagem Reduzida (Flat+Dark)')
ax[1].imshow(reducao1,cmap='gray',vmin=vmin or np.nanpercentile(reducao1, 0.1),vmax=vmax or np.nanpercentile(reducao1, 99))
ax[2].set_title('Diferença')
ax[2].imshow(diferença1,cmap='gray',vmin=vmin or np.nanpercentile(diferença1, 0.1),vmax=vmax or np.nanpercentile(diferença1, 99))
ax[4].set_title('Imagem Reduzida (Flat+Dark)')
ax[4].imshow(reducao2,cmap='gray',vmin=vmin or np.nanpercentile(reducao2, 0.1),vmax=vmax or np.nanpercentile(reducao2, 99))
ax[5].set_title('Diferença')
ax[5].imshow(diferença2,cmap='gray',vmin=vmin or np.nanpercentile(diferença2, 0.1),vmax=vmax or np.nanpercentile(diferença2, 99))
ax[3].set_title('DiferençaNova')
ax[3].imshow(diferença3,cmap='gray',vmin=vmin or np.nanpercentile(diferença3, 0.1),vmax=vmax or np.nanpercentile(diferença3, 99))

ax[6].set_title('Master Flat')
ax[6].imshow(mflat,cmap='gray',vmin=vmin or np.nanpercentile(mflat, 0.1),vmax=vmax or np.nanpercentile(mflat, 99))
ax[7].set_title('Master Dark')
ax[7].imshow(mdark,cmap='gray',vmin=vmin or np.nanpercentile(mdark, 0.1),vmax=vmax or np.nanpercentile(mdark, 99))

plt.show()
