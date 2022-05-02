#!/usr/bin/env python3
##
##

nodeSerialNumber = 'FTX8675309'
fh = open('routers.txt')

line=fh.readline()
while line:
    if nodeSerialNumber in line:
        line=fh.readline()
        continue
    else:
        print(line.strip())
        line=fh.readline()

print()
print()

fh.seek(0)
for lines in fh:
    if nodeSerialNumber in lines:
        continue
    else:
        print(lines.strip())

##
##End of file 
