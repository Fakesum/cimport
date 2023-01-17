import re
import ctypes

class Program(dict):
    def __init__(self, filename, func_names):
        self._program = ctypes.cdll.LoadLibrary(filename)
        self.names = func_names
        
        super().__init__()
    
    def get(self, key):
        if (key != "names") and (key != "_program") and (key in self.__dict__):
            return self.__dict__[key]
        
        func_regex = re.compile(key)

        for name in self.names:
            if func_regex.findall(name).__len__() == 1:
                res = self._program.__getitem__(name)
                self.__dict__[name] = res
                return res
        
        raise SyntaxError(f"Did not find function {key}")
            
    def __getattr__(self, key):
        self.get(key)