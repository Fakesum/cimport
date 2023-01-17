__version__ = "0.0.1a"
__name__ = "cimport"


import os
import pathlib
from .compile import compile_c, find_functions
from .program import Program

def import_program(filename: pathlib.Path | str, cpp=True, flags=[[], []]):
    if (not os.path.exists(os.path.join("__pycache__", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        return compile_c(filename, cpp, flags)
    
    return Program(filename.split('.')[0], find_functions(filename))