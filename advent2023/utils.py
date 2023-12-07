from pathlib import Path


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
