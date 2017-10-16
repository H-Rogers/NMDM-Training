"""
Shaded map of Mount Saint Helens
By Richard Essery
"""
import numpy as np
from matplotlib import pylab as plt
from matplotlib.colors import LightSource

z = np.loadtxt('MtStHelens.txt')

ls = LightSource(azdeg=-45, altdeg=45)
shade = ls.shade(z, cmap=plt.cm.gray)
plt.imshow(shade, origin='lower')
plt.xticks([])
plt.yticks([])

plt.show()