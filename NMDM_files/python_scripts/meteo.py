"""
Plot of wind speed, wind vectors and surface pressure
By Richard Essery
"""
import numpy as np
import matplotlib.pylab as plt
plt.figure(figsize=(10, 10))

P = np.loadtxt('Psurf.txt')
U = np.loadtxt('Uwind.txt')
V = np.loadtxt('Vwind.txt')
W = np.sqrt(U**2 + V**2)

# wind speed as an image with a colour bar
plt.imshow(W, cmap='PuBu', origin='lower')
cbar = plt.colorbar(shrink=0.6)
cbar.set_label('wind speed (m s$^{-1}$)', fontsize=16, rotation=270)

# surface pressure as a contour plot with 4 hPa spacing
levels = 960 + 4*np.arange(20)
cs = plt.contour(P, colors='black', levels=levels)
plt.clabel(cs, fmt='%d')

# wind vectors
plt.quiver(U,V)

plt.xticks([])
plt.yticks([])
plt.show()
