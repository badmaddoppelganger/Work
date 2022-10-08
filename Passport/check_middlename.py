"""Check the middlename (base-validate)"""
from check_cyrillic_string import check_string


def check_middlename(middlename: str) -> str or dict[str, str]:
    # Re-write function return annotation as "->  str | dict[str, str]" (work in Python 3.10+)
    """Validate middlename-string by extracting from raw-data
    :rtype: str or dict[str, str]
    :param middlename: string with raw-data
    :return: clean middlename or dict with error details
    """
    clean_middlename = check_string(middlename)
    return clean_middlename if clean_middlename is not None \
        else {'Error': 'Invalid middlename'}
