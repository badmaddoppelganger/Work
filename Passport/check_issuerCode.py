"""Validate the issuerCode of the passport"""
from check_string_of_digits import check_string_of_digits


def check_issuercode(issuercode: str) -> dict:
    """Validate string with issuerCode of passport"""
    clear_issuerCode = check_string_of_digits(issuercode)
    return {'issuerCode': clear_issuerCode} if len(clear_issuerCode) == 6 \
        else {'Error': 'Invalid issuerCode'}


# print(check_issuerCode("!@#@$#%$^YHGFVCVB1NJYUYTrert74er6ujhvcd876[]"))
