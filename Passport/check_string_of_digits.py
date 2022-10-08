"""Custom function to extract digits from any string"""


def check_string_of_digits(string: str) -> str:
    """Extract digits from the raw data
    (see the passport field restriction in Russia)
    :param string: raw string which contains digits to be extracted
    :return: all the digits converted to the string
    """
    return ''.join(filter(lambda el: el.isdigit(), string))

# print(check_string_of_digits("!@#@$#%$^YHGFVCVBNJYUYTrert76554er6ujhvcd876[]"))
