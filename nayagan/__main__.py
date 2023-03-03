import sys 
from loguru import logger 
from typer import Typer 
from __init__ import __version__, __version_str__, nayagan

app = Typer()

@app.command()
def version():
    '''
    prints the version of nayagan
    '''
    logger.info(__version_str__)
    print(__version_str__)

@app.command()
def tokenize(file_path:str):
    '''
    print the tokens of the input file
    '''

    logger.remove()
    logger.add(sys.stderr, level="ERROR")
    with open(file_path, "r") as f:
        code = f.read() 

    tokens = nayagan.tokenize(code = code)
    for token in tokens:
        print(token)

@app.command()
def run(file_path :str , debug: bool = False):
    '''
    runs the nayagan code from the input file 
    '''
    logger.remove()
    if debug:
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.add(sys.stderr, level="ERROR")
    with open(file_path, "r") as f:
        code = f.read()

    nayagan.exec(code = code)

@app.command()
def shell():
    print(f"nayagan v{__version__}")
    while True:
        code_line = input("nayagan>> ")
        output = nayagan.eval(code_line)
        if output is not None:
            print(output)


@app.callback()
def main():
    '''
    nayagan is a programming language which is a tribute to Andavar.
    Author: Rohith ND (ndrohith09#gmail.com)
    '''


if __name__ == "__main__":
    app()
