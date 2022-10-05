"""Validate the birthday in passport"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
from check_date import check_date


def check_birthday(birthday: str):
    """Convert birthday-string to datetime format"""
    clear_birthday = check_date(birthday)
    if type(clear_birthday) == dict:
        return clear_birthday
    if clear_birthday <= datetime.now() - relativedelta(years=+100):
        return {'Error': 'Date is too old'}
    return clear_birthday if clear_birthday <= datetime.now() - relativedelta(years=+14)\
        else {'Error': 'Date is too early'}


# print(check_birthday("2010-10-02"))
