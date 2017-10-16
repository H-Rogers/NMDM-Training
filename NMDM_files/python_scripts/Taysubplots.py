"""
Plot flow data for each month on a different subplot
By Richard Essery
"""
import matplotlib.pyplot as plt
import numpy as np
from calendar import month_name
plt.figure(figsize=(15, 10))

mnth = np.loadtxt('Tay1993.txt', skiprows=1, usecols=[1])
date = np.loadtxt('Tay1993.txt', skiprows=1, usecols=[2])
flow = np.loadtxt('Tay1993.txt', skiprows=1, usecols=[3])

for i in range(1,13):
    days = date[mnth == i]
    flow_month = flow[mnth == i]
    plt.subplot(4,3,i)
    plt.plot(days, flow_month)
    plt.xlim(1,31)
    plt.xlabel('Day of month')
    plt.ylim(0,2000)
    plt.ylabel('Flow (m$^3$ s$^{-1}$)')
    plt.title(month_name[i])
plt.tight_layout()
plt.show()
