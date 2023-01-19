import os
import pathlib
from .compile import compile_c, find_functions
from .program import CppProgram, CProgram

def c_import(filename: pathlib.Path | str, flags=[[], []]):
    cpp = filename.split(".")[1] in ['C','cpp', 'c++']
    print("[DEBUG] Importing")
    if (not os.path.exists(f"""__pycache__/cimport/{filename}.s""")) or (open(f"__pycache__/cimport/{filename}.ver").read() != open(filename).read()):
        print("[DEBUG] Compiling")
        return compile_c(filename, cpp, flags)
    
    print("[DEBUG] geting functions.")

    if cpp: 
        return CppProgram(f"__pycache__/cimport/{filename}.compiled", find_functions(filename))
    elif filename.split(".")[1] == 'c':
        return CProgram(f"__pycache__/cimport/{filename}.compiled")