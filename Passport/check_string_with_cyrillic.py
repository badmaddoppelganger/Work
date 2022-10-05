"""Local function to validate string with cyrillic symbols"""


def check_string(string: str) -> str:
    """Base-validation and extract symbols from cyrillic-like string"""
    alphabet = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь",
                "э", "ю", "я", "-", "."}
    clear_string = ''.join(filter(lambda el: el in alphabet, string.lower())) \
        .strip('.-').replace('--', '-')
    return clear_string if len(clear_string) > 1 else None


# print(check_string('\"\'~!@@@#$%нефун--кциональныеи,,,her,,,-/.     '))
