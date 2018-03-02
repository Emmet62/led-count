ledcheck
===============================

version number: 0.0.1
author: Emmet Tracey

Overview
--------

Counts the number of LED lights that are on

Installation 
--------------------

To install use pip:

    $ pip install ledcheck


Or clone the repo:

    $ git clone https://github.com/Emmet62/ledcheck.git
    $ python setup.py install
    
Usage
------------

To use please enter the following command:
    
    $ ledcheck --input 'file_link'
    
file_link can be either a local saved file or a network address

Description
-----------------

ledcheck can be ran as a command line argument. It reads the
first line of the input file to retrieve the size of the grid.
It then reads each subsequent line of the input file and 
executes the command on the respective coordinates. Once the 
commands have all been executed it counts the number of LED 
lights that are on
