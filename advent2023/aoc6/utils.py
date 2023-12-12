import numpy as np


def wins_product(times: list[int], distances: list[int]) -> int:
    total = 1
    for t, d in zip(times, distances):
        total *= count_wins(t, d)
    return total


def count_wins(time: int, best_distance: int) -> int:
    press_time = np.arange(time + 1)
    return ((time - press_time) * press_time > best_distance).sum()
