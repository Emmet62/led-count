'''
Created on 27 Feb 2018

@author: Emmet
'''

import sys
import urllib.request
import re

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
    ''' Reads the input file (local file or network address) and converts contents to a string'''
    if file.startswith('http://'):
        request = urllib.request.urlopen(file)
        response = request.read().decode('utf-8') #.read() is used to convert output to string
    else:
        response = open(file, 'r').read() #.read() is used to convert output to string
    return response

def file_clean(file):
    ''' Use the string we string from file_existence to check that any commands other then "turn on", "turn off", and "toggle" are ignored'''
    str = file_existence(file)
    cleaned = re.findall(r".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", str)
    return cleaned

def main():
    pass

if __name__ == '__main__':
    main()