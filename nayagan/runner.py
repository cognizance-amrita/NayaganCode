'''
# nayagan python runner 
The nayagan python runner is a python script that runs the nayagan python module.
It is used to run the nayagan python module from the command line.

It exposes the nayagan runner to nayagan interpreter.
'''

import os 
import sys
import warnings 
from pathlib import Path

from loguru import logger
from .helpers import read_yaml
from .lexical_analyser import LexicalAnalyser

class NayaganRunner:
    '''
    The nayagan runner handles the execution of nayagan code
    '''

    def __init__(self):
        
        yml_path = os.path.join(Path(__file__).parent, "token.yml")
        self.tokens_dict = read_yaml(yml_path)

    def init_parser(self ):
        pass 

    def eval(self):
        pass 

    def tokenize(self):
        pass

    def exec(self):
        pass 

    def eval(self):
        pass 
