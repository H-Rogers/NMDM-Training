"""
Plot flow data for each month on one plot
By Richard Essery
"""
import matplotlib.pyplot as plt
import numpy as np
from calendar import month_abbr

mnth = np.loadtxt('Tay1993.txt', skiprows=1, usecols=[1])
date = np.loadtxt('Tay1993.txt', skiprows=1, usecols=[2])
flow = np.loadtxt('Tay1993.txt', skiprows=1, usecols=[3])

for i in range(1,13):
    days = date[mnth == i]
    flow_month = flow[mnth == i]
    plt.plot(days, flow_month, label=month_abbr[i])
plt.xlim(1,31)
plt.xlabel('Day of month')
plt.ylim(0,2000)
plt.ylabel('Flow (m$^3$ s$^{-1}$)')
plt.legend(loc='upper left')
plt.show()
