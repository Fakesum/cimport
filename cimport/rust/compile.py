from ..command.linux import ConsoleLinux
from ..command.window import ConsoleWindow
import os

def compile_rs(filename):
    if os.name == "posix":
        console = ConsoleLinux()

        console.required_cmd("rustc")
        console.required_cmd("gcc")

        if not (os.path.exists("__pycache__/cimport/")):
            os.makedirs("__pycache__/cimport/")

        console.run_cmd([
            f"rustc", 
            filename, 
            "-o",
            f"__pycache__/cimport/{filename.split('.')[0]}",
            "--emit=obj", "--emit=asm",
            "--crate-type=lib"
        ])
        
        filename = filename.split('.')[0]

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
            f"{filename}.rs",
            f"__pycache__/cimport/{filename}.ver"
        ])
    else:
        raise NotImplementedError("Comming Soon, Sry") #TODO