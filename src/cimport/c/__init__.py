import os
import pathlib
from .compile import compile_c, find_functions
from .program import CppProgram, CProgram

def c_import(filename: pathlib.Path | str, flags=[[], []]):
    cpp = filename.split(".")[1] in ['C','cpp', 'c++']
    if (not os.path.exists(os.path.join("__pycache__/cimport", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/cimport/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        return compile_c(filename, cpp, flags)

    if cpp: 
        return CppProgram(f"__pycache__/cimport/{filename.split('.')[0]}.compiled", find_functions(filename))
    elif filename.split(".")[1] == 'c':
        return CProgram(f"__pycache__/cimport/{filename.split('.')[0]}.compiled")