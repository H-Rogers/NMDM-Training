#A code to complete 5.1.2 in Simon Mudd's NMDM tutorial

#Import required packages
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


#Generate Random Data
N = 50
x = np.random.rand(N)
av_mole = x

#Create HIG variable and area variable
HIG = 1 + 2*np.exp(x) + x**2 + np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2

#Create an error assosiated with each variable
mole_error = 0.1+0.1*np.sqrt(av_mole)
hig_error = 0.1* 0.2*np.sqrt(HIG)/10

#Plot av_mole against HIG in a scatter plot
#set up figure
fig = plt.figure(1, facecolor='white', figsize = (10,7.5))
ax = plt.subplot(1,1,1)

#plot data
obj = ax.scatter(av_mole,HIG, s=70, c=area, marker = 'o', cmap = plt.cm.jet, zorder = 10)
cb = plt.colorbar(obj)
cb.set_label('Field Area (m2)', fontsize = 20)

#add error bars
ax.errorbar(av_mole,HIG, xerr = mole_error, yerr = hig_error, fmt= 'o', color= 'b')

#add labels
plt.xlabel('Average number of moles per a sq meter', fontsize= 18)
plt.ylabel('Health index for Gardeners (HIG)', fontsize = 18)
plt.title('Mole population against gardeners health', fontsize = 24)

#Add slope
slope, intercept, r_value, p_value, std_err = stats.linregress(av_mole, HIG)

#Print output
print 'slope = ', slope
print 'intercept = ', intercept
print 'r value = ', r_value
print 'p value = ', p_value
print 'standard error = ', std_err

line = slope*av_mole+intercept
plt.plot(av_mole,line,'m-')
plt.title('Linear fit y(x)=ax+b, with a = '+str('%.1f' % slope)+' and b=' +str('%.1f' % intercept), fontsize=24)
plt.savefig('PythonTest.svg', format="svg")