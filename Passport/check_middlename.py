"""Check the middlename (base-validate)"""
from check_cyrillic_string import check_string


def check_middlename(middlename: str) -> dict:
    """Validate middlename-string"""
    return {'middlename': check_string(middlename)} if check_string(middlename) is not None \
        else {'Error': 'Invalid middlename'}
