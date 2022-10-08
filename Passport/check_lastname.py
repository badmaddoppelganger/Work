"""Check the lastname (base-validate)"""
from check_cyrillic_string import check_string


def check_lastname(lastname: str) -> str or dict[str, str]:
    # Re-write function return annotation as "->  str | dict[str, str]" (work in Python 3.10+)
    """Validate lastname-string by extracting from raw-data
    :rtype: str or dict[str, str]
    :param lastname: string with raw-data
    :return: clean lastname or dict with error details
    """
    clean_lastname = check_string(lastname)
    return clean_lastname if clean_lastname is not None\
        else {'Error': 'Invalid lastname'}
