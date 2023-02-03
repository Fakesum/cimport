import js2py
import os
from importlib.util import spec_from_file_location, module_from_spec
from ..utils.cache_file import (
    check_tmp,
    get_file_path,
    make_temp_dir
)

class JsProgram:
    def __init__(self, filename) -> None:
        spec = spec_from_file_location(filename.split(".")[0], filename)
        self._program = module_from_spec(spec)
        spec.loader.exec_module(self._program)
    
    def get(self, name, *args):
        return eval(f"self._program.PyJsHoisted_{name}_")
    
    def __getattr__(self, __name):
        return self.get(__name)

def js_import(filename):
    if not(os.path.exists(filename)):
        raise FileNotFoundError(f"{filename} Not Found")

    make_temp_dir(filename)
    
    if check_tmp(filename, ".py"):
        js2py.translate_file(filename, get_file_path(filename+".py"))

    return JsProgram(get_file_path(filename + ".py"))