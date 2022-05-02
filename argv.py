#!/usr/bin/env python3
##
##
##import sys
from sys import argv
from sys import exit
##from sys import argv as args

if len(argv) < 2:
##    exit("""
##RaiseArgumentException: Need at least 1 command line argument
##Not provided
##""")
    exit(99)

print(argv[1:])

##
##End of file
