"""Check the lastname (base-validate)"""
from check_string_with_cyrillic import check_string


def check_lastname(lastname: str) -> dict:
    """Validate lastname-string"""
    clear_lastname = check_string(lastname)
    return {'lastname': clear_lastname} if clear_lastname is not None \
        else {'Error': 'Invalid lastname'}
