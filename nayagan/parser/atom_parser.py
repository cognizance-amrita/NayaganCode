from loguru import logger

from abstract_syntax_tree.base import Boolean, Number, String, Word
from abstract_syntax_tree.control import FuncWord


class AtomParser:
    """
    Parser all atomic expressions.
    Atomic expressions are:
        - Numbers
        - Strings 
        - Words 
        - Booleans
    """

    def parse(self, pg):
        @pg.production("forvar : NUMBER")
        @pg.production("expression : NUMBER")
        def number_expression(p):
            logger.debug("Parser --> number")
            return Number(p[0].value)

        @pg.production("expression : BOOL_TRUE")
        @pg.production("expression : BOOL_FALSE")
        def bool_expression(p):
            return Boolean(p[0])

        @pg.production("expression : STRING")
        def string_expression(p):
            logger.debug("Parser --> string")
            return String(p[0].value)

        @pg.production("forvar : WORD")
        @pg.production("expression : WORD")
        @pg.production("variable : WORD")
        def word_expression(p):
            return Word(p[0])

        @pg.production("func_name : WORD")
        def func_word(p):
            return FuncWord(p[0])
