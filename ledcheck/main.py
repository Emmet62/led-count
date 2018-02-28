'''
Created on 27 Feb 2018

@author: Emmet
'''

import sys
import urllib.request

''' Create a class for the LightTester'''
class LightTester():
    lights = None
    
    def __init__(self):
        pass
        
    def boundaries(self):
        pass
    
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass
    
    def toggle(self):
        pass

def file_existence(file):
    ''' Checks that the input file exists (local file or network address)'''
    if file.startswith('http://'):
        request = urllib.request.urlopen(file)
        response = request.read().decode('utf-8') #.read() is used to convert output to string
    else:
        response = open(file, 'r').read() #.read() is used to convert output to string
    return response

def main():
    pass

if __name__ == '__main__':
    main()