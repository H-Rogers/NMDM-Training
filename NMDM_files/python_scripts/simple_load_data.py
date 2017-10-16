# This program was written by Simon Mudd
# It is used to demonstrate some properties of file reading and writing
# As well as some properties of numpy arrays and lists

# import the numerical python package
import numpy as np

print "Welcome to the load data file, I am your computer."
print "I am going to try to open the file some_data.csv"

# use this is you want to load this text using numpy
# It is best if the number of data elements in each row is the same!
# my_data = np.loadtxt(fname = 'some_data.csv', delimiter=',')

# this is the standard python way to open a file
f = open('some_data.csv','r')

print "What is f?"
print f

# get all the lines in the file
lines = f.readlines()

print "these are the lines in the file"
print lines



# Now split the line with the comma character. 
#
# ~~~~~~~~~~TASK~~~~~~~~~~~~~
#
# See how this differs from simple_load_data2.py
# The code is different but this gets split line from the first row in the file. 
split_line = lines[0].split(',')

# the variable split_line is now an array with elements from the first line
print "split line is: "
print split_line

# go through the elements in the first line, printing them to screen
for element in split_line:
  num = int(element)
  print num


