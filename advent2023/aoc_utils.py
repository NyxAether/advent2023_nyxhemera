from pathlib import Path
import re

from advent2023.aoc7.hand import Hand


def get_lines(path: Path) -> list:
    """
    Reads the contents of a file and returns a list of stripped lines.

    Args:
        path (Path): The path to the file.

    Returns:
        list: A list of stripped lines from the file.
    """
    with Path(path).open("r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def get_characters_table(path: Path) -> list[list[str]]:
    """
    Generates a table of characters from a given file path.

    Args:
        path (Path): The path to the file.

    Returns:
        list[list[str]]: A table of characters where each row represents a line in the file.
    """

    lines = get_lines(path)
    return [[c for c in line] for line in lines]


def get_cards(path: str) -> tuple[list[set[int]], list[set[int]]]:
    wins: list[set[int]] = []
    values: list[set[int]] = []
    with Path(path).open("r", encoding="utf-8") as f:
        # Exemple "Card   1: 99 71  |  5 45 54 83  3"
        lines_cards = [line.strip().split(":")[1].split("|") for line in f]
        for winning, numbers in lines_cards:
            wins.append(set(int(v_win) for v_win in re.split(r"\s+", winning.strip())))
            values.append(set(int(v) for v in re.split(r"\s+", numbers.strip())))
    return wins, values


def parse_seeds(path: str):
    with Path(path).open("r", encoding="utf-8") as f:
        almanach = f.read()
    seeds_pat = re.compile(r"seeds: ((?:\d+ ?)+)\n")
    seeds_soils_pat = re.compile(r"""seed-to-soil map:\n((?:\d+ \d+ \d+\n)+)\n""", re.M)
    soils_fert_pat = re.compile(
        r"""soil-to-fertilizer map:\n((?:\d+ \d+ \d+\n)+)\n""", re.M
    )
    fert_water_pat = re.compile(
        r"""fertilizer-to-water map:\n((?:\d+ \d+ \d+\n)+)\n""", re.M
    )
    water_light_pat = re.compile(
        r"""water-to-light map:\n((?:\d+ \d+ \d+\n)+)\n""", re.M
    )
    light_temp_pat = re.compile(
        r"""light-to-temperature map:\n((?:\d+ \d+ \d+\n)+)\n""", re.M
    )
    temp_hum_pat = re.compile(
        r"""temperature-to-humidity map:\n((?:\d+ \d+ \d+\n)+)\n""", re.M
    )
    hum_loc_pat = re.compile(
        r"""humidity-to-location map:\n((?:\d+ \d+ \d+\n)+)\n""", re.M
    )

    seeds = [int(x) for x in seeds_pat.search(almanach).group(1).split(" ")]

    def extract_groups(pattern: re.Pattern, almanach: str) -> tuple[int, int, int]:
        res = pattern.search(almanach).group(1).strip().split("\n")
        return [tuple(int(x) for x in line.strip().split(" ")) for line in res]

    seeds_soils = extract_groups(seeds_soils_pat, almanach)
    soils_fert = extract_groups(soils_fert_pat, almanach)
    fert_water = extract_groups(fert_water_pat, almanach)
    water_light = extract_groups(water_light_pat, almanach)
    light_temp = extract_groups(light_temp_pat, almanach)
    temp_hum = extract_groups(temp_hum_pat, almanach)
    hum_loc = extract_groups(hum_loc_pat, almanach)
    return (
        seeds,
        seeds_soils,
        soils_fert,
        fert_water,
        water_light,
        light_temp,
        temp_hum,
        hum_loc,
    )


def parse_race(path: str) -> tuple[list[int], list[int]]:
    with Path(path).open("r", encoding="utf-8") as f:
        times = re.split(r"\s+", f.readline().strip())[1:]
        times = [int(t) for t in times]
        distances = re.split(r"\s+", f.readline().strip())[1:]
        distances = [int(d) for d in distances]
    return times, distances


def parse_hands(path: str) -> tuple[list[Hand]]:
    with Path(path).open("r", encoding="utf-8") as f:
        lines = f.readlines()
    hands = [
        Hand(line.strip().split(" ")[0], int(line.strip().split(" ")[1]))
        for line in lines
    ]
    return hands
