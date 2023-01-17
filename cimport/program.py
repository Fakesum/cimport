import re
import ctypes

class Program(dict):
    def __init__(self, filename, function_names):
        self._program = ctypes.LoadLibrary(filename)
        
        for func in function_names:
            self.__dict__[func] = exec(f"self._program.{func}")
        
        super().__init__()
        print(self.__dict__)
    
    def __getitem__(self, key):
        func_regex = re.compile(key)

        for val in self.__dict__.values():
            found_func = func_regex.findall(val)

            if found_func.__len__() == 0:
                raise SyntaxError("Function Not found")
        return [self.__dict__[func] for func in found_func]