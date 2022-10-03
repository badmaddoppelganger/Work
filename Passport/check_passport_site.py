"""
Check the passport - only issue date and birthdate
Note - 20 and 45 years is the points of exchange passport
"""

from datetime import datetime

from dateutil.relativedelta import relativedelta


def check_issued_on(birthday: datetime, issued_on: datetime, sign_date: datetime = None) -> dict:
    """Note - 20 and 45 years is the points of exchange passport
    Check by count age (today - birthday) and issue date"""
    first_exchange = birthday + relativedelta(years=+20)
    second_exchange = birthday + relativedelta(years=+45)
    min_days_limit = relativedelta(days=+30)
    if issued_on > datetime.now() or birthday > datetime.now() \
            or birthday > issued_on or issued_on < birthday + relativedelta(years=+14):
        return {'Error': 'Wrong date of issue or birthdate'}
    if datetime.now() < first_exchange:
        return warning_case(first_exchange, sign_date, min_days_limit)
    if issued_on >= second_exchange:
        return {'Error': False}
    if first_exchange <= issued_on < second_exchange and datetime.now() < second_exchange:
        return warning_case(second_exchange, sign_date, min_days_limit)
    return {'Error': 'Passport expired'}


def warning_case(passport_change_date: datetime, sign_date: datetime,
                 min_days_limit: relativedelta) -> dict:
    """Return warning about passport details if we have too few days before date of deal"""
    return_body = {}
    if datetime.now() > passport_change_date - min_days_limit:
        return_body |= {'Warning_contact': f'{passport_change_date - datetime.now()}'
                                           f' hours before passport expires'}
        if sign_date > passport_change_date - min_days_limit and sign_date > datetime.now():
            return_body |= {'Warning_deal': f'{sign_date - datetime.now()}'
                                            f' hours before date of sign'}
    return_body |= {'Error': False}
    return return_body


# date_of_birthday = datetime.strptime('2002-10-05T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
# issue_date = datetime.strptime('2020-10-01T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
# signing_date = datetime.strptime('2022-10-15T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')

# print(check_issued_on(date_of_birthday, issue_date, signing_date))
