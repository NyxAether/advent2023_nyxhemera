import numpy as np
from utils import get_characters_table, get_lines
from aoc1.utils import extract_first_last_digit, transform_text_digits_to_digits
from aoc2.utils import extract_game, max_product, possible_max
from aoc3.utils import digit_pos, isolate_digits, neighbors_symb, symbole_pos


if __name__ == "__main__":
    INPUT_1_PATH = "data/input1.txt"
    INPUT_2_PATH = "data/input2.txt"
    lines = get_lines(INPUT_1_PATH)

    # Problem 1-1
    res_1 = sum([extract_first_last_digit(line) for line in lines])
    print(f"Solution 1-1: {res_1}")

    # Problem 1-2
    res_2 = sum(
        [
            extract_first_last_digit(transform_text_digits_to_digits(line))
            for line in lines
        ]
    )
    print(f"Solution 1-2: {res_2}")

    # AOC 2
    INPUT_2_PATH = "data/input2.txt"
    lines = get_lines(INPUT_2_PATH)

    # Problem 2-1
    games = [possible_max(extract_game(line)) for line in lines]
    print(f"Solution 2-1: {sum([game for game in games if game is not None])}")

    # Problem 2-2
    games = [max_product(extract_game(line)) for line in lines]
    print(f"Solution 2-2: {sum(games)}")

    # AOC 3
    INPUT_3_PATH = "data/input3.txt"

    # Problem 3-1
    characters = get_characters_table(INPUT_3_PATH)
    test = isolate_digits(characters)
    print(sum(isolate_digits(characters)))
