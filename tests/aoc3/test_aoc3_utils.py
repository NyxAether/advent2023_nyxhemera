import numpy as np
from advent2023.aoc3.aoc_utils import (
    get_all_character_indexes,
    symbole_pos,
    digit_pos,
    neighbors_symb,
    neighbors_digit,
    find_digits_of_interest,
    isolate_digits,
    two_around,
)

data = [
    ["1", ".", "*"],
    ["5", "7", "1"],
    [".", "%", "."],
]
data2 = [
    ["1", ".", "*"],
    ["5", "7", "1"],
    ["2", "%", "."],
]
data3 = [
    ["1", "2", ".", "*"],
    ["3", ".", "7", "1"],
    ["4", "5", ".", "."],
]


def test_symbole_pos():
    assert (
        symbole_pos(data)
        == np.array([[False, False, True], [False, False, False], [False, True, False]])
    ).all()


def test_digit_pos():
    assert (
        digit_pos(data)
        == np.array([[True, False, False], [True, True, True], [False, False, False]])
    ).all()


def test_neighbors_symb():
    assert (
        neighbors_symb(
            np.array(
                [
                    [False, False, False],
                    [False, True, False],
                    [False, False, False],
                ]
            )
        )
        == np.array(
            [
                [True, True, True],
                [True, True, True],
                [True, True, True],
            ]
        )
    ).all()
    assert (
        neighbors_symb(
            np.array(
                [
                    [False, False, False],
                    [False, False, False],
                    [False, False, False],
                ]
            )
        )
        == np.array(
            [
                [False, False, False],
                [False, False, False],
                [False, False, False],
            ]
        )
    ).all()
    assert (
        neighbors_symb(
            np.array(
                [
                    [True, False, False],
                    [False, False, False],
                    [False, False, False],
                ]
            )
        )
        == np.array(
            [
                [True, True, False],
                [True, True, False],
                [False, False, False],
            ]
        )
    ).all()
    assert (
        neighbors_symb(
            np.array(
                [
                    [True, False, False],
                    [False, False, False],
                    [False, False, True],
                ]
            )
        )
        == np.array(
            [
                [True, True, False],
                [True, True, True],
                [False, True, True],
            ]
        )
    ).all()


def test_neighbors_digit():
    assert (
        neighbors_digit(
            np.array(
                [
                    [False, False, False],
                    [False, True, False],
                    [False, False, False],
                ]
            )
        )
        == np.array(
            [
                [False, False, False],
                [True, True, True],
                [False, False, False],
            ]
        )
    ).all()
    assert (
        neighbors_digit(
            np.array(
                [
                    [False, False, False],
                    [False, False, False],
                    [False, False, False],
                ]
            )
        )
        == np.array(
            [
                [False, False, False],
                [False, False, False],
                [False, False, False],
            ]
        )
    ).all()
    assert (
        neighbors_digit(
            np.array(
                [
                    [True, False, False],
                    [False, False, False],
                    [False, False, False],
                ]
            )
        )
        == np.array(
            [
                [True, True, False],
                [False, False, False],
                [False, False, False],
            ]
        )
    ).all()
    assert (
        neighbors_digit(
            np.array(
                [
                    [True, False, False],
                    [False, False, False],
                    [False, False, True],
                ]
            )
        )
        == np.array(
            [
                [True, True, False],
                [False, False, False],
                [False, True, True],
            ]
        )
    ).all()


def test_find_digits_of_interest():
    assert (
        find_digits_of_interest(data)
        == np.array(
            [
                [False, False, False],
                [True, True, True],
                [False, False, False],
            ]
        )
    ).all()


def test_isolate_digits():
    assert isolate_digits(data) == [571]
    assert isolate_digits(data2) == [571, 2]
    assert isolate_digits(data3) == [71]


def test_get_all_character_indexes():
    assert set(get_all_character_indexes(".", data)) == set([(2, 0), (0, 1), (2, 2)])
    assert set(get_all_character_indexes("*", data2)) == set([(0, 2)])
    assert set(get_all_character_indexes("?", data3)) == set([])


def test_two_around():
    assert (
        two_around(
            np.array(
                [[False, False, False], [False, True, False], [False, False, False]]
            )
        )
        == 1
    )
    assert (
        two_around(
            np.array([[True, False, True], [False, False, False], [False, True, False]])
        )
        == 3
    )
    assert (
        two_around(
            np.array(
                [[True, True, False], [False, False, False], [False, False, False]]
            )
        )
        == 1
    )
    assert (
        two_around(
            np.array([[True, True, True], [False, False, False], [False, False, False]])
        )
        == 1
    )
