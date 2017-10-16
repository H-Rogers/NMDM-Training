# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:30:14 2015

@author: smudd
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

N = 50
x = np.random.rand(N)
av_mole = x

HIG = 1+2*np.exp(x)+x*x+np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2

mole_error = 0.1 + 0.1*np.sqrt(av_mole)
hig_error = 0.1 + 0.2*np.sqrt(HIG)/10

fig = plt.figure(1, facecolor='white',figsize=(10,7.5))
ax = plt.subplot(1,1,1)

obj = ax.scatter(av_mole, HIG, s=70, c=area, marker='o',cmap=plt.cm.jet, zorder=10)
cb = plt.colorbar(obj)
cb.set_label('Field Area (m2)',fontsize=20)

ax.errorbar(av_mole, HIG, xerr=mole_error, yerr=hig_error, fmt='o',color='b')

plt.xlabel('Average number of moles per sq. meter', fontsize = 18)
plt.ylabel('Health Index for Gardeners (HIG)', fontsize = 18)
plt.title('Mole population against gardeners health', fontsize = 24)

plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(av_mole, HIG)

print 'slope = ', slope
print 'intercept = ', intercept
print 'r value = ', r_value
print  'p value = ', p_value
print 'standard error = ', std_err

line = slope*av_mole+intercept
plt.plot(av_mole,line,'m-')
plt.title('Linear fit y(x)=ax+b, with a='+str('%.1f' % slope)+' and b='+str('%.1f' % intercept), fontsize = 24)

plt.show()