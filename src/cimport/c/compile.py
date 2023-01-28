from ..command.linux import ConsoleLinux
from ..command.window import ConsoleWindow
from .program import CppProgram, CProgram
import os
import re

FunctionRegex = re.compile(r'.type([^,]+)')

def find_functions(filename):
    return [func.replace("\t", "") for func in FunctionRegex.findall(open(f"__pycache__/cimport/{filename}.s").read())]

def compile_c(filename, cpp, flags):
    compiler = ("g++" if cpp else "gcc")
    if os.name == "posix":
        console = ConsoleLinux()

        console.required_cmd("gcc")
        console.required_cmd("g++")
        console.required_cmd("cp")

        try:
            os.makedirs("__pycache__/cimport")
        except:
            pass
        

        console.run_cmd([compiler, "-c", "-fPIC", "-save-temps=obj", filename, *flags[1], "-o", f"__pycache__/cimport/{filename}.o"])

        console.require_file(f'__pycache__/cimport/{filename}.s')
        console.require_file(f'__pycache__/cimport/{filename}.o')

        console.run_cmd([compiler, f"__pycache__/cimport/{filename}.o", "-shared", "-o",f"__pycache__/cimport/{filename}.compiled"])

        console.require_file(f'__pycache__/cimport/{filename}.compiled')

        console.run_cmd(["rm", "-rf", f"__pycache__/cimport/{filename}.o"])
        console.run_cmd(["rm", "-rf", f"__pycache__/cimport/{filename}.ii"])
        console.run_cmd(["rm", "-rf", f"__pycache__/cimport/{filename}.i"])

        console.run_cmd(["cp", "-rf", filename, f"__pycache__/cimport/{filename}.ver"])
    
    else:
        raise NotImplementedError("Comming Soon, Sry") #TODO

    if cpp: 
        return CppProgram(f"__pycache__/cimport/{filename}.compiled", find_functions(filename))
    else:
        return CProgram(f"__pycache__/cimport/{filename}.compiled")