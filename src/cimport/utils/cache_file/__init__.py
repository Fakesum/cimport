import os
import pathlib
import sys

cimport_temp_path = "__pycache__/cimport/"

def check_version_file(filename):
    file = pathlib.Path(filename)
    ver_file = os.path.join(file.parent.absolute().__str__(), cimport_temp_path, file.name+ ".ver")

    if not os.path.exists(ver_file):
        return True
    return open(file.absolute().__str__()).read() != open(ver_file).read()

def create_version_file(filename):
    file = pathlib.Path(filename)
    ver_file = os.path.join(file.parent.absolute().__str__(), cimport_temp_path, file.name+ ".ver")
    open(ver_file, "w+").write(open(file.absolute().__str__()).read())

def get_file_path(filename):
    file = pathlib.Path(filename)
    return os.path.join(file.parent.absolute().__str__(), cimport_temp_path, file.name)

def make_temp_dir(filename):
    file = pathlib.Path(filename)
    try:
        os.makedirs(os.path.join(file.parent.absolute().__str__(), cimport_temp_path))
    except OSError as e:
        pass

def check_tmp(filename, ext):
    file = pathlib.Path(filename)

    if (not os.path.exists(os.path.join(file.parent.absolute().__str__(), cimport_temp_path, file.name+ ext))) or check_version_file(filename):
        create_version_file(filename)
        return True
    
    return False

def clear_temp(files):
    for file in files:
        file = pathlib.Path(file)
        try:
            os.remove(os.path.join(file.parent.absolute().__str__(), cimport_temp_path, file.name))
        except OSError as e:
            pass