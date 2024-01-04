from dataclasses import dataclass
from pathlib import Path


@dataclass
class Position:
    i: int
    j: int

    def __call__(self) -> tuple[int, int]:
        return self.i, self.j

    def __getitem__(self, item):
        if item == 0:
            return self.i
        if item == 1:
            return self.j

    @property
    def north(self):
        return Position(self.i - 1, self.j)

    @property
    def east(self):
        return Position(self.i, self.j + 1)

    @property
    def south(self):
        return Position(self.i + 1, self.j)

    @property
    def west(self):
        return Position(self.i, self.j - 1)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Position):
            return self.i == __value.i and self.j == __value.j
        return False


class Pipe:
    def __init__(self, path: str) -> None:
        self.pipes = []
        with Path(path).open("r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                self.pipes.append([x for x in line.strip()])
                if "S" in self.pipes[-1]:
                    self.start = Position(i, self.pipes[-1].index("S"))
        # self.__symb = ("|", "-", "L", "J", "7", "F", ".", "S")
        self.__north = ("|", "7", "F", "S")
        self.__east = ("-", "J", "7", "S")
        self.__south = ("|", "L", "J", "S")
        self.__west = ("-", "L", "F", "S")
        self.shape = (len(self.pipes), len(self.pipes[0]))
        self.chaine = None

    def get_longest_point(self) -> int:
        if not self.chaine:
            self.chaine = self.find_path(self.start, [], True)
        history = self.chaine
        if not history:
            return 0
        return len((history)) // 2

    def contained_space(self) -> None:
        if not self.chaine:
            self.chaine = self.find_path(self.start, [], True)
        history = self.chaine
        if not history:
            return None
        chaine = set(history)
        out_space: set[Position] = set(chaine)
        in_space: set[Position] = set()
        not_seen = set(
            Position(i, j)
            for i in range(len(self.pipes))
            for j in range(len(self.pipes[0]))
        )
        for pos in chaine:
            if self.border(pos)>0:
                current = pos
                break
            else:
                return None
        match self.pipes[current.i][current.j]:
            case "|":
                current = current.north
            case "-":
                current = current.east
            case "L":
                current = current.south
            case "J":
                current = current.west
            case "7":
                current = current.north
            case "F":
                current = current.east
            case _ :
                return None

    def find_path(
        self,
        pos: Position,
        prev_history: list[Position],
        is_s: bool = False,
    ) -> list[Position] | None:
        history = prev_history + [pos]
        match self.pipes[pos[0]][pos[1]]:
            case "|":
                if self.can_north(pos, history, is_s):
                    new_history = self.find_path(pos.north, history)
                    if new_history:
                        return new_history
                if self.can_south(pos, history, is_s):
                    new_history = self.find_path(pos.south, history)
                    if new_history:
                        return new_history
            case "-":
                if self.can_east(pos, history, is_s):
                    new_history = self.find_path(pos.east, history)
                    if new_history:
                        return new_history
                if self.can_west(pos, history, is_s):
                    new_history = self.find_path(pos.west, history)
                    if new_history:
                        return new_history
            case "L":
                if self.can_north(pos, history, is_s):
                    new_history = self.find_path(pos.north, history)
                    if new_history:
                        return new_history
                if self.can_east(pos, history, is_s):
                    new_history = self.find_path(pos.east, history)
                    if new_history:
                        return new_history
            case "J":
                if self.can_north(pos, history, is_s):
                    new_history = self.find_path(pos.north, history)
                    if new_history:
                        return new_history
                if self.can_west(pos, history, is_s):
                    new_history = self.find_path(pos.west, history)
                    if new_history:
                        return new_history
            case "7":
                if self.can_south(pos, history, is_s):
                    new_history = self.find_path(pos.south, history)
                    if new_history:
                        return new_history
                if self.can_west(pos, history, is_s):
                    new_history = self.find_path(pos.west, history)
                    if new_history:
                        return new_history
            case "F":
                if self.can_south(pos, history, is_s):
                    new_history = self.find_path(pos.south, history)
                    if new_history:
                        return new_history
                if self.can_east(pos, history, is_s):
                    new_history = self.find_path(pos.east, history)
                    if new_history:
                        return new_history
            case "S":
                if not is_s:
                    return history
                if self.can_north(pos, history):
                    new_history = self.find_path(pos.north, history, is_s)
                    if new_history:
                        return new_history
                if self.can_east(pos, history):
                    new_history = self.find_path(pos.east, history, is_s)
                    if new_history:
                        return new_history
                if self.can_west(pos, history):
                    new_history = self.find_path(pos.west, history, is_s)
                    if new_history:
                        return new_history
                if self.can_south(pos, history):
                    new_history = self.find_path(pos.south, history, is_s)
                    if new_history:
                        return new_history
        return None

    def can_north(
        self, pos: Position, history: list[Position], is_s: bool = True
    ) -> bool:
        return (
            pos[0] > 0
            and (
                (pos.north not in history)
                or (not is_s and self.pipes[pos[0] - 1][pos[1]] == "S")
            )
            and self.pipes[pos[0] - 1][pos[1]] in self.__north
        ) and not (is_s and self.pipes[pos[0] - 1][pos[1]] == "S")

    def can_east(
        self, pos: Position, history: list[Position], is_s: bool = True
    ) -> bool:
        return (
            pos[1] < len(self.pipes[pos[0]]) - 1
            and (
                (pos.east not in history)
                or (not is_s and self.pipes[pos[0]][pos[1] + 1] == "S")
            )
            and self.pipes[pos[0]][pos[1] + 1] in self.__east
        ) and not (is_s and self.pipes[pos[0]][pos[1] + 1] == "S")

    def can_south(
        self, pos: Position, history: list[Position], is_s: bool = True
    ) -> bool:
        return (
            pos[0] < len(self.pipes) - 1
            and (
                (pos.south not in history)
                or (not is_s and self.pipes[pos[0] + 1][pos[1]] == "S")
            )
            and self.pipes[pos[0] + 1][pos[1]] in self.__south
        ) and not (is_s and self.pipes[pos[0] + 1][pos[1]] == "S")

    def can_west(
        self, pos: Position, history: list[Position], is_s: bool = True
    ) -> bool:
        return (
            pos[1] > 0
            and (
                (pos.west not in history)
                or (not is_s and self.pipes[pos[0]][pos[1] - 1] == "S")
            )
            and self.pipes[pos[0]][pos[1] - 1] in self.__west
        ) and not (is_s and self.pipes[pos[0]][pos[1] - 1] == "S")

    def border(self,pos: Position) -> int:
        if pos[0] == 0:
            return 1
        if pos[1] == len(self.pipes[pos[0]]) - 1:
            return 2
        if pos[1] == 0:
            return 3
        if pos[0] == len(self.pipes) - 1:
            return 4
        return 0