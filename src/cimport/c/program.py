import ctypes
import typing

THRESHOLD = 50

class CppProgram(dict):
    def __init__(self, filename, func_names: list[str]):
        self._program = ctypes.cdll.LoadLibrary(filename)
        self.names: list[str] = func_names
        
        super().__init__()
        
    def get(self, key, res_type = ctypes.c_int, arg_type = []):
        if (key != "names") and (key != "_program") and (key in self.__dict__):
            return self.__dict__[key]
        
        for name in self.names:
            f_name = name.replace("_Z", "").lstrip("0123456789")
            if (f_name.__len__() > key.__len__()) and (f_name[:key.__len__()] == key):
                self.__dict__[key] = self._program.__getitem__(name)
                types = f_name.replace(key, "")
                self.__dict__[key].argtypes = []

                if arg_type == []:
                    for _type in types:
                        if _type == "i":
                            self.__dict__[key].argtypes.append(ctypes.c_int)
                        elif _type == "f":
                            self.__dict__[key].argtypes.append(ctypes.c_float)
                        elif _type == "c":
                            self.__dict__[key].argtypes.append(ctypes.c_char)
                
                self.__dict__[key].argtypes = tuple(self.__dict__[key].argtypes) if arg_type == [] else arg_type
                self.__dict__[key].restype = res_type
        
                return self.__dict__[key]
    def __getattr__(self, key):
        return self.get(key)

    def restype(self, key, _type):
        self.__dict__[key].restype = _type

class CProgram:
    def __init__(self, filename):
        self._program = ctypes.cdll.LoadLibrary(filename)
    
    def get(self, name, _type = ctypes.c_int, arg_type = []):
        func = self._program.__getitem__(name)
        
        func.restype = _type
        func.argtypes = arg_type
        
        setattr(self, name, func)
        return func
    
    def __getattr__(self, __name: str):
        return self.get(__name)