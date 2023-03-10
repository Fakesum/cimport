import os
import pathlib
from .compile import compile_c, find_functions
from .program import CppProgram, CProgram

from ..utils.cache_file import (
    get_file_path,
    check_tmp,
    make_temp_dir
)

# Function ot import a c/c++ file.
def c_import(filename: pathlib.Path | str, flags: tuple[list[str], list[str]]=[[], []]) -> CppProgram | CProgram:
    """
        Explination:
            This function imports function from any c/c++ file.
        Args:
            filename: Path | str, This is the location of the C/C++ file.
            flags: tuple[list[str], list[str]]=[[], []]), Any flags given to the compiler:
                gcc in case of linux and msvc in case of windows.
        
        Exceptions:
            raise FileNotFoundError: The filepath given could not be found. Remember that this is in
            relation to the main file at the moment
        
        Returns:
            CppProgram, in case of c++ file.
            CProgram, in case of pure c file.
    """

    if not (os.path.exists(filename)):
        raise FileNotFoundError(f"{filename} Not Found")
    
    make_temp_dir(filename)
    
    cpp: bool = filename.split(".")[1] in ['C','cpp', 'c++']
    if check_tmp(filename, ".s"):
        compile_c(filename, cpp, flags)
    
    if cpp: 
        return CppProgram(get_file_path(filename+".compiled"), find_functions(filename))
    elif filename.split(".")[1] == 'c':
        return CProgram(get_file_path(filename+".compiled"))