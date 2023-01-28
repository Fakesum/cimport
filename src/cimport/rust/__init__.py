import os
from .compile import compile_rs
from ..c.program import CProgram

def pre_processor(filename):
    lines: list[str] = open(filename, "r+").read().split("\n")
    n_file = ""

    for line in lines:
        if line.startswith("fn") and ((lines.index(line) == 0) or (lines[lines.index(line)-1] != "#[no_mangle]")):
            n_file += "#[no_mangle]\n"
        n_file += line + ("\n" if line != "\n" else "")
    n_file = n_file[:-1]
    
    open(filename, "w+").write(n_file)

def rust_import(filename):
    if (not os.path.exists(os.path.join("__pycache__/cimport", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/cimport/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        pre_processor(filename)
        compile_rs(filename)
    return CProgram(f"__pycache__/cimport/{filename.split('.')[0]}.compiled")