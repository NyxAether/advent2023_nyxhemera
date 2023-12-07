import numpy as np
from advent2023.aoc3.utils import (
    symbole_pos,
    digit_pos,
    neighbors_symb,
    neighbors_digit,
    find_digits_of_interest,
    isolate_digits,
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
