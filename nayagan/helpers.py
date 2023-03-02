import yaml 
from munch import DefaultMunch 

__vars__ = {}
__functions__ = {}

def read_yml(path: str) -> DefaultMunch:
    '''
    read a yaml file and return a munch object
    '''
    with open(path, "r") as f:
        yml = yaml.safe_load(f)
    return DefaultMunch.fromDict(yml)