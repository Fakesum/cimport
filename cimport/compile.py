from .command.linux import ConsoleLinux
from .command.window import ConsoleWindow
import os
import re

FunctionRegex = re.compile(r'.type([^,]+)')

def find_functions(filename):
    return [func.replace("\t", "").replace("_Z", "")[0:-1] for func in FunctionRegex.findall(open(f"__pycache__/{filename.split('.')[0]}.s").read())]

def compile_c(filename, cpp, flags):
    compiler = ("g++" if cpp else "gcc")
    if os.name == "posix":
        ConsoleLinux.required_cmd("gcc")
        ConsoleLinux.required_cmd("g++")
        ConsoleLinux.required_cmd("cp")

        if not os.path.exists("__pycache__"):
            os.makedirs("__pycache__")
        
        ConsoleLinux.run_cmd([compiler, "-S", "-o", f'__pycache__/{filename.split(".")[0]}.s', filename, *flags[0]])
        ConsoleLinux.run_cmd([compiler, *flags[1], "-o", f"__pycache__/{filename.split('.')[0]}"])
        
        ConsoleLinux.run_cmd(["cp", "-rf", filename, f"__pycache__/{filename.split('.')[0]}.ver"])
    
    else:
        raise NotImplementedError("Comming Soon, Sry")
    
    find_functions(filename)