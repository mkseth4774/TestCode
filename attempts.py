#!/usr/bin/env python3
##
##
attempts = 0
magicWord = 'cisco'
while True:
    word = input('Pl enter the magic word: ')
    attempts += 1
    if magicWord == word.lower():
        break
    else:
        print('You are getting closer1')

print('You guessed the MagicWord '+ magicWord + ' in ' + str(attempts) + ' attempts')   

##
##End of file 
