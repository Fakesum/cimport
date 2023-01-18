import os
import re
from .compile import compile_rs
from .program import RustProgram

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


def rustimport(filename):
    if (not os.path.exists(os.path.join("__pycache__/cimport", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/cimport/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        pre_processor(filename)
        compile_rs(filename)
    return RustProgram(f"__pycache__/cimport/{filename}.compiled")