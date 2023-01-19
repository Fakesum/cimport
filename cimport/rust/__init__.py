import os
from .compile import compile_rs
from .program import RustProgram

def pre_processor(filename):
    lines = open(filename, "r+").readlines()

    for line in enumerate(lines):
        if (line[1].count("fn") > 0) and (lines[line[0]-1] != "#[no_mangle]"):
            lines.insert((line[0]-1 if line[0] != 0 else 0), "#[no_mangle]")
    
    if lines != open(filename, "w+").readlines():
        print("Modifying File, since no_mangle is required for function to be accessable")
        open(filename, "w+").write("\n".join(lines))


def rust_import(filename):
    if (not os.path.exists(os.path.join("__pycache__/cimport", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/cimport/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        pre_processor(filename)
        compile_rs(filename)
    return RustProgram(f"__pycache__/cimport/{filename.split('.')[0]}.compiled")