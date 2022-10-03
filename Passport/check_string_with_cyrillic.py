"""Local function to validate string"""


def check_string(string: str) -> str:
    """Base-validation of cyrillic-like string"""
    alphabet = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь",
                "э", "ю", "я", "-", "."}
    clear_string = (''.join(el.lower() for el in string if el.lower() in alphabet)) \
        .strip('.-').replace('--', '-')
    return clear_string if len(clear_string) > 1 else None

# print(check_string('\"\'~!@@@#$%нефун--кциональныеи,,,her,,,-/.     '))
