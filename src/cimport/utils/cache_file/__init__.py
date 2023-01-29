import os

cimport_temp_path = "__pycache__/cimport/"

def check_version_file(filename):
    ver_file = cimport_temp_path + filename + ".ver"
    if not os.path.exists(ver_file):
        return True
    return open(filename).read() != open(ver_file).read()

def create_version_file(filename):
    ver_file = cimport_temp_path + filename + ".ver"
    open(ver_file, "w+").write(open(filename).read())

def get_file_path(filename):
    return cimport_temp_path + filename

def make_temp_dir():
    try:
        os.makedirs(cimport_temp_path)
    except OSError as e:
        pass

def check_tmp(filename, ext, split=False):
    if (not os.path.exists(cimport_temp_path + filename + ext)) or check_version_file(filename):
        create_version_file(filename)
        return True
    
    return False

def clear_temp(files):
    for file in files:
        try:
            os.remove(cimport_temp_path + file)
        except OSError as e:
            pass