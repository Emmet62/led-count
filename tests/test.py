# Testing for ledcheck.main

from ledcheck.main import *


def test_file_existence():
    ''' Checks that the input file exists'''
    test_file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    assert file_existence(test_file) != None

def test_file_content():
    ''' Reads the first 36 characters from the file and checks that this matches the characters I have'''
    test_file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    assert file_existence(test_file)[:36] == "1000\nturn off 660,55 through 986,197" 

def test_boundaries():
    ''' Need to write a test that will check that the coordinates are within the boundaries of the grid
    If they aren't, they should be changed'''
    test_grid = LightTester(1000)
    test_coordinates = test_grid.boundaries([0, 1099], [-2, 230])
    assert test_coordinates == ([0, 999],[0, 230])

def test_turn_on():
    pass

def test_turn_off():
    pass

def test_toggle():
    pass