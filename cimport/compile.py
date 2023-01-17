from .command.linux import ConsoleLinux
from .command.window import ConsoleWindow
from .program import Program
import os
import re

FunctionRegex = re.compile(r'.type([^,]+)')

def find_functions(filename):
    return [func.replace("\t", "") for func in FunctionRegex.findall(open(f"__pycache__/{filename.split('.')[0]}.s").read())]

def compile_c(filename, cpp, flags):
    compiler = ("g++" if cpp else "gcc")
    if os.name == "posix":
        console = ConsoleLinux()

        console.required_cmd("gcc")
        console.required_cmd("g++")
        console.required_cmd("cp")

        if not os.path.exists("__pycache__"):
            os.makedirs("__pycache__")
        
        console.run_cmd([compiler, "-S", "-o", f'__pycache__/{filename.split(".")[0]}.s', filename, *flags[0]])
        console.run_cmd([compiler, *flags[1], "-o", f"__pycache__/{filename.split('.')[0]}"])
        
        console.run_cmd(["cp", "-rf", filename, f"__pycache__/{filename.split('.')[0]}.ver"])
    
    else:
        raise NotImplementedError("Comming Soon, Sry") #TODO
    
    return Program(filename.split('.')[0], find_functions(filename))