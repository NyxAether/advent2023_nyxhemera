import numpy as np


def wins_product(times: list[int], distances: list[int]) -> int:
    total = 1
    for t, d in zip(times, distances):
        total *= count_wins(t, d)
    return total


def count_wins(time: int, best_distance: int) -> int:
    # Cast is necessary on windows
    press_time = np.arange(time + 1).astype('int64')
    return (((time - press_time) * press_time) > best_distance).sum()
