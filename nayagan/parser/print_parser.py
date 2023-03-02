from loguru import logger

from ..abstract_syntax_tree.blocks import PrintBlock

class PrintParser:
    
    '''
    Parser all print expressions.
    '''

    def parse(self, pg):
        @pg.production(
            "printexprs : printexprs expression", precedence="NOOP"
        )
        def print_expression(p):
            logger.debug("Parser --> print_exprs")
            return PrintBlock(p[0], p[1])

        @pg.production("printexprs : ")
        def print_expression_empty(p):
            logger.debug("Parser --> print_empty")
            return PrintBlock()
