from ..utils.command.linux import ConsoleLinux
from ..utils.command.window import ConsoleWindow
from ..utils.cache_file import get_file_path, clear_temp

import os

def compile_rs(filename):
    if os.name == "posix":
        console = ConsoleLinux()

        console.required_cmd("rustc")
        console.required_cmd("gcc")

        console.run_cmd([
            f"rustc", 
            filename, 
            "-o",
            get_file_path(filename.split(".")[0]),
            "--emit=obj", "--emit=asm",
            "--crate-type=lib"
        ])

        filename = filename.split(".")[0]
        
        console.require_file(get_file_path(f"{filename}.o"))
        console.require_file(get_file_path(f"{filename}.s"))

        console.run_cmd([
            f"gcc",
            get_file_path(f"{filename}.o"),
            "-shared",
            "-o",
            get_file_path(f"{filename}.compiled")
        ])

        console.require_file(get_file_path(f"{filename}.compiled"))

        clear_temp([
            get_file_path(f"{filename}.o")
        ])

    else:
        raise NotImplementedError("Comming Soon, Sry") #TODO