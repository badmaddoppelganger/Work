import importlib

function_string = 'Passport.check_firstname.check_firstname'
mod_name, func_name = function_string.rsplit('.', 1)
mod = importlib.import_module(mod_name)
func = getattr(mod, func_name)
print(func)

