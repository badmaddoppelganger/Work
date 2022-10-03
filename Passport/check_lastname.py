"""Check the lastname (base-validate)"""
from check_cyrillic_string import check_string


def check_lastname(lastname: str) -> dict:
    """Validate lastname-string"""
    return {'lastname': check_string(lastname)} if check_string(lastname) is not None \
        else {'Error': 'Invalid lastname'}
