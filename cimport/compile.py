from .command.linux import ConsoleLinux
from .command.window import ConsoleWindow
from .program import Program
import os
import re

FunctionRegex = re.compile(r'.type([^,]+)')

def find_functions(filename):
    return [func.replace("\t", "") for func in FunctionRegex.findall(open(f"__pycache__/cimport/{filename.split('.')[0]}.s").read())]

def require_file(filename):
    if not os.path.exists(filename):
        raise RuntimeError("File Does not exsit")

def compile_c(filename, cpp, flags):
    compiler = ("g++" if cpp else "gcc")
    if os.name == "posix":
        console = ConsoleLinux()

        console.required_cmd("gcc")
        console.required_cmd("g++")
        console.required_cmd("cp")

        if not os.path.exists("__pycache__/cimport"):
            os.makedirs("__pycache__/cimport")
        
        console.run_cmd([compiler, "-S", "-o", f'__pycache__/cimport/{filename.split(".")[0]}.s', filename, *flags[0]])
        require_file(f'__pycache__/cimport/{filename.split(".")[0]}.s')

        console.run_cmd([compiler, "-c", "-fPIC",filename, *flags[1], "-o", f"__pycache__/cimport/{filename.split('.')[0]}.o"])
        require_file(f'__pycache__/cimport/{filename.split(".")[0]}.o')

        console.run_cmd([compiler, f"__pycache__/cimport/{filename.split('.')[0]}.o", "-shared", "-o",f"__pycache__/cimport/{filename.split('.')[0]}.compiled"])
        require_file(f'__pycache__/cimport/{filename.split(".")[0]}.compiled')

        console.run_cmd(["rm", "-rf", f"__pycache__/cimport/{filename.split('.')[0]}.o"])

        console.run_cmd(["cp", "-rf", filename, f"__pycache__/cimport/{filename.split('.')[0]}.ver"])
    
    else:
        raise NotImplementedError("Comming Soon, Sry") #TODO
    
    return Program(f"__pycache__/cimport/{filename.split('.')[0]}.compiled", find_functions(filename))