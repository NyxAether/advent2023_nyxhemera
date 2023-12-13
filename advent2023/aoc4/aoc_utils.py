def score(win: list[set[int]], values: list[set[int]]) -> int:
    total_score = 0
    for w, v in zip(win, values):
        if len(w & v) != 0:
            total_score += 2 ** (len(w & v) - 1)
    return total_score


def wins_per_card(win: list[set[int]], values: list[set[int]]) -> list[int]:
    return [len(w & v) for w, v in zip(win, values)]


def total_cards(win: list[set[int]], values: list[set[int]]) -> int:
    wins_per_cards = wins_per_card(win, values)
    nbcards = [0] * len(wins_per_cards)
    for i in range(len(wins_per_cards) - 1, -1, -1):
        nbcards[i] = wins_per_cards[i] + sum(nbcards[i + 1 : i + wins_per_cards[i] + 1])
    nbcards = [x + 1 for x in nbcards]
    return sum(nbcards)
