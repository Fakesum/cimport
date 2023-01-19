import time
from threading import Thread
from cimport import c_import

def timeit(f):
    st = time.time()
    return (f(), time.time() - st)

def c_test():
    c_program = timeit(lambda: c_import("speed_test.c"))
    print("took", c_program[0], "seconds to load c program")

def cpp_test():
    cpp_program = timeit(lambda: c_import("speed_test.cpp"))
    print("took", cpp_program[0], "seconds to load c++ program")

def rust_test():
    rust_program = timeit(lambda: c_import("speed_test.rs"))
    print("took", rust_program[0], "seconds to load rust program")

TESTS = [
    c_test,
    cpp_test,
    rust_test
]

if __name__ == "__main__":
    for test in TESTS:
        Thread(target=test).start()