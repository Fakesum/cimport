import js2py
from importlib.util import spec_from_file_location, module_from_spec
import os

class JsProgram:
    def __init__(self, filename, name) -> None:
        spec = spec_from_file_location(filename.split(".")[0], filename + ".py")
        self._program = module_from_spec(spec)
        spec.loader.exec_module(self._program)
    
    def get(self, name, *args):
        return eval(f"self._program.PyJsHoisted_{name}_")
    
    def __getattr__(self, __name):
        return self.get(__name)

def js_import(filename):
    if (not (os.path.exists(f"""__pycache__/cimport/{filename + ".py"}"""))) or (open("""""")):
        js2py.translate_file(filename, filename + ".py")

    return JsProgram(filename, filename.split(".")[0])