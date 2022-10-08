"""Validate the series of the passport"""
from check_string_of_digits import check_string_of_digits


def check_series(series: str) -> str:
    """Validate string with series of passport
    :param series: series of the passport
    :return: clean series or dict with the details of error
    """
    clear_series: str = check_string_of_digits(series)
    return clear_series if len(clear_series) == 4 \
        else {'Error': 'Invalid series'}


# print(check_series("!@#@$#%$^YHGFVCVB1NJY4UYTrert7er6ujhvcd6[]"))
