import re
import numpy as np


def symbole_pos(lines: list[list[str]]) -> np.ndarray:
    table = np.array(lines)
    pattern = re.compile(r"\d|\.")
    is_symbole = np.vectorize(lambda x: pattern.search(x) is None)
    return is_symbole(table)


def digit_pos(lines: list[list[str]]) -> np.ndarray:
    table = np.array(lines)
    is_digit = np.vectorize(
        lambda x: x in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    )
    return is_digit(table)


def neighbors_symb(pos: np.ndarray) -> np.ndarray:
    len_line = pos.shape[0]
    len_col = pos.shape[1]
    arg_pos = np.where(pos)
    for i, j in zip(arg_pos[0], arg_pos[1]):
        pos[
            max(i - 1, 0) : min(i + 2, len_line), max(j - 1, 0) : min(j + 2, len_col)
        ] = True
    return pos


def neighbors_digit(pos: np.ndarray) -> np.ndarray:
    len_col = pos.shape[1]
    arg_pos = np.where(pos)
    for i, j in zip(arg_pos[0], arg_pos[1]):
        pos[i, max(j - 1, 0) : min(j + 2, len_col)] = True
    return pos


def find_digits_of_interest(table: list[list[str]]) -> None:
    # Detect postions of digits and symbols
    digit_mat = digit_pos(table)
    symb_mat = symbole_pos(table)

    # Detect digits neighbors with symbols
    nn_symb = neighbors_symb(symb_mat)
    valid_digits = digit_mat & nn_symb

    # Detect digits neighbors with digits
    nb_digits_prev = valid_digits.sum()
    valid_digits = neighbors_digit(valid_digits) & digit_mat
    nb_digits = valid_digits.sum()
    while nb_digits != nb_digits_prev:
        nb_digits_prev = nb_digits
        valid_digits = neighbors_digit(valid_digits) & digit_mat
        nb_digits = valid_digits.sum()
    return valid_digits


def isolate_digits(table: list[list[str]]) -> list[int]:
    digits_selected = find_digits_of_interest(table)
    characters = np.array(table)
    characters[~digits_selected] = "."
    res = []
    for line in characters:
        res.extend([int(v.group()) for v in re.finditer(r"\d+", "".join(line))])
    return res