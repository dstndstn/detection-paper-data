
from astrometry.util.fits import fits_table
import numpy as np
import os

T = fits_table('survey-ccds-snx3-25.fits')
for fn in np.unique(T.image_filename):
    I = np.flatnonzero(T.image_filename == fn)
    print(len(I), 'ext for', fn)

    exts = ' '.join(['-e %i' % e for e in T.image_hdu[I]])
    for rep in ['_ooi_', '_oow_', '_ood_']:
        fnx = fn.replace('_ooi_', rep)
        infn = os.path.join('images', fnx)
        outfn = os.path.join('images-sub', fnx)
        outdir = os.path.dirname(outfn)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        cmd = 'fitsgetext -i %s -o %s -e 0 %s' % (infn, outfn, exts)
        print(cmd)
        os.system(cmd)

    T.image_hdu[I] = 1 + np.arange(len(I))
T.writeto('survey-ccds-snx3-25-sub.fits')
