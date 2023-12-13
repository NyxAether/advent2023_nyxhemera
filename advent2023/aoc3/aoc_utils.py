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


def find_digits_of_interest(table: list[list[str]]) -> np.ndarray:
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


def get_all_character_indexes(c: str, table: list[str]) -> list[tuple[int, int]]:
    indexes = []
    for i, line in enumerate(table):
        for j, ltr in enumerate(line):
            if ltr == c:
                indexes.append((i, j))
    return indexes


def get_box_around(pos: tuple[int, int], is_int: np.ndarray) -> np.ndarray:
    len_line = is_int.shape[0]
    len_col = is_int.shape[1]
    return is_int[
        max(pos[0] - 1, 0) : min(pos[0] + 2, len_line),
        max(pos[1] - 1, 0) : min(pos[1] + 2, len_col),
    ]


def two_around(box: np.ndarray):
    def weird_sum_line(line: np.ndarray) -> int:
        line = line.astype(int)
        return line[1] or (line[0] + line[2])

    return weird_sum_line(box[0]) + weird_sum_line(box[1]) + weird_sum_line(box[2])


def get_int(pos: tuple[int, int], is_int: np.ndarray, table: list[list[str]]):
    pos_min = list(pos)
    pos_max = list(pos)
    while pos_min[1] >= 0 and is_int[pos_min[0], pos_min[1]]:
        pos_min[1] -= 1
    pos_min[1] += 1
    while pos_max[1] < is_int.shape[1] and is_int[pos_max[0], pos_max[1]]:
        pos_max[1] += 1
    pos_max[1] -= 1
    return int("".join(table[pos[0]][pos_min[1] : pos_max[1] + 1]))


def get_gear_ratio(
    pos: tuple[int, int], box: np.array, is_int: np.ndarray, table: list[list[str]]
):
    arg_pos = box.max(axis=1)
    pos_per_line = {(a - 1): b - 1 for a, b in zip(*(np.where(box)))}
    nb_lines = arg_pos.sum()
    if nb_lines == 1:
        pos1 = (pos[0] + arg_pos.argmax() - 1, pos[1] - 1)
        pos2 = (pos[0] + arg_pos.argmax() - 1, pos[1] + 1)
        first_int = get_int(pos1, is_int, table)
        second_int = get_int(pos2, is_int, table)
    else:
        all_ints = []
        for line in pos_per_line:
            all_ints.append(
                get_int((pos[0] + line, pos[1] + pos_per_line[line]), is_int, table)
            )
        first_int = all_ints[0]
        second_int = all_ints[1]
    return first_int * second_int


def get_gears(table: list[list[str]]) -> int:
    valid_ints = find_digits_of_interest(table)
    poses = get_all_character_indexes("*", table)
    boxes = [get_box_around(pos, valid_ints) for pos in poses]
    valid_boxes = [(box, pos) for box, pos in zip(boxes, poses) if two_around(box) == 2]
    return [get_gear_ratio(pos, box, valid_ints, table) for box, pos in valid_boxes]
