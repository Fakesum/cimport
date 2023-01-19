from cimport import c_import

basic_program = c_import("basic.cpp")
basic_program.basicFunction()