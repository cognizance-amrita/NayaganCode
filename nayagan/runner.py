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
from helpers import read_yml
from lexical_analyser import LexicalAnalyser
from parser.main import ProgramParser , LineParser , ParserBase

class NayaganRunner:
    '''
    The nayagan runner handles the execution of nayagan code
    '''

    def __init__(self):
        
        yml_path = os.path.join(Path(__file__).parent, "token.yml")
        self.tokens_dict = read_yml(yml_path)

        self.__pgm_parser = self.init_parser(ProgramParser)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            logger.warning("LineParser supports only a few nayagan features")
            self.__line_parser = self.init_parser(LineParser) 

    def init_parser(self , Parser : ParserBase):
        parser = Parser(list(self.tokens_dict.keys()))
        parser.parse()
        return parser.get_parser()

    def __eval(self , parser , code):
        parsed_tokens  = parser.parse(self.tokenize(code))
        return parsed_tokens.eval()

    def tokenize(self , code:str):
        ''''
        tokenizes the input code
        return : a generator of tokens 
        '''
        lexical_analyser = LexicalAnalyser(self.tokens_dict).get_lexer()
        tokens = lexical_analyser.lex(code)
        return tokens

    def exec(self , code , log : str="INFO"):
        '''
        executes the nayagan code 
        args :
            code : the nayagan code to be executed 
            log : Defaults to "ERROR"
        '''
        logger.remove() 
        logger.add(sys.stderr, level=log)
        self.__eval(self.__pgm_parser , code)

    def eval(self, code_line:str):
        '''
        evaluates the nayagan code
        only nayagan features are supported
        returns : _type_ -> output of evaluation
        '''
        
        logger.remove()
        logger.add(sys.stderr, level="ERROR") 
        return self.__eval(self.__line_parser , code_line)


