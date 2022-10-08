"""Check the firstname (base-validate)"""
from check_cyrillic_string import check_string


def check_firstname(firstname: str) -> str or dict[str, str]:
    # Re-write as "str | dict[str, str]" (work in Python 3.10+)
    """Validate firstname-string by extracting from raw-data
    :rtype: str or dict[str, str]
    :param firstname: string with raw-data
    :return: clean firstname or dict with error details
    """
    clear_firstname = check_string(firstname)
    return clear_firstname if clear_firstname is not None \
        else {'Error': 'Invalid firstname'}


# print(check_firstname('\"\'~!@@@#$%нефун--кциональныеи,,,her,,,-/.     '))
