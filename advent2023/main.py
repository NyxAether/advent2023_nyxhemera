from utils import get_lines
from aoc1.utils import extract_first_last_digit, transform_text_digits_to_digits
from aoc2.utils import extract_game, max_product, possible_max


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