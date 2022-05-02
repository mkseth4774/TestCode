#!/usr/bin/env python3
##
##

def funscope():
    global macAddr01
    macAddr01 = '0e:22:fb:e9:35:4a'
    print('The MAC Address that is defined inside the function is', macAddr01)
    
macAddr01 = '00:0c:29:c7:3f:6c'
print('The MAC Address that is globally defined', macAddr01)
funscope()
print('The MAC Address that is globally defined after the function is executed', macAddr01)
##
##End of file
