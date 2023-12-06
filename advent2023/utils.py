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
