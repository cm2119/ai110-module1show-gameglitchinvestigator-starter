from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"



def test_parse_guess_valid_integer():
    # A plain integer string parses successfully to its int value
    assert parse_guess("42") == (True, 42, None)

def test_parse_guess_decimal_truncates():
    # A decimal string is accepted and truncated toward zero
    assert parse_guess("3.7") == (True, 3, None)

def test_parse_guess_not_a_number():
    # Non-numeric input fails with the expected error message
    assert parse_guess("abc") == (False, None, "That is not a number.")



def test_get_range_for_difficulty_easy():
    # Easy difficulty uses the 1-20 range
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_get_range_for_difficulty_unknown_defaults():
    # An unrecognized difficulty falls back to the default 1-100 range
    assert get_range_for_difficulty("Whatever") == (1, 100)


def test_update_score_too_low_subtracts():
    # A "Too Low" outcome subtracts 5 from the current score
    assert update_score(20, "Too Low", 3) == 15
