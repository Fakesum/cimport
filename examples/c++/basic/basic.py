import time
from cimport import c_import

st = time.time()
basic_program = c_import("basic.cpp")
print(time.time() - st)

basic_program.basicFunction()