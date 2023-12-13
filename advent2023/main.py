from advent2023.aoc8.desert_map import AdvancedDesertMap, DesertMap
from advent2023.aoc_utils import (
    get_cards,
    get_characters_table,
    get_lines,
    parse_desert_map,
    parse_hands,
    parse_race,
    parse_seeds,
)
from advent2023.aoc1.aoc_utils import (
    extract_first_last_digit,
    transform_text_digits_to_digits,
)
from advent2023.aoc2.aoc_utils import extract_game, max_product, possible_max
from advent2023.aoc3.aoc_utils import get_gears, isolate_digits
from advent2023.aoc4.aoc_utils import score, total_cards
from advent2023.aoc5.almanach import Almanach
from advent2023.aoc6.aoc_utils import count_wins, wins_product
from advent2023.aoc7.aoc_utils import rank_hands


def main():
    INPUT_1_PATH = "data/input1.txt"
    INPUT_2_PATH = "data/input2.txt"
    lines = get_lines(INPUT_1_PATH)

    # Problem 1-1
    res_1 = sum((extract_first_last_digit(line) for line in lines))
    print(f"Solution 1-1: {res_1}")

    # Problem 1-2
    res_2 = sum(
        (
            extract_first_last_digit(transform_text_digits_to_digits(line))
            for line in lines
        )
    )
    print(f"Solution 1-2: {res_2}")
    del lines
    del res_1
    del res_2

    # AOC 2
    INPUT_2_PATH = "data/input2.txt"
    lines = get_lines(INPUT_2_PATH)

    # Problem 2-1
    games = [possible_max(extract_game(line)) for line in lines]
    print(f"Solution 2-1: {sum([game for game in games if game is not None])}")

    # Problem 2-2
    games = [max_product(extract_game(line)) for line in lines]
    print(f"Solution 2-2: {sum(games)}")
    del lines
    del games

    # AOC 3
    INPUT_3_PATH = "data/input3.txt"

    # Problem 3-1
    characters = get_characters_table(INPUT_3_PATH)
    print(f"Solution 3-1: {sum(isolate_digits(characters))}")

    # Problem 3-2
    characters = get_characters_table(INPUT_3_PATH)
    print(f"Solution 3-2: {sum(get_gears(characters))}")
    del characters

    # AOC 4
    INPUT_4_PATH = "data/input4.txt"

    # Problem 4-1
    wins, values = get_cards(INPUT_4_PATH)
    print(f"Solution 4-1: {score(wins, values)}")

    # Problem 4-2
    wins, values = get_cards(INPUT_4_PATH)
    print(f"Solution 4-2: {total_cards(wins, values)}")
    del wins
    del values

    # AOC 5
    INPUT_5_PATH = "data/input5.txt"

    # Problem 5-1
    alma = Almanach(*(parse_seeds(INPUT_5_PATH)))
    print(f"Solution 5-1: {alma.find_closest_position()}")

    # Problem 5-2
    print(f"Solution 5-2: {alma.find_closest_position_from_tuple()}")
    del alma

    # AOC 6
    INPUT_6_PATH = "data/input6.txt"

    # Problem 6-1
    times, distances = parse_race(INPUT_6_PATH)
    print(f"Solution 6-1: {wins_product(times,distances)}")

    # Problem 6-2
    print(f"Solution 6-2: {count_wins(44826981, 202107611381458)}")
    del times, distances

    # AOC 7
    INPUT_7_PATH = "data/input7.txt"

    # Problem 7-1
    hands = parse_hands(INPUT_7_PATH)
    print(f"Solution 7-1: {rank_hands(hands)}")

    # Problem 7-2
    for hand in hands:
        hand.joker = True
    print(f"Solution 7-2: {rank_hands(hands)}")
    del hands

    # AOC 8
    INPUT_8_PATH = "data/input8.txt"

    # Problem 8-1
    directions, froms, tos = parse_desert_map(INPUT_8_PATH)
    dm = DesertMap(directions, froms, tos)
    print(f"Solution 8-1: {dm.steps_start_to_end('AAA')[0]}")

    # Problem 8-2
    adm = AdvancedDesertMap(directions, froms, tos)
    print(f"Solution 8-2: {adm.advanced_steps_start_to_end()}")
    del dm, adm
    

if __name__ == "__main__":
    main()
