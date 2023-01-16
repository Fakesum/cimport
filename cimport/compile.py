def compile_c(filename, cpp, flags):
    compiler = ("g++" if cpp else "gcc")
    if os.name == "posix":
        from .linux import
        _required_cmd("gcc")
        _required_cmd("g++")
        _required_cmd("cp")

        if not os.path.exists("__pycache__"):
            os.makedirs("__pycache__")
        
        _run_cmd([compiler, "-S", "-o", f'__pycache__/{filename.split(".")[0]}.s', filename, *flags[0]])
        _run_cmd([compiler, *flags[1], "-o", f"__pycache__/{filename.split('.')[0]}"])
        
        _run_cmd(["cp", "-rf", filename, f"__pycache__/{filename.split('.')[0]}.ver"])
    
    else:
        raise NotImplementedError("Comming Soon, Sry")