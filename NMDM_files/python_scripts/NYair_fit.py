"""
Scatterplots of air quality and meteorological data with fitted lines
By Richard Essery
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8), dpi=100)
plt.subplots_adjust(wspace=0.2, hspace=0.2)
plt.rcParams['font.size'] = 11

vars = ['O$_3$(ppb)','Radiation (MJ m$^{-2}$)','Temperature ($^\circ$C)',
        'Wind speed (m s$^{-1}$)']
vlim = np.array([[0,200],[0,15],[0,50],[0,50]])
        
data = np.loadtxt('NYair.txt',skiprows=2)
corrmat = np.around(np.corrcoef(data, rowvar=0), decimals=2)
for j in range(3):
    for i in range(j+1,4):
        plt.subplot(3,3,i+3*j)
        plt.plot(data[:,i],data[:,j],'o',ms=4)
        plt.xlim(vlim[i,:])
        plt.ylim(vlim[j,:])
        b = np.polyfit(data[:,i],data[:,j],1)
        line = b[0]*vlim[i,:] + b[1]
        plt.plot(vlim[i,:],line,'k')
        if i == j+1:
            plt.xlabel(vars[i])
            plt.ylabel(vars[j])
        else:
            plt.xticks([])
            plt.yticks([])
        if j == 0:
            plt.title(vars[i])
        if i == 3:
            plt.text(53,np.mean(vlim[j,:]),vars[j],rotation=-90,
                     verticalalignment='center',fontsize=13)
        label = 'r$^2$=' + str(round(corrmat[i,j]**2,2))
        plt.text(0.6*vlim[i,1], 0.85*vlim[j,1], label)
plt.show()
