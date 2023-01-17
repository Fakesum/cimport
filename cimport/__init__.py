__version__ = "0.0.1b"
__name__ = "cimport"


import os
import pathlib
from .compile import compile_c, find_functions
from .program import Program

def import_program(filename: pathlib.Path | str, cpp=True, flags=[[], []]):
    if (not os.path.exists(os.path.join("__pycache__/cimport", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/cimport/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        return compile_c(filename, cpp, flags)
    
    return Program(f"__pycache__/cimport/{filename.split('.')[0]}.compiled", find_functions(filename))