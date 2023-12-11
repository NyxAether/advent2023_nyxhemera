from pathlib import Path
import re


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


def get_cards(path: str) -> tuple[set[int], set[int]]:
    wins: list[set[int]] = []
    values: list[set[int]] = []
    with Path(path).open("r", encoding="utf-8") as f:
        # Exemple "Card   1: 99 71  |  5 45 54 83  3"
        lines_cards = [line.strip().split(":")[1].split("|") for line in f]
        for winning, numbers in lines_cards:
            wins.append(set(int(v_win) for v_win in re.split(r"\s+", winning.strip())))
            values.append(set(int(v) for v in re.split(r"\s+", numbers.strip())))
    return wins, values
