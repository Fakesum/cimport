import os    
import pathlib
import re

FunctionRegex = re.compile(r'.type([^,]+)')


def import_program(filename: pathlib.Path | str, cpp=True, flags=[[], []]):
    if (not os.path.exists(os.path.join("__pycache__", f"""{filename.split(".")[0]}.s"""))) or (open(f"__pycache__/{filename.split('.')[0]}.ver").read() != open(filename).read()):
        return _compile_c(filename, cpp, flags)
    return _find_functions(filename)

def _find_functions(filename):
    return [func.replace("\t", "").replace("_Z", "")[0:-1] for func in FunctionRegex.findall(open(f"__pycache__/{filename.split('.')[0]}.s").read())]
