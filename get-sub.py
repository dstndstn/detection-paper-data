
from astrometry.util.fits import fits_table
import numpy as np
import os

T = fits_table('survey-ccds-snx3-25.kd.fits')
for fn in np.unique(T.image_filename):
    I = np.flatnonzero(T.image_filename == fn)
    print(len(I), 'ext for', fn)
    infn = os.path.join('images', fn)
    outfn = os.path.join('images-sub', fn)
    outdir = os.path.dirname(outfn)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    exts = ' '.join(['-e %i' % e for e in T.image_hdu[I]])
    cmd = 'fitsgetext -i %s -o %s -e 0 %s' % (infn, outfn, exts)
    print(cmd)
    os.system(cmd)
