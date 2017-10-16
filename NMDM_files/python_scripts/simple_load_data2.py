# This program was written by Simon M. Mudd
# A simple progrtam for reading csv files
# It is used to demonstrate some properties of file reading and writing
# As well as some properties of numpy arrays and lists


# import the numerical python package
import numpy as np

print "Welcome to the load data file, I am your computer."
print "I am going to try to open the file some_data.csv"

# here is where you tell python what the filename is
#
# ~~~~~~~~~~TASK~~~~~~~~~~~~~
#
# Try to make a new file and load it!
f = open('some_data.csv','r')

print "What is f?"
print f

# read all the lines in the file
lines = f.readlines()

print "these are the lines in the file"
print lines

# get the first line
line = lines[0]

# get the data elements in the first row
split_line = lines[0].split(',')
print "split line is: "
print split_line


# find the number of elements in the line
n_elements_in_line = len(split_line)


# start an empty list. 
#
# ~~~~~~~~~~TASK~~~~~~~~~~~~~
#
# what happens if you dont start with an empty list?
line_nums = []
line_string = []

# look through the line, getting the elements
for element in split_line:
  num = int(element)
  print num
  line_nums.append(num)
  line_string.append(element)
  
# the line numbers are:  
print line_nums

# the line strings are
print line_string


#
# ~~~~~~~~~~TASK~~~~~~~~~~~~~
#
# what happens if you multiply elements in line_nums together?
# what happens if you multiple elements in line_string together?