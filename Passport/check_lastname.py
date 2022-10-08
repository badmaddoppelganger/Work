"""Check the lastname (base-validate)"""
from check_cyrillic_string import check_string


def check_lastname(lastname: str) -> dict:
    """Validate lastname-string"""
    clear_lastname = check_string(lastname)
    return clear_lastname if clear_lastname is not None\
        else {'Error': 'Invalid lastname'}
