from advent2023.aoc7.hand import Hand


def test_best_hand():
    hands = []
    hands.append(Hand("32T3K", 1))
    hands.append(Hand("T55J5", 1))
    hands.append(Hand("KK677", 1))
    hands.append(Hand("KTJJT", 1))
    hands.append(Hand("QQQJA", 1))
    assert hands[0] < hands[3]
    assert hands[3] < hands[2]
    assert hands[2] < hands[1]
    assert hands[1] < hands[4]
    for h in hands:
        h.joker = True
    assert hands[0] < hands[2]
    assert hands[2] < hands[1]
    assert hands[1] < hands[4]
    assert hands[4] < hands[3]
