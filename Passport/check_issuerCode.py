"""Validate the issuerCode of the passport"""
from check_string_of_digits import check_string_of_digits


def check_issuercode(issuercode: str) -> dict:
    """Validate string with series of passport
     :param issuercode: number of the passport
     :return: clean issuer code or dict with the details of error
     """
    clear_issuerCode: str = check_string_of_digits(issuercode)
    return clear_issuerCode if len(clear_issuerCode) == 6 \
        else {'Error': 'Invalid issuerCode'}


# print(check_issuercode("!@#@$#%$^YHGFVCVB1NJYUYTrert74er6ujhvcd876[]"))
