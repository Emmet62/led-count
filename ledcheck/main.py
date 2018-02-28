'''
Created on 27 Feb 2018

@author: Emmet
'''

import sys
import requests

''' Create a class for the LightTester'''
class LightTester():
    lights = None
    
    def __init__(self):
        pass
        
    def file_format(self):
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
        response = requests.get(file)
    else:
        response = open(file, 'r')
    return response

def read_file():
    pass

def main():
    pass

if __name__ == '__main__':
    main()