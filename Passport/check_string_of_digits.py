"""Local function to extract digits from the string"""


def check_string_of_digits(string: str) -> str:
    """Extract digits from the string and return as the string"""
    clear_string = ''.join(filter(lambda el: el.isdigit(), string))
    return clear_string if len(clear_string) > 3 else None

# print(check_string_of_digits("!@#@$#%$^YHGFVCVBNJYUYTrert76554er6ujhvcd876[]"))
