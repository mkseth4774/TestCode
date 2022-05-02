#!/usr/bin/env python3
##
##

def funscope():
    list1.append('Thsi was appended inside the function')
    
list1 = [8,9,10]
print('Before we call the function is', list1)
funscope()
print('The list outside of the function is:', list1)

##
##End of file
