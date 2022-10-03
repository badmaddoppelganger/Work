"""Local function to extract digits from the string"""


def check_string_of_digits(string: str) -> str:
    """Extract digits from the string and return as the string"""
    clear_string = (''.join(el for el in string if el.isdigit()))
    return clear_string if len(clear_string) > 1 else None


# check_digits("!@#@$#%$^YHGFVCVBNJYUYTrert76554er6ujhvcd876[]")
