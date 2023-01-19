import ctypes

class RustProgram:
    def __init__(self, filename):
        self._program = ctypes.cdll.LoadLibrary(filename)
    
    def get(self, name):
        return self._program.__getitem__(name)
    
    def __getattr__(self, __name: str):
        return self.get(__name)