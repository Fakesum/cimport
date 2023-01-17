import cimport

program = cimport.import_program("find_name.cpp")
print(program["printf"]("hello"))