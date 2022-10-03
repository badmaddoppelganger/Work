"""Check and validate the passport"""
import importlib


# function_string = 'mypackage.mymodule.myfunc'
# mod_name, func_name = function_string.rsplit('.',1)
# mod = importlib.import_module(mod_name)
# func = getattr(mod, func_name)
# result = func()

def check_passport(fields: dict) -> dict:
    answer_lst = []
    if len(fields) > 0:
        for key, value in fields.items():
            func = getattr(importlib.import_module("check_" + key), "check_" + key)
            answer_lst.append(func(value))
        return print(answer_lst)


check_passport({'number': '46876', 'firstname': '@#%$Пи--лин-т23345%$#@', 'lastname': '@#%$Агрегатор Плюс23345%$#@',
                'middlename': '@#$Самолет'})
