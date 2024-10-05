import random as rnd
import string


def create_strings_from_file(filename: str, count: int) -> list[str]:
    """
    Create all strings by reading lines in specified files
    """
    strings = []
    with open(filename, "r", encoding="utf8") as f:
        lines = [l[0:200] for l in f.read().splitlines() if len(l) > 0]
        if len(lines) == 0:
            raise Exception("No lines could be read in file")
        while len(strings) < count:
            if len(lines) >= count - len(strings):
                strings.extend(lines[0: count - len(strings)])
            else:
                strings.extend(lines)
    return strings


def create_strings_from_dict(length: int, allow_variable: bool, count: int, lang_dict: list[str]) -> list[str]:
    """
    Create all strings by picking X random word in the dictionary
    """
    dict_len = len(lang_dict)
    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, rnd.randint(1, length) if allow_variable else length):
            current_string += lang_dict[rnd.randrange(dict_len)]
            current_string += " "
        strings.append(current_string[:-1])
    return strings


def create_strings_randomly(length: int, allow_variable: bool, count: int, let: bool, num: bool, sym: bool,
                            lang: str) -> list[str]:
    """
    Create all strings by randomly sampling from a pool of characters.
    """
    # If none specified, use all three
    if True not in (let, num, sym):
        let, num, sym = True, True, True

    pool = ""
    if let:
        if lang == "cn":
            pool += "".join([chr(i) for i in range(19968, 40908)])  # Unicode range of CHK characters
        elif lang == "ja":
            pool += "".join([chr(i) for i in range(12288, 12351)])  # unicode range for japanese-style punctuation
            pool += "".join([chr(i) for i in range(12352, 12447)])  # unicode range for Hiragana
            pool += "".join([chr(i) for i in range(12448, 12543)])  # unicode range for Katakana
            pool += "".join([chr(i) for i in range(65280,
                                                   65519)])  # unicode range for Full-width roman characters and half-width katakana
            pool += "".join([chr(i) for i in range(19968, 40908)])  # unicode range for common and uncommon kanji
            # https://stackoverflow.com/questions/19899554/unicode-range-for-japanese
        else:
            pool += string.ascii_letters
    if num:
        pool += "0123456789"
    if sym:
        pool += "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~"

    if lang == "cn":
        min_seq_len = 1
        max_seq_len = 2
    elif lang == "ja":
        min_seq_len = 1
        max_seq_len = 2
    else:
        min_seq_len = 2
        max_seq_len = 10

    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, rnd.randint(1, length) if allow_variable else length):
            seq_len = rnd.randint(min_seq_len, max_seq_len)
            current_string += "".join([rnd.choice(pool) for _ in range(seq_len)])
            current_string += " "
        strings.append(current_string[:-1])
    return strings
