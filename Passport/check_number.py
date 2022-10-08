"""Validate the number of the passport"""
from check_string_of_digits import check_string_of_digits


def check_number(number: str) -> str or dict[str, str]:
    # Re-write function return annotation as "->  str | dict[str, str]" (work in Python 3.10+)
    """Validate string with series of passport
    :rtype: str or dict[str, str]
    :param number: number of the passport
    :return: clean number or dict with the details of error
    """
    clean_number: str = check_string_of_digits(number)
    return clean_number if len(clean_number) == 6 \
        else {'Error': 'Invalid number'}

# print(check_number("!@#@$#%$^YHGFVCVB1NJYUYTrert74er6ujhvcd876[]"))
