"""
Check the passport - only issue date and birthdate
Note - 20 and 45 years is the points of exchange passport
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta


def check_issued_on(date_of_birth: datetime, issued_on: datetime):
    """Note - 20 and 45 years is the points of exchange passport
    Check by count age (today - birthday) and issue date"""
    if issued_on > datetime.now() or date_of_birth > datetime.now() or date_of_birth > issued_on:
        return {'Error': 'Wrong date of issue or birthdate'}

    # If age < 20 years => stop the process
    if datetime.now() < date_of_birth + relativedelta(years=+20):
        return {'Error': False}

    # If issue date > 45 years => stop the process
    if  issued_on >= date_of_birth + relativedelta(years=+45):
        return {'Error': False}

    # If age > 20 check that issue date
    if date_of_birth+relativedelta(years=+45) > issued_on >= date_of_birth+relativedelta(years=+20)\
            and datetime.now() < date_of_birth + relativedelta(years=+45):
        return {'Error': False}

    return {'Error': 'Passport expired'}


date_of_birthday = datetime.strptime('1977-10-02T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
date_of_issued = datetime.strptime('2022-10-01T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
print(check_issued_on(date_of_birthday, date_of_issued))
