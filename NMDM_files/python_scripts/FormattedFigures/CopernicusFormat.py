# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:55:52 2016

@author: smudd
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams


# A very simple plot that makes an 83mm wide figure
def SimplePlot(x,y):
    
    # We want a pdf figure so we set the fileformat to pdf
    FileFormat = "pdf"    
    
    # Set the label font
    label_size = 8

    # Set up fonts for plots
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['arial']
    rcParams['font.size'] = label_size
    
    plt.figure(1, facecolor='white',figsize=(3.26,3.26))  
    plt.plot(x,y)
    plt.savefig("A_figure.pdf", format = FileFormat)
    plt.clf()
 
# A very simple plot that makes an 83mm wide figure
def SimplePlot2(x,y,xlabel_text = "x", ylabel_text = "y"):
    
    # We want a pdf figure so we set the fileformat to pdf
    FileFormat = "png"    
    
    # Set the label font
    default_size = 8
    label_size = 11

    # Set up fonts for plots
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['arial']
    rcParams['font.size'] = default_size
    
    plt.figure(1, facecolor='white',figsize=(3.26,3.26)) 
    ax = plt.subplot(111)    
    ax.plot(x,y,linewidth=2) 
    plt.xlabel(xlabel_text,fontsize = label_size)
    plt.ylabel(ylabel_text,fontsize = label_size) 

    # This makes all the spines thick so you can see them         
    ax.spines['top'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['right'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
        
    # This gets all the ticks, and pads them away from the axis so that the corners don't overlap
    ax.tick_params(axis='both', width=1.5, pad = 2, length = 3,direction="in")
    for tick in ax.xaxis.get_major_ticks():
        tick.set_pad(10)

    plt.savefig("Figure2.png", format = FileFormat)
    plt.clf()
   
# A very simple plot that makes an 83mm wide figure, using GridSpec
def SimpleGridSpecPlot(x,y,xlabel_text = "x", ylabel_text = "y"):
 
    # We need to get the GridSpec package
    from matplotlib.gridspec import GridSpec
   
    # We want a pdf figure so we set the fileformat to pdf
    FileFormat = "png"    
    
    # Set the label font
    default_size = 8
    label_size = 11

    # Set up fonts for plots
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['arial']
    rcParams['font.size'] = default_size
    
    Fig1 = plt.figure(1, facecolor='white',figsize=(3.26,3.26)) 
    
    # generate a 100x100 grid. The other bits of data are the padding on the edge 
    gs = GridSpec(100,100,bottom=0.13,left=0.0,right=0.95,top=1.0)     

    # Now place the plot in the grid. NOTE: the first set of numbers is the rows (vertical direction),
    # starting from the TOP
    ax = Fig1.add_subplot(gs[15:90,15:95])
    
   
    ax.plot(x,y,linewidth=2) 
    plt.xlabel(xlabel_text,fontsize = label_size)
    plt.ylabel(ylabel_text,fontsize = label_size) 

    # This makes all the spines thick so you can see them         
    ax.spines['top'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['right'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
        
    # This gets all the ticks, and pads them away from the axis so that the corners don't overlap
    ax.tick_params(axis='both', width=1.5, pad = 2, length = 3,direction="in")
    for tick in ax.xaxis.get_major_ticks():
        tick.set_pad(10)

    plt.savefig("Figure_GridSpec.png", format = FileFormat)
    plt.clf() 
   