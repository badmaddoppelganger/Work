"""Validate the series of the passport"""
from check_string_of_digits import check_string_of_digits


def check_series(series: str) -> str or dict[str, str]:
    # Re-write function return annotation as "->  str | dict[str, str]" (work in Python 3.10+)
    """Validate string with series of passport
    :rtype: str or dict[str, str]
    :param series: series of the passport
    :return : clean series or dict with the details of error
    """
    clean_series: str = check_string_of_digits(series)
    return clean_series if len(clean_series) == 4 \
        else {'Error': 'Invalid series'}


# print(check_series("!@#@$#%$^YHGFVCVB1NJY4UYTrert7er6ujhvcd6[]"))
