"""Validate the series of the passport"""
from check_string_of_digits import check_string_of_digits


def check_series(series: str) -> dict:
    """Validate string with series of passport"""
    clear_series = check_string_of_digits(series)
    return {'series': clear_series} if len(clear_series) == 4 \
        else {'Error': 'Invalid series'}


# print(clear_series("!@#@$#%$^YHGFVCVB1NJYUYTrert74er6ujhvcd876[]"))
