import ctypes
import typing
from fuzzywuzzy.fuzz import ratio as fuzz

THRESHOLD = 50

class Program(dict):
    def __init__(self, filename, func_names):
        self._program = ctypes.cdll.LoadLibrary(filename)
        self.names = func_names
        
        super().__init__()
    
    # def find_type(self, key, name):
    #     self.name
    
    def get(self, key):
        if (key != "names") and (key != "_program") and (key in self.__dict__):
            return self.__dict__[key]
        
        match = []
        for name in self.names:
            match_percentage = fuzz(name, key)
            if match_percentage > THRESHOLD:
                match.append([match_percentage, name])
        
        if match.__len__() != 0:
            name = max(match)[1]
            self.__dict__[key] = self._program.__getitem__(name)
            # self.find_type(key, name)
            return self.__dict__[key]
        else:    
            raise SyntaxError(f"Did not find value {key}")
    
    def __setattr__(self, __name: str, __value: typing.Any) -> None:
        self.__dict__[__name] = __value
            
    def __getattr__(self, key):
        return self.get(key)