from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message or "lower" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message or "higher" in message



#AI pytest
def test_guess_too_high_detailed():
    # Test that when guess is too high, we get the correct outcome and hint
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert "LOWER" in message or "lower" in message

def test_guess_too_low_detailed():
    # Test that when guess is too low, we get the correct outcome and hint
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message or "higher" in message