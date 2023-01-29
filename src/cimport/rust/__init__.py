import os
from .compile import compile_rs
from ..c.program import CProgram

from ..utils.cache_file import (
    cimport_temp_path,
    create_version_file,
    check_version_file,
    make_temp_dir,
    get_file_path
)

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
    make_temp_dir()
    if (not os.path.exists(cimport_temp_path + filename.split(".")[0] + ".s")) or check_version_file(filename):
        create_version_file(filename)
        pre_processor(filename)
        compile_rs(filename)
    
    filename = filename.split(".")[0]
    return CProgram(get_file_path(f"{filename}.compiled"))