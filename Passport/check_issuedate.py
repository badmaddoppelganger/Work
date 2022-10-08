"""Validate the issue date in passport"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
from check_date import check_date


def check_issuedate(issueDate: str) -> str or dict[str, str]:
    # Re-write function return annotation as "->  str | dict[str, str]" (work in Python 3.10+)
    """Convert birthday-string to datetime format
    :rtype: str or dict[str, str]
    :param issueDate:
    :return: birthdate in datetime format or dict with error details
    """
    clear_issuedate = check_date(issueDate)
    if clear_issuedate is True:
        return clear_issuedate
    if clear_issuedate <= datetime.strptime('1991-09-01', '%Y-%m-%d'):
        return {'Error': 'Date is too old'}
    return clear_issuedate if clear_issuedate <= datetime.now() \
        else {'Error': 'Date is in the future'}

# print(check_issuedate("1990-10-02"))
