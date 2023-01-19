from cimport import c_import

parameter_test = c_import("parameters.cpp")

print(parameter_test.parameters_test(4))