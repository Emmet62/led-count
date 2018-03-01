'''
Created on 27 Feb 2018

@author: Emmet
'''

import sys
import urllib.request
import re
from tkinter import Grid

class LightTester():
    ''' Create a class for the LightTester'''
    lights = None
    
    def __init__(self, S):
        '''The display board is of size SxS
        Every value is set to 0 originally, representing off'''
        self.grid = [[0 for x in range (S)] for y in range (S)]
        self.size = S
        
    def boundaries(self, start, stop):
        ''' If a command affects a region outside the area of the grid, 
        then it will still be executed, but only on the region of lights inside the boundary of the grid'''
        if start[0] < 0:
            start[0] = 0
        if start[1] >= self.size:
            start[1] = (self.size - 1)
        if stop[0] < 0:
            stop[0] = 0
        if stop[1] >= self.size:
            stop[1] = (self.size - 1)
        return start, stop
    
    def turn_on(self, start, stop):
        ''' Method that runs from start to stop points, switching lights on
        On is represented by the number 1'''
        if start[0] <= stop[0] and start[1] <= stop[1]:
            for i in range (start[0], (stop[0] + 1)):
                for j in range (start[1], (stop[1] + 1)):
                    self.grid[i][j] = 1
    
    def turn_off(self, start, stop):
        ''' Method that runs from start to stop points, switching lights off
        On is represented by the number 0'''
        if start[0] <= stop[0] and start[1] <= stop[1]:
            for i in range (start[0], (stop[0] + 1)):
                for j in range (start[1], (stop[1] + 1)):
                    self.grid[i][j] = 0            
    
    def toggle(self, start, stop):
        ''' Method that runs from start to stop points, switching lights from on to off or off to on'''
        if start[0] <= stop[0] and start[1] <= stop[1]:
            for i in range (start[0], (stop[0] + 1)):
                for j in range (start[1], (stop[1] + 1)):
                    if self.grid[i][j] == 0:
                        self.grid[i][j] = 1
                    elif self.grid[i][j] == 1:
                        self.grid[i][j] = 0                
                        
    def count(self, gridSize):
        lights_on = 0
        for i in range (0, gridSize):
            for j in range (0, gridSize):
                if self.grid[i][j] == 1:
                    lights_on += 1
        return lights_on

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

sample = (file_clean('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt')[1])
startFirst = int(sample[1])
startLast = int(sample[2])
stopFirst = int(sample[3])
stopLast = int(sample[4])
print(sample)
print(startFirst)
print(startLast)
print(stopFirst)
print(stopLast)
coord = [startFirst, startLast]
print(coord)

def main():
    if len(sys.argv) < 3:
        print('Error: No input file provided')
    else:
        instruction = sys.argv[2]
        instructionString = file_existence(instruction)
        gridSize = int(instructionString.split('\n')[0])
        instructionClean = file_clean(instructionString)
        grid = LightTester(gridSize)
        
        for i in range (0, gridSize):
            
            if instructionClean[i][0] == 'turn on':
                pass 
            

if __name__ == '__main__':
    main()