import os    
import subprocess
import pathlib
import re

FunctionRegex = re.compile(r'.type([^,]+)')


def _is_cmd(cmd):
    return _run_cmd(['which', cmd]) != f"{cmd} not found"

def import_program(filename: pathlib.Path | str, cpp=True, flags=[[], []]):
    if (not os.path.exists(os.path.join("__pycache__", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        return _compile_c(filename, cpp, flags)
    return _find_functions(filename)

def _find_functions(filename):
    return [func.replace("\t", "").replace("_Z", "")[0:-1] for func in FunctionRegex.findall(open(f"__pycache__/{filename.split('.')[0]}.s").read())]

def _compile_c(filename, cpp, flags):
    compiler = ("g++" if cpp else "gcc")
    if os.name == "posix":
        _required_cmd("gcc")
        _required_cmd("g++")
        _required_cmd("cp")

        if not os.path.exists("__pycache__"):
            os.makedirs("__pycache__")
        
        _run_cmd([compiler, "-S", "-o", f'__pycache__/{filename.split(".")[0]}.s', filename, *flags[0]])
        _run_cmd([compiler, *flags[1], "-o", f"__pycache__/{filename.split('.')[0]}"])
        
        _run_cmd(["cp", "-rf", filename, f"__pycache__/{filename.split('.')[0]}.ver"])
    
    else:
        raise NotImplementedError("Comming Soon, Sry")
    
    return _find_functions(filename)