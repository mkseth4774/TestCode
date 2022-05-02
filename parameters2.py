#!/usr/bin/env python3
##
##
def sshnodes(param1, param2, arg4, arg3):
    print('param1 is:', param1)
    print('param2 is:', param2)
    print('param3 is:', arg3)
    print('param4 is:', arg4)

myList = ['nodename','ip','username','password']

sshnodes(*myList)
##
##End of file
