__all__ = ['speed_test']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['return_int', 'return_bool', 'return_string'])
@Js
def PyJsHoisted_return_int_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js(1.0)
PyJsHoisted_return_int_.func_name = 'return_int'
var.put('return_int', PyJsHoisted_return_int_)
@Js
def PyJsHoisted_return_bool_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js(True)
PyJsHoisted_return_bool_.func_name = 'return_bool'
var.put('return_bool', PyJsHoisted_return_bool_)
@Js
def PyJsHoisted_return_string_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js('String')
PyJsHoisted_return_string_.func_name = 'return_string'
var.put('return_string', PyJsHoisted_return_string_)
pass
pass
pass
pass


# Add lib to the module scope
speed_test = var.to_python()