from ..command.linux import ConsoleLinux
from ..command.window import ConsoleWindow
from .program import RustProgram
import os
import re

FunctionRegex = re.compile(r'.type([^,]+)')

def find_function(filename):
    return [func.replace("\t", "") for func in FunctionRegex.findall(open(f"__pycache__/cimport/{filename}.s").read())]

def pre_processor(filename):
    file = open(filename, "rw")
    lines = file.readlines()

    for line in enumerate(lines):
        if (line.count("fn") == 1) and (not (lines[line[0]-1] != "#[no_mangle]")):
            lines.insert(line[0]-1, "#[no_mangle]")
    
    if lines != file.readlines():
        print("Modifying File, since no_mangle is required for function to be accessable")
        file.write("\n".join(lines))

def compile_rs(filename):
    if os.name == "posix":
        console = ConsoleLinux()

        console.required_cmd("rustc")
        console.required_cmd("gcc")

        console.run_cmd([
            f"rustc", 
            filename, 
            "-o",
            f"__pycache__/cimport/{filename}",
            "--emit=obj", "--emit=asm",
            "--crate-type=lib"
        ])

        console.require_file(f"__pycache__/cimport/{filename}.o")
        console.require_file(f"__pycache__/cimport/{filename}.s")

        console.run_cmd([
            f"gcc",
            f"__pycache__/cimport/{filename}.o",
            "-shared",
            "-o",
            f"__pycache__/cimport/{filename}.compiled"    
        ])

        console.require_file(f"__pycache__/cimport/{filename}.compiled")

        console.run_cmd([
            "rm",
            "-rf",
            f"__pycache__/cimport/{filename}.o",
        ])

        console.run_cmd([
            "cp",
            "-rf",
            filename,
            f"__pycache__/cimport/{filename}.ver"
        ])
    else:
        raise NotImplementedError("Comming Soon, Sry") #TODO
    
    return RustProgram(f"__pycache__/cimport/{filename}.compiled")