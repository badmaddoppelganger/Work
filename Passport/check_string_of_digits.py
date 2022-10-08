"""Custom function to extract digits from any string"""


def check_string_of_digits(string: str) -> str:
    """Extract digits from the raw data
    (see the passport field restriction in Russia)
    :rtype: str
    :param string: raw string
    :return: all the digits as the string.
    """
    return ''.join(filter(lambda el: el.isdigit(), string))

# print(check_string_of_digits("!@#@$#%$^YHGFVCVBNJYUYTrert76554er6ujhvcd876[]"))
