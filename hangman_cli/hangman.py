import string
from pathlib import Path
from random import choice


def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)


def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input


def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))


def select_word():
    with Path("words.txt").open() as words:
        word_list = words.readlines()
    return choice(word_list).strip()


def _validate_input(player_input, guessed_letters):
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )