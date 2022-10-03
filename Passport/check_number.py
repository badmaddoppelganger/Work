"""Validate the number of the passport"""
from check_string_of_digits import check_string_of_digits


def check_number(number: str) -> dict:
    """Validate firstname-string"""
    clear_number = check_string_of_digits(number)
    return {'number': clear_number} if len(clear_number) == 6 \
        else {'Error': 'Invalid number'}


# print(check_number("!@#@$#%$^YHGFVCVB1NJYUYTrert74er6ujhvcd876[]"))
