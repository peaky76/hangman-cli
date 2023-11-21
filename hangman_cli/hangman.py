from pathlib import Path
from random import choice


def select_word():
    with Path("words.txt").open() as words:
        word_list = words.readlines()
    return choice(word_list).strip()