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
        if start[1] < 0:
            start[1] = 0
        if stop[0] >= self.size:
            stop[0] = (self.size - 1)
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
        Off is represented by the number 0'''
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
        ''' Method that iterates through the multidimensional array and counts the number of lights on'''
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

def get_coord(string):
    ''' Reads a string and returns coordinates as integers in a list'''
    First = int(string[0])
    Last = int(string[1])
    coord = [First, Last]
    return coord

def main():
    ''' Checks that command is in required format'''
    if len(sys.argv) < 3:
        print('Error: Please check the parameters\nCommand should be of form: "ledcheck --input file_link"')
    else:
        link = sys.argv[2]
        file = file_existence(link)
        gridSize = int(file.split("\n")[0]) # get the grid size from the first line of file
        cleanFile = re.findall(r".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", file) 
        commandNumber = len(cleanFile) # get the number of commands
        print("Grid Size:", gridSize)
        print("No. of Commands:", commandNumber)
        grid = LightTester(gridSize) # create an instance of class LightTester
        
        ''' for loop that iterates through each element in the list
        The RegEx used above returns the input file as a list of lists
        Each inner list is in the form ('turn off', '660', '55', '986', '197'), etc.
        We can index into each inner list and then index into the specific elements in it'''
        for i in range (0, commandNumber):
            start = get_coord(cleanFile[i][1:3]) # start coordinates are at index 1 and 2
            stop = get_coord(cleanFile[i][3:]) # stop coordinates are at index 3 and 4
            boundedStart, boundedStop = grid.boundaries(start, stop) # ensures that start/stop coordinates are within boundaries of grid
            
            ''' Depending on the command (turn on, turn off, toggle), the necessary method is called'''
            if cleanFile[i][0] == 'turn on':
                grid.turn_on(boundedStart, boundedStop)
            elif cleanFile[i][0] == 'turn off':
                grid.turn_off(boundedStart, boundedStop)
            elif cleanFile[i][0] == 'switch':
                grid.toggle(boundedStart, boundedStop)
        
        ''' Call the count method and print the results'''    
        print("No. of Lights On:", grid.count(gridSize))

if __name__ == '__main__':
    main()