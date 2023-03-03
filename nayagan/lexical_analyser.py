from munch import Munch 
from rply import LexerGenerator

class LexicalAnalyser:

    ''' 
    lexical analyser class
    '''

    def __init__(self , tokens: Munch = None):

        '''
        create a lexer generator 
        token is a dictionary of tokens
        '''
        self._lg = LexerGenerator()
        self._tokens = tokens

    def add_tokens(self):

        '''
        add tokens to the lexer generator
        '''
        for token in self._tokens:
            self._lg.add(token, r"{}".format(self._tokens[token])) 

        self._lg.ignore(r'\s+')
        self._lg.ignore(r"!!.*\n") 

    def get_lexer(self):
        '''
        build the lexer and return it
        '''
        if self._tokens:
            self.add_tokens()
        else:
            self._lg = self._lg.ignore(r'\s+')
        return self._lg.build()