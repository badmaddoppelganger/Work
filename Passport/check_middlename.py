"""Check the middlename (base-validate)"""
from check_string_with_cyrillic import check_string


def check_middlename(middlename: str) -> dict:
    """Validate middlename-string"""
    clear_middlename = check_string(middlename)
    return {'middlename': clear_middlename} if clear_middlename is not None \
        else {'Error': 'Invalid middlename'}
