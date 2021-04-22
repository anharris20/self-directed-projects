# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import copy

#user input
str = input ("Enter names separated with commas (and don't forget to include yourself!'): ")
print()

#splits user insput string into multiple elements
str_split = str.split(", ")

#places elements into numpy array
str_array = np.array(str_split)

#copies array for later pairing
str_array2 = copy.deepcopy(str_array)

#check for number of elements in array
element_count = len(str_array)

#feckin' loop -- pair generation
while element_count != 0:
    np.random.shuffle(str_array)
    np.random.shuffle(str_array2)
    if str_array[0] != str_array2[0]:
        print (str_array[0]+"'s secret santa is", str_array2[0])
        str_array = np.delete(str_array, 0)
        str_array2 = np.delete(str_array2, 0)
        element_count = element_count - 1
    elif str_array[0] == str_array2[0]:
            np.random.shuffle(str_array2)
    else:
        print ("something's wrong!")

print()

#Keeps command line from closing automatically
input ("Press Enter to exit:")