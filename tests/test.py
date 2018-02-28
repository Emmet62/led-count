# Testing for ledcheck.main

from ledcheck.main import *


def test_file_existence():
    test_file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    assert file_existence(test_file) != None

def test_file_format():
    ''' Reads the first 35 characters from the file and checks that this matches the characters I have manually added'''
    test_file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    assert file_format("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")[:4] == "1000" #\nturn off 660,55 through 986,197"

def test_boundaries():
    pass

def test_turn_on():
    pass

def test_turn_off():
    pass

def test_toggle():
    pass