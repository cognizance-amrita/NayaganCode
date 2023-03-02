from .base import Node 

'''
Create a class for unary operations and inherit from the base class Node
'''

class UnaryOperation(Node):
    def __init__(self , value ):
        super().__init__() 
        self.value = value 

class UnarySum(UnaryOperation):
    # def __init__(self , value ):
    #     super().__init__(value) 
    
    def eval(self):
        return float(self.value.eval()) 

class UnarySub(UnaryOperation):
    # def __init__(self, value):
    #     super().__init__(value) 

    def eval(self):
        return float(-self.value.eval())
    
'''
Create a class for unary operations and inherit from the base class Node
'''

class BinaryOperation(Node):
    def __init__(self , left , right ):
        super().__init__() 
        self.left = left 
        self.right = right 

class Sum(BinaryOperation):

    def eval(self):
        return float(self.left.eval()) + float(self.right.eval())

class Sub(BinaryOperation):

    def eval(self):
        return float(self.left.eval()) - float(self.right.eval())

class Mul(BinaryOperation): 
    
    def eval(self):
        return float(self.left.eval()) * float(self.right.eval())


class Div(BinaryOperation): 
    
    def eval(self):
        return float(self.left.eval()) / float(self.right.eval())
    

class Mode(BinaryOperation): 
    
    def eval(self):
        return float(self.left.eval()) % float(self.right.eval())
    
class Power(BinaryOperation):

    def eval(self):
        return float(self.left.eval()) ** float(self.right.eval()) 
    
class FloorDiv(BinaryOperation): 

    def eval(self):
        return float(self.left.eval()) // float(self.right.eval()) 
    
''' 
Logical Operations
'''

class GreaterThan(BinaryOperation): 

    def eval(self):
        return float(self.left.eval()) > float(self.right.eval())
    
class GreaterThanEqual(BinaryOperation):

    def eval(self):
        return float(self.left.eval()) >= float(self.right.eval())
    
class LessThan(BinaryOperation): 

    def eval(self):
        return float(self.left.eval()) < float(self.right.eval())
    
class LessThanEqual(BinaryOperation):

    def eval(self):
        return float(self.left.eval()) <= float(self.right.eval()) 
    
class Equal(BinaryOperation):
    
    def eval(self):
        return float(self.left.eval()) == float(self.right.eval()) 
    
class NotEqual(BinaryOperation):

    def eval(self):
        return float(self.left.eval()) != float(self.right.eval()) 

# TODO: implement the operations

class And(BinaryOperation):

    def eval(self):
        return float(self.left.eval()) and float(self.right.eval()) 

class Or(BinaryOperation): 

    def eval(self):
        return float(self.left.eval()) or float(self.right.eval())
    
class Not(BinaryOperation):

    def eval(self):
        return not float(self.left.eval()) 
