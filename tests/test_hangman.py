from pathlib import Path
from unittest.mock import mock_open

from hangman_cli.hangman import (
    _validate_input,
    build_guessed_word,
    get_player_input,
    join_guessed_letters,
    select_word,
)


def test_build_guessed_word():
    target_word = "hangman"
    guessed_letters = ["a", "n", "g"]
    expected_result = "_ a n g _ a n"
    assert build_guessed_word(target_word, guessed_letters) == expected_result  # noqa: F821


def test_get_player_input_with_valid_input(mocker):
    mocker.patch("builtins.input", return_value="h")
    guessed_letters = ["a", "n", "g"]
    assert get_player_input(guessed_letters) == 'h'


def test_get_player_input_with_invalid_input(mocker):
    mocker.patch("builtins.input", side_effect=['1', 'h'])
    guessed_letters = ["a", "n", "g"]
    assert get_player_input(guessed_letters) == 'h'


def test_get_player_input_with_previously_guessed_letter(mocker):
    mocker.patch("builtins.input", side_effect=['a', 'n', 'h'])
    guessed_letters = ["a", "n", "g"]
    assert get_player_input(guessed_letters) == 'h'


def test_join_guessed_letters():
    guessed_letters = ["a", "n", "g"]
    expected_result = "a g n"
    assert join_guessed_letters(guessed_letters) == expected_result


def test_join_guessed_letters_empty():
    guessed_letters = []
    expected_result = ""
    assert join_guessed_letters(guessed_letters) == expected_result


def test_join_guessed_letters_single():
    guessed_letters = ["a"]
    expected_result = "a"
    assert join_guessed_letters(guessed_letters) == expected_result


def test_select_word(mocker):
    m = mock_open(read_data="apple\nbanana\ncherry\n")
    mocker.patch.object(Path, 'open', new=m)
    word = select_word()
    assert word in ["apple", "banana", "cherry"]


def test_validate_input_when_new_letter():
    guessed_letters = ["a", "n", "g"]
    assert _validate_input("b", guessed_letters) is True


def test_validate_input_when_previously_guessed_letter():
    guessed_letters = ["a", "n", "g"]
    assert _validate_input("a", guessed_letters) is False


def test_validate_input_when_input_length_too_long():
    guessed_letters = ["a", "n", "g"]
    assert _validate_input("hm", guessed_letters) is False
    
    
def test_validate_input_when_input_is_numeric():
    guessed_letters = ["a", "n", "g"]
    assert _validate_input("1", guessed_letters) is False
    

def test_validate_input_when_input_is_non_alphabetic():
    guessed_letters = ["a", "n", "g"]    
    assert _validate_input("$", guessed_letters) is False
    