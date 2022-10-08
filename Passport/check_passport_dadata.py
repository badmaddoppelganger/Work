"""Check the passport:
 1. func(is_valid) check the passport in Ministry of internal Affairs of Russia
 2. func(fill_issued_by) - return the fullname of the passport's issuer by issuer code
 3. func(normalize_address) - normalize the raw-address
Warning: save you config by using some tools like 'https://pypi.org/project/dynaconf/' or similar"""

from dadata import Dadata

TOKEN = "9b23dbd41e5f143094a94ff6d1ae204b7e702fae"
SECRET = "a380afa548e2b3c9ce3e4a23fddbba02ccaaf337"


def is_valid(passport_value: str) -> bool:
    """qc-key means quality check in the Dadata service
    where '0' is Valid option and '10' is Invalid.
    Warning: False-answer must be checked manually, see more details in the link below
             https://dadata.ru/api/clean/passport/
    :rtype: bool
    :param passport_value: string-concatenation of passport's number and series
    :return: status as the boolean expression"""
    dadata = Dadata(TOKEN, SECRET)
    result: int = (dadata.clean("passport", passport_value))['qc']
    return result == 0


def fill_issued_by(issuer_code: str) -> str:
    """Convert issuer code to the fullname of the passport's issuer
    Can work with the raw-data (like '390-021') but highly recommended to pre-processing value:
            please check the 'Passport/check_string_of_digits.py/check_string_of_digits'
    :rtype: str
    :param issuer_code: string issuer code from the passport
    :return: the raw_name only but contains more details in the dict(see details-link below)
             https://dadata.ru/api/suggest/fms_unit/"""
    dadata = Dadata(TOKEN)
    result: str = dadata.suggest("fms_unit", issuer_code)[0]['value']
    return result


def address_normalize(address: str) -> dict:
    """Return the raw address after the normalization process and the address
     as the object (dict-type)
     :rtype: dict
     :param address: string which contains raw-address
     :return: dict that contains the raw address after the normalization process
              and the address as the object (see details-link below)
              Details: https://dadata.ru/api/clean/address/"""
    dadata = Dadata(TOKEN, SECRET)
    result: dict = {'normalized_address_raw_string': dadata.clean("address", address)['result'],
                    'normalized_address_object': dadata.clean("address", address)}
    return result

# print(address_normalize('sukhonskaya'))
# print(fill_issued_by('390021'))
# print(is_valid('2715585020'))
