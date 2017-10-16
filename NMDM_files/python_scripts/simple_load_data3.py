# This program was written by Simon M. Mudd
# A simple progrtam for reading csv files

# import the numerical python package
import numpy as np

print "Welcome to the load data file, I am your computer."
print "I am going to try to open the file some_data.csv"
# my_data = np.loadtxt(fname = 'some_data.csv', delimiter=',')

# here is where you tell python what the filename is
f = open('some_data.csv','r')

print "What is f?"
print f

lines = f.readlines()


# start an empty list.
line_nums = []


# now we try to get all of the data
for line in lines:

  # split this line
  split_line = line.split(',')
  
  # initiate a list for just this line
  this_line_nums = []
  
  for element in split_line:
    num = int(element)
    this_line_nums.append(num)
    
  # now append this line to line nums
  line_nums.append(this_line_nums)
  
# the data are
print line_nums

#get the median of the 2nd line
# median is a function within numpy, so we need to tell python we want the numpy median function
median = np.median(line_nums[1])
print median


#get the mean of the 3rd line
# mean is a function within numpy, so we need to tell python we want the numpy median function
mean = np.mean(line_nums[2])
print mean


# your data is in a python list. 
# Numpy arrays are frequently better for numerics (they have been designed for speed).
# Convert some of your data to a numpy array
first_line_numpy_array = np.asarray(line_nums[0])

#
# ~~~~~~~~~~TASK~~~~~~~~~~~~~
#
# What is the difference in appearance of arrays and lists when printed to screen?
# Note, if you want to do Matlab-like matrix manipulation you'll have to convert to array

# print to screen, showing how python will tell you the difference
print "list:"
print line_nums[0]

print "array: "
print first_line_numpy_array

#
# ~~~~~~~~~~TASK~~~~~~~~~~~~~
#
# Try to convert all of the data (line_nums) to array. What happens?