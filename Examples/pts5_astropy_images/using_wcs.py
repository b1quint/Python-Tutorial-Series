#!/usr/bin/python

from astropy.io import fits
from astropy.wcs import WCS
from matplotlib import pyplot as plt


hdul = fits.open("simple_image.fits")
sci = hdul["SCI"]
wcs = WCS(hdul["SCI"].header)

ax = plt.subplot(projection=wcs)
ax.imshow(sci.data)
ax.coords.grid(True, color="white", ls="solid")
ax.coords[0].set_axislabel("Right Ascention (J2000)")
ax.coords[1].set_axislabel("Declination (J2000)")

plt.show()

