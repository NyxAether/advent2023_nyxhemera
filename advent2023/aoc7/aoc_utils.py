from advent2023.aoc7.hand import Hand


def rank_hands(hands: list[Hand]) -> int:
    sorted_hands = sorted(hands)
    total_score = 0
    for i, hand in enumerate(sorted_hands):
        total_score += (i + 1) * hand.bid
    return total_score
