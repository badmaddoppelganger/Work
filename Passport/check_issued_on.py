"""
Check the passport - only issue date and birthdate
Note - 20 and 45 years is the points of exchange passport
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

def check_issued_on(birthday: datetime, issued_on: datetime) -> dict:
    """Note - 20 and 45 years is the points of exchange passport
    Check by count age (today - birthday) and issue date"""
    first_exchange = birthday + relativedelta(years=+20)
    second_exchange = birthday + relativedelta(years=+45)
    if issued_on > datetime.now() or birthday > datetime.now() \
            or birthday > issued_on or issued_on < birthday + relativedelta(years=+14):
        return {'Error': 'Wrong date of issue or birthdate'}
    if datetime.now() < first_exchange:
        return {'Error': False}
    if  issued_on >= second_exchange:
        return {'Error': False}
    if first_exchange <= issued_on < second_exchange\
            and datetime.now() < second_exchange:
        return {'Error': False}
    return {'Error': 'Passport expired'}

# print(check_issued_on(check_date('1988-10-26'), check_date('2015-10-23')))

#date_of_birthday = datetime.strptime('2002-10-03T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
#issue_date = datetime.strptime('2022-10-03T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
#print(check_issued_on(date_of_birthday, issue_date))
