"""Check the firstname (base-validate)"""
from check_cyrillic_string import check_string


def check_firstname(firstname: str) -> dict:
    """Validate firstname-string"""
    return {'firstname': check_string(firstname)} if check_string(firstname) is not None \
        else {'Error': 'Invalid firstname'}


# print(check_firstname('\"\'~!@@@#$%нефун--кциональныеи,,,her,,,-/.     '))
