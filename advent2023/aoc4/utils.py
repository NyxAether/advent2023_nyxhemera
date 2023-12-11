def score(win: list[set[int]], values: list[set[int]]) -> int:
    total_score = 0
    for w, v in zip(win, values):
        if len(w & v) != 0:
            total_score += 2 ** (len(w & v) - 1)
    return total_score
