from advent2023.aoc2.utils import extract_game, max_product, possible_max


def test_extract_game():
    assert extract_game(
        "Game 100: 1 red, 5 blue, 2 green; 3 red, 1 blue; 1 green, 1 blue, 1 red"
    ) == (
        100,
        ("1 red", "5 blue", "2 green", "3 red", "1 blue", "1 green", "1 blue", "1 red"),
    )
    assert (
        extract_game(
            "Game 1:\
            2 red, 2 green;\
            1 red, 1 green, 2 blue;\
            3 blue, 3 red, 3 green;\
            1 blue, 3 green, 7 red;\
            5 red, 3 green, 1 blue"
        )
        == (
            1,
            (
                "2 red",
                "2 green",
                "1 red",
                "1 green",
                "2 blue",
                "3 blue",
                "3 red",
                "3 green",
                "1 blue",
                "3 green",
                "7 red",
                "5 red",
                "3 green",
                "1 blue",
            ),
        )
    )


def test_possible_max():
    assert (
        possible_max(
            (
                1,
                (
                    "2 red",
                    "2 green",
                    "1 red",
                    "1 green",
                    "2 blue",
                    "3 blue",
                    "3 red",
                    "3 green",
                    "1 blue",
                    "3 green",
                    "7 red",
                    "5 red",
                    "3 green",
                    "1 blue",
                ),
            )
        )
        == 1
    )
    assert (
        possible_max(
            (
                6,
                (
                    "2 red",
                    "2 green",
                    "1 red",
                    "1 green",
                    "2 blue",
                    "3 blue",
                    "3 red",
                    "30 green",
                    "1 blue",
                    "3 green",
                ),
            )
        )
        is None
    )
    assert possible_max((41, ("12 red",))) == 41
    assert possible_max((41, ("13 green",))) == 41
    assert possible_max((41, ("14 blue",))) == 41
    assert possible_max((41, ("13 red",))) is None
    assert possible_max((41, ("14 green",))) is None
    assert possible_max((41, ("15 blue",))) is None


def test_max_product():
    assert (
        max_product(
            (
                1,
                ("2 red", "2 green", "1 blue"),
            )
        )
        == 4
    )
    assert (
        max_product(
            (
                6,
                ("2 red", "2 blue", "4 blue"),
            )
        )
        == 0
    )
    assert (
        max_product(
            (
                6,
                ("2 red", "2 blue", "4 blue", "7 green"),
            )
        )
        == 56
    )
