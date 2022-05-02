#!/usr/bin/env python3
##
##
##def sshnodes(param1, param2, arg4, arg3):
def sshnodes(nodename, ip, password, username):
    print('param1 is:', nodename)
    print('param2 is:', ip)
    print('param3 is:', username)
    print('param4 is:', password)

myDict = {'nodename':'rtr001','ip':'10.0.0.1','username':'mksethi','password':'cisco'}

sshnodes(**myDict)
##
##End of file
