from ..utils.command.linux import ConsoleLinux
from ..utils.command.window import ConsoleWindow
from ..utils.cache_file import (
    create_version_file,
    get_file_path,
    clear_temp
)
import os
import re

FunctionRegex = re.compile(r'.type([^,]+)')

def find_functions(filename):
    return [func.replace("\t", "") for func in FunctionRegex.findall(open(get_file_path(filename+".s")).read())]

def compile_c(filename, cpp, flags):
    if os.name == "posix":
        compiler = ("g++" if cpp else "gcc")

        console = ConsoleLinux()

        console.required_cmd("g++") if cpp else console.required_cmd("gcc")
        console.required_cmd("cp")

        console.run_cmd([
            compiler,
            "-c",
            "-fPIC",
            "-save-temps=obj",
            filename,
            *flags[1],
            "-o",
            get_file_path(filename+".o")
        ])

        console.require_file(get_file_path(filename+".s"))
        console.require_file(get_file_path(filename+".o"))

        console.run_cmd([
            compiler,
            get_file_path(filename + ".o"),
            "-shared",
            "-o",
            get_file_path(filename + ".compiled")
        ])

        console.require_file(get_file_path(filename+".compiled"))

        clear_temp([
            filename+".o",
            filename+".ii",
            filename+".i"
        ])

    else:
        raise NotImplementedError("Comming Soon, Sry") #TODO
    
    create_version_file(filename)