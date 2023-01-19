import ctypes
import typing
# from fuzzywuzzy.fuzz import ratio as fuzz

THRESHOLD = 50

class CppProgram(dict):
    def __init__(self, filename, func_names: list[str]):
        self._program = ctypes.cdll.LoadLibrary(filename)
        self.names: list[str] = func_names
        
        super().__init__()
        
    def get(self, key):
        if (key != "names") and (key != "_program") and (key in self.__dict__):
            return self.__dict__[key]
        
        for name in self.names:
            f_name = name.replace("_Z", "").lstrip("0123456789")
            if (f_name.__len__() > key.__len__()) and (f_name[:key.__len__()] == key):
                self.__dict__[key] = self._program.__getitem__(name)
                types = f_name.replace(key, "")
                self.__dict__[key].argtypes = []

                for _type in types:
                    if _type == "i":
                        self.__dict__[key].argtypes.append(ctypes.c_int)
                    elif _type == "f":
                        self.__dict__[key].argtypes.append(ctypes.c_float)
                    elif _type == "c":
                        self.__dict__[key].argtypes.append(ctypes.c_char)
                    
                self.__dict__[key].argtypes = tuple(self.__dict__[key].argtypes)
        
                return self.__dict__[key]
    def __setattr__(self, __name: str, __value: typing.Any) -> None:
        self.__dict__[__name] = __value
            
    def __getattr__(self, key):
        return self.get(key)
    
    def restype(self, key, _type):
        self.__dict__[key].restype = _type

class CProgram:
    def __init__(self, filename):
        self._program = ctypes.cdll.LoadLibrary(filename)
    
    def get(self, name):
        return self._program.__getitem__(name)
    
    def __getattr__(self, __name: str):
        return self.get(__name)
    
    def restype(self, key, _type):
        self._program.__getitem__(key).restype = _type