import os

cimport_temp_path = "__pycache__/cimport/"

def check_version_file(filename):
    ver_file = cimport_temp_path + filename + ".ver"
    if not os.path.exists(ver_file):
        return False
    return open(filename).read() == open(ver_file).read()

def create_version_file(filename):
    filename = cimport_temp_path + filename+".ver"
    open(filename, "w+").write(open(filename).read())
    return filename

def get_file_path(filename):
    return cimport_temp_path + filename