'''
Created on 27 Feb 2018

@author: Emmet
'''

import sys
import urllib.request
import re

class LightTester():
    ''' Create a class for the LightTester'''
    lights = None
    
    '''The display board is of size SxS
    Every value is set to 0 originally, representing off'''
    def __init__(self, S):
        self.array = [[0 for x in range (S)] for y in range (S)]
        self.size = S
        
    def boundaries(self):
        pass
    
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass
    
    def toggle(self):
        pass

def file_existence(file):
    ''' Reads the input file (local file or network address) and converts contents to a string'''
    if file.startswith('http://'):
        request = urllib.request.urlopen(file)
        response = request.read().decode('utf-8') #.read() is used to convert output to string
    else:
        response = open(file, 'r').read() #.read() is used to convert output to string
    return response

def file_clean(file):
    ''' Use the string we return from file_existence to check that any commands that are not "turn on", "turn off", and "toggle" are ignored'''
    str = file_existence(file)
    cleaned = re.findall(r".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", str)
    return cleaned    

def main():
    pass

if __name__ == '__main__':
    main()