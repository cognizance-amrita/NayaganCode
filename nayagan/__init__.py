import abstract_syntax_tree , lexical_analyser , parser , runner , helpers 

__all__ = ["abstract_syntax_tree" , "lexical_analyser" , "parser" , "runner" , "helpers"] 

__version__ = "0.0.1" 
__version_str__ = (
    f"nayagan version {__version__}."
    + "\n nayagan is a programming language which is a tribute to Andavar."
    + "\n Author: Rohith ND (ndrohith09@gmail.com)"
)

nayagan = runner.NayaganRunner()