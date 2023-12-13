import re


def extract_game(line: str) -> tuple[int, tuple[str]]:
    """
    Extracts the game number and the players from a given string line.

    Parameters:
        line (str): The input string line.

    Returns:
        tuple[int, tuple[str]]: The game ID and the list of pulls.

    Example:
        >>> extract_game("Game 100: 1 red, 5 blue, 2 green; 3 red, 1 blue; 1 green, 1 blue, 1 red")
        (100, ('1 red', '5 blue', '2 green', '3 red', '1 blue', '1 green', '1 blue', '1 red'))
    """
    pattern = re.compile(r"Game (\d+):")
    game_id = int(pattern.search(line).group(1))
    draws = line.split(":")[1].replace(";", ",").split(",")
    draws = tuple(draw.strip() for draw in draws)
    return game_id, draws


def possible_max(game: tuple[int, tuple[str]]) -> int:
    """
    Given a game tuple containing an identifier and a list of draws,
    this function determines if the maximum number drawn for each color
    (red, green, blue) is within the specified limits. If all the maximum
    numbers are within the limits, it returns the game identifier; otherwise,
    it returns None.

    Parameters:
    - game: A tuple containing an identifier (int) and a list of draws (tuple[str]).

    Returns:
    - int: The game identifier if the maximum numbers are within the limits,
      otherwise None.
    """
    max_draw = {"red": 0, "blue": 0, "green": 0}
    game_id, draws = game
    for draw in draws:
        number, color = draw.split(" ")
        if max_draw[color] < int(number):
            max_draw[color] = int(number)

    if max_draw["red"] <= 12 and max_draw["green"] <= 13 and max_draw["blue"] <= 14:
        return game_id
    else:
        return None


def max_product(game: tuple[int, tuple[str]]) -> int:
    _, draws = game
    max_draw = {"red": 0, "blue": 0, "green": 0}
    for draw in draws:
        number, color = draw.split(" ")
        if max_draw[color] < int(number):
            max_draw[color] = int(number)
    return max_draw["red"] * max_draw["green"] * max_draw["blue"]
