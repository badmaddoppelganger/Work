"""Check and validate the passport"""
import importlib
from check_issued_on import check_issued_on
from check_passport_dadata import is_valid
from check_passport_dadata import fill_issued_by


# function_string = 'mypackage.mymodule.myfunc'
# mod_name, func_name = function_string.rsplit('.',1)
# mod = importlib.import_module(mod_name)
# func = getattr(mod, func_name)
# result = func()

def check_passport(fields: dict) -> dict:
    """
    Can be used to validate and check all the fields in the passport
    :rtype: dict
    :param fields: all the attrs of the passport:
            'birthday':   str
            'issuedate':  str
            'series':     str
            'number':     str
            'firstname':  str
            'lastname':   str
            'middlename': str
            'issuerCode': str
    :return: all the fields after validation|check
    """
    results = {}
    for key, value in fields.items():
        func = getattr(importlib.import_module("check_" + key), "check_" + key.lower())
        results |= {key: (func(value))}
    return results


print(check_passport({'birthday': '1988-10-26',
                      'issuedate': '10-23-2015',
                      'series': '2ad7@vf15[]"',
                      'number': '585sewf0--20',
                      'firstname': '@#alisher#@',
                      'lastname': '@#%$Агрегатор Плюс23345%$#@',
                      'middlename': '@#$Самолет',
                      'issuerCode': '390-02wdfc1'}))

""""Some code to be released next
    if not isinstance(results['birthday'], dict) and not isinstance(results['issuedate'], dict):
        is_expired = check_issued_on(results['birthday'], results['issuedate'])
        results |= {'Not expired': is_expired}
    if isinstance(results['number'], str) and isinstance(results['series'], str):
        is_valid_passport = is_valid(results['series'] + results['number'])
        results |= {'Passport is valid': is_valid_passport}
    if 'issuerCode' in results and isinstance(results['issuerCode'], str):
        results |= {'issued_by_value': fill_issued_by(results['issuerCode'])}"""