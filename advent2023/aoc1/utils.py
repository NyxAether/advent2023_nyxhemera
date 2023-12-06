import re


def extract_first_last_digit(line: str) -> int:
    """
    Extracts the first and last digit from a given string.

    Args:
        line (str): The input string.

    Returns:
        int: The first and last digit extracted from the string.

    Example:
        >>> extract_first_last_digit("abc123def456")
        16
    """
    # Remove all non-digit characters
    line = re.sub(r"\D", "", line)
    return int(line[0] + line[-1])


def transform_text_digits_to_digits(line: str) -> str:
    """
    A function that transforms the digits written in plain text in a given string line to digits.

    Parameters:
        line (str): The input string line to be transformed.

    Returns:
        str: The transformed string line with digits written in plain text replaced by digits.
    """
    p = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    line = "".join([m for m in p.findall(line)])
    text_to_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for key, value in text_to_digits.items():
        line = line.replace(key, value)
    return line
