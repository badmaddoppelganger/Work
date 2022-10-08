"""Local function to validate string with cyrillic symbols
Don't use regex because the hash-dict is the fastest and the simplest algorithm (O(1))
See the official docs about fullname attrs restriction in Russia"""


def check_string(string: str) -> str or None:
    # Re-write function return annotation as "->  str | None" (work in Python 3.10+)
    """Extract cyrillic symbols from the raw data
    (see the passport field restriction in Russia)
    :rtype: str or None
    :param string: raw string
    :return: all the cyrillic symbols as the string in lower case. Error handling incl.
    """
    alphabet = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь",
                "э", "ю", "я", "-", "."}
    clear_string = ''.join(filter(lambda el: el in alphabet, string.lower())) \
        .strip('.-').replace('--', '-')
    return clear_string if 64 >= len(clear_string) > 1 else None

# print(check_string('\"\'~!@@@#$%нефун--кциональныеи,,,her,,,-/.     '))
