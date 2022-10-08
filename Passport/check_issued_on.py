"""
Check the passport - only issue date and birthdate
Note - 20 and 45 years is the points of exchange passport
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta


def check_issued_on(birthday: datetime, issued_on: datetime) -> bool or dict[str, str]:
    # Re-write function return annotation as "->  str | dict" (work in Python 3.10+)
    """Note - 20 and 45 years is the points of exchange passport
    Check by count age (today - birthday) and issue date
    :rtype: bool or dict[str, str]
    :param birthday: day of birthdate in the datetime format
    :param issued_on: day of issue in the datetime format
    :return: True or dict with error details"""
    first_exchange = birthday + relativedelta(years=+20)
    second_exchange = birthday + relativedelta(years=+45)
    if birthday > issued_on or issued_on < birthday + relativedelta(years=+14):
        return {'Error': 'Wrong date of issue or birthdate'}
    if datetime.now() < first_exchange:
        return True
    if issued_on >= second_exchange:
        return True
    if first_exchange <= issued_on < second_exchange \
            and datetime.now() < second_exchange:
        return True
    return {'Error': 'Passport expired'}

# print(check_issued_on(check_date('1988-10-26'), check_date('2015-10-23')))

# date_of_birthday = datetime.strptime('2002-10-03T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
# issue_date = datetime.strptime('2022-10-03T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
# print(check_issued_on(date_of_birthday, issue_date))
