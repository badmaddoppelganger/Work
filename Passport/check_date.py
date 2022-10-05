"""Check any string and convert into the datetime format"""
from dateutil import parser


def check_date(date: str):
    """Try to parse date from string or return Error message"""
    if len(date) < 10:
        return {'Error': f'ParserError(Unknown string format: %s, {date})'}
    try:
        dt_obj = parser.parse(date)
    except parser.ParserError as parser_error:
        dt_obj = {"Error": parser_error}
    return dt_obj


# print(check_date('1921-10-10'))
