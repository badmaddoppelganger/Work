"""Check the firstname (base-validate)"""
from check_string_with_cyrillic import check_string


def check_firstname(firstname: str) -> dict:
    """Validate firstname-string"""
    clear_firstname = check_string(firstname)
    return {'firstname': clear_firstname} if clear_firstname is not None \
        else {'Error': 'Invalid firstname'}


# print(check_firstname('\"\'~!@@@#$%нефун--кциональныеи,,,her,,,-/.     '))
