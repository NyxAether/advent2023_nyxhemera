import numpy as np
from utils import get_cards, get_characters_table, get_lines, parse_seeds
from aoc1.utils import extract_first_last_digit, transform_text_digits_to_digits
from aoc2.utils import extract_game, max_product, possible_max
from aoc3.utils import get_gears, isolate_digits
from aoc4.utils import score, total_cards
from aoc5.almanach import Almanach


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
    print(f"Solution 3-1: {sum(isolate_digits(characters))}")

    # Problem 3-2
    characters = get_characters_table(INPUT_3_PATH)
    print(f"Solution 3-2: {sum(get_gears(characters))}")

    # AOC 4
    INPUT_4_PATH = "data/input4.txt"

    # Problem 4-1
    wins, values = get_cards(INPUT_4_PATH)
    print(f"Solution 4-1: {score(wins, values)}")  

    # Problem 4-2
    wins, values = get_cards(INPUT_4_PATH)
    print(f"Solution 4-2: {total_cards(wins, values)}")    

    # AOC 5
    INPUT_5_PATH = "data/input5.txt"

    # Problem 5-1
    alma = Almanach(*(parse_seeds(INPUT_5_PATH)))
    print(f"Solution 5-1: {alma.find_closest_position()}")
