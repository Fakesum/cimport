import time
from threading import Thread
from cimport import c_import, rust_import, js_import
import ctypes

def timeit(f):
    st = time.time()
    return (f(), time.time() - st) 

def run_test(program, command: str, _type = ctypes.c_int, arg_type = []):
    res = timeit(lambda: program.get(command, _type, arg_type)())
    print("took", res[1], "Seconds to run", command, "returned", res[0])

def c_test():
    c_program = timeit(lambda: c_import("speed_test.c"))
    print("took", c_program[1], "seconds to load c program")

    c_program = c_program[0]

    run_test(c_program, "return_int")
    run_test(c_program, "return_float")
    run_test(c_program, "return_double")
    run_test(c_program, "return_string", ctypes.c_char_p)

def cpp_test():
    cpp_program = timeit(lambda: c_import("speed_test.cpp"))
    print("took", cpp_program[1], "seconds to load c++ program")

    cpp_program = cpp_program[0]

    run_test(cpp_program, "return_int")
    run_test(cpp_program, "return_float")
    run_test(cpp_program, "return_double")
    run_test(cpp_program, "return_string", ctypes.c_char_p)

def rust_test():
    rust_program = timeit(lambda: rust_import("speed_test.rs"))
    print("took", rust_program[1], "seconds to load rust program")

    rust_program = rust_program[0]

    run_test(rust_program, "return_int")
    run_test(rust_program, "return_float")
    run_test(rust_program, "return_string", ctypes.c_char_p)

def js_test():
    js_program = timeit(lambda: js_import("speed_test.js"))
    print("took", js_program[1], "seconds to load rust program")

    js_program = js_program[0]

    run_test(js_program, "return_bool")
    run_test(js_program, "return_int")
    run_test(js_program, "return_string")


TESTS = [
    c_test,
    cpp_test,
    rust_test,
    js_test
]

if __name__ == "__main__":
    for test in TESTS:
        Thread(target=test).start()