#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Encoding: UTF-8

# import modules
import sys, getopt, os

# import modules from file modules.py
from modules import onError, usage, videoTypes

from videoInfo import videoInfo
from pathlib import Path
from pprint import pprint as pp

# import external modules

# handle options and arguments passed to script
try:
    myopts, args = getopt.getopt(sys.argv[1:],
                                 'p:vh',
                                 ['path=', 'verbose', 'help'])

except getopt.GetoptError as e:
    onError(1, str(e))

# if no options passed, then exit
if len(sys.argv) == 1:  # no options passed
    onError(2, "No options given")
    
path = Path.cwd()
verbose = False
    
# interpret options and arguments
for option, argument in myopts:
    if option in ('-p', '--path'):
        path = argument
    elif option in ('-v', '--verbose'):  # verbose output
        verbose = True
    elif option in ('-h', '--help'):  # display help text
        usage(0)

if verbose:
    print("\nSearching '{}' ...".format(path))
    
pathObject = Path(path)

for item in pathObject.iterdir():
    
    if verbose:
        print("Checking if video file ...")
        
    if Path(item).is_file():
        if Path(item).is_symlink():
            if verbose:
                print("Not a file")
        else:
            print("\n{}".format(item))
            
            file_name, file_extension = os.path.splitext(item)
    
            if verbose:
                print("Extension: {}".format(file_extension))
                
                print("Getting media info ...")
            
            videoInfo(path, item, verbose)
    else:
        if verbose:
            print("Not a file")
    