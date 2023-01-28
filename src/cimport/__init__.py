__version__ = "0.1.0c"
__name__ = "cimport"

from .c import c_import
from .rust import rust_import
from .c.program import CppProgram, CProgram