
class JsProgram:
    def __init__(self, program) -> None:
        self._program = program
    
    def get(name, *args):
        return eval(f"self._program.{name}")

def js_import(filename):
    import js2py
    import importlib
    js2py.translate_file(filename, filename + ".js")

    return JsProgram(importlib.import_module(filename + ".js"))