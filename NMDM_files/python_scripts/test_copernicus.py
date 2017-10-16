# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:05:35 2016

@author: smudd
"""

import FormattedFigures as FF

def test_plot():
    x = [1,2,3,4]
    y = [3,2,1,2]
    
    print x
    print y
    
    FF.SimplePlot(x,y)
    FF.SimplePlot2(x,y,"Toads","Popsicles")
    FF.SimpleGridSpecPlot(x,y,"Hairstyles","Product")
    


# This bit at the bottom tells the python interpreter what to do if you run the
# script directly
if __name__ == "__main__":
    test_plot()    
