from tests.flow.flo import Flo
def test_quitter():
    Flo.test("tests/flow/quitter.txt")

def test_wanna_play_then_quit():
    Flo.test("tests/flow/bank_one_roll_then_quit.txt")

def test_bank_first_for_two_round():
    Flo.test("tests/flow/bank_first_for_two_rounds.txt")

def test_zilch():
    Flo.test("tests/flow/zilch.txt")
def test_cheat_and_fix():
    Flo.test("tests/flow/cheat_and_fix.txt")

def test_hot_dice():
    Flo.test("tests/flow/hot_dice.txt")
