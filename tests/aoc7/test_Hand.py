from advent2023.aoc7.hand import Hand


def test_best_hand():
    hand1 = Hand("33J12", 1)
    hand2 = Hand("5J122", 1)
    assert hand1 < hand2