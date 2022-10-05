"""Validate the issue date in passport"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
from check_date import check_date


def check_issuedate(issueDate: str):
    """Convert birthday-string to datetime format"""
    clear_issuedate = check_date(issueDate)
    if type(clear_issuedate) == dict:
        return clear_issuedate
    if clear_issuedate <= datetime.strptime('1991-09-01', '%Y-%m-%d'):
        return {'Error': 'Date is too old'}
    return clear_issuedate if clear_issuedate <= datetime.now() \
        else {'Error': 'Date is in the future'}

# print(check_issuedate("1990-10-02"))
