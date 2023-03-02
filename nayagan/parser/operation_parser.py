from ..abstract_syntax_tree.operations import (
    Div,
    LessThan,
    LessThanEqual,
    GreaterThan,
    GreaterThanEqual, 
    Equal,
    NotEqual,
    Power,
    Mod,
    FloorDiv,
    Mul,
    Sub,
    Sum,
    And,
    Or, 
    Not
)


class BinaryMathOperationsParser:
    def parse(self, pg):
        @pg.production("mathop : SUM")
        def binary_sum(p):
            return Sum

        @pg.production("mathop : SUB")
        def binary_sub(p):
            return Sub

        @pg.production("mathop : MUL")
        def binary_mul(p):
            return Mul

        @pg.production("mathop : DIV")
        def binary_div(p):
            return Div

        @pg.production("mathop : MOD")
        def binary_mod(p):
            return Mod
        
        # Todo: Add support 
        @pg.production("mathop : POW")
        def binary_pow(p):
            return Power
        
        @pg.production("mathop : FLRDIV")
        def binary_floor_div(p):
            return FloorDiv

#todo : change to compare operations
class BinaryLogicalOperationsParser:
# class BinaryComparisonOperationsParser:
    def parse(self, pg):
        @pg.production("logicalop : GT")
        def binary_gt(p):
            return GreaterThan

        @pg.production("logicalop : GTE")
        def binary_gte(p):
            return GreaterThanEqual

        @pg.production("logicalop : LT")
        def binary_lt(p):
            return LessThan

        @pg.production("logicalop : LTE")
        def binary_lte(p):
            return LessThanEqual

        @pg.production("logicalop : EQ")
        def binary_eq(p):
            return Equal

        @pg.production("logicalop : NEQ")
        def binary_neq(p):
            return NotEqual


# TODO: implement the operations 
class BinaryLogicalOperationsParser:
# class BinaryComparisonOperationsParser:
    def parse(self, pg):        

        @pg.production("logicalop : AND")
        def binary_and(p):
            return And
        
        @pg.production("logicalop : OR")
        def binary_or(p):
            return Or
        
        @pg.production("logicalop : NOT")
        def binary_not(p):
            return Not
        
#todo : change to bitwise operations