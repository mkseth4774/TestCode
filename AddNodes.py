#!/usr/bin/env python3
##
##
nodeName = input('Pl enter the routerHostname: ')
nodeipAddress = input('Pl enter the Mgmt IP address of vendor equipment: ')
nodeSerialNumber = input('Pl enter the serial# of the vendor equipment: ')

nodesString = open('routers.txt').read()

if nodeSerialNumber in nodesString:
    print('Duplicate Detected: ' + nodeSerialNumber)
else:
    try:
        with open('routers.txt','a+') as fh:
            fh.write(nodeName + ',' + nodeipAddress + ',' + nodeSerialNumber + ',admin,cisco123\n')
            print(nodeSerialNumber,'has been added succesfully')
    except IOError:
        print('Problem encountered when adding vendor equipement Serial#')

##
##End of file
