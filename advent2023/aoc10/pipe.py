from pathlib import Path
import sys


class Pipe:
    def __init__(self, path: str) -> None:
        self.pipes = []
        with Path(path).open("r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                self.pipes.append([x for x in line.strip()])
                if "S" in self.pipes[-1]:
                    self.start = (i, self.pipes[-1].index("S"))
        self.__symb = ("|", "-", "L", "J", "7", "F", ".", "S")
        self.__north = ("|", "7", "F", "S")
        self.__east = ("-", "J", "7", "S")
        self.__south = ("|", "L", "J", "S")
        self.__west = ("-", "L", "F", "S")
        self.shape = (len(self.pipes), len(self.pipes[0]))

    def get_longest_point(self) -> int:
        history = self.find_path(self.start, [], True)
        return len((history))//2
    
    def find_path(
        self,
        pos: tuple[int, int],
        prev_history: list[tuple[int, int]],
        is_s: bool = False,
    ) -> list[tuple[int, int]] | None:
        history = prev_history + [pos]
        match self.pipes[pos[0]][pos[1]]:
            case "|":
                if self.can_north(pos, history, is_s):
                    new_history = self.find_path((pos[0] - 1, pos[1]), history)
                    if new_history:
                        return new_history
                if self.can_south(pos, history, is_s):
                    new_history = self.find_path((pos[0] + 1, pos[1]), history)
                    if new_history:
                        return new_history
            case "-":
                if self.can_east(pos, history, is_s):
                    new_history = self.find_path((pos[0], pos[1] + 1), history)
                    if new_history:
                        return new_history
                if self.can_west(pos, history, is_s):
                    new_history = self.find_path((pos[0], pos[1] - 1), history)
                    if new_history:
                        return new_history
            case "L":
                if self.can_north(pos, history, is_s):
                    new_history = self.find_path((pos[0] - 1, pos[1]), history)
                    if new_history:
                        return new_history
                if self.can_east(pos, history, is_s):
                    new_history = self.find_path((pos[0], pos[1] + 1), history)
                    if new_history:
                        return new_history
            case "J":
                if self.can_north(pos, history, is_s):
                    new_history = self.find_path((pos[0] - 1, pos[1]), history)
                    if new_history:
                        return new_history
                if self.can_west(pos, history, is_s):
                    new_history = self.find_path((pos[0], pos[1] - 1), history)
                    if new_history:
                        return new_history
            case "7":
                if self.can_south(pos, history, is_s):
                    new_history = self.find_path((pos[0] + 1, pos[1]), history)
                    if new_history:
                        return new_history
                if self.can_west(pos, history, is_s):
                    new_history = self.find_path((pos[0], pos[1] - 1), history)
                    if new_history:
                        return new_history
            case "F":
                if self.can_south(pos, history, is_s):
                    new_history = self.find_path((pos[0] + 1, pos[1]), history)
                    if new_history:
                        return new_history
                if self.can_east(pos, history, is_s):
                    new_history = self.find_path((pos[0], pos[1] + 1), history)
                    if new_history:
                        return new_history
            case "S":
                if not is_s:
                    return history
                if self.can_north(pos, history):
                    new_history = self.find_path((pos[0] - 1, pos[1]), history, is_s)
                    if new_history:
                        return new_history
                if self.can_east(pos, history):
                    new_history = self.find_path((pos[0], pos[1] + 1), history, is_s)
                    if new_history:
                        return new_history
                if self.can_west(pos, history):
                    new_history = self.find_path((pos[0], pos[1] - 1), history, is_s)
                    if new_history:
                        return new_history
                if self.can_south(pos, history):
                    new_history = self.find_path((pos[0] + 1, pos[1]), history, is_s)
                    if new_history:
                        return new_history
        return None

    def can_north(
        self, pos: tuple[int, int], history: list[tuple[int, int]], is_s: bool = True
    ) -> bool:
        return (
            pos[0] > 0
            and (
                ((pos[0] - 1, pos[1]) not in history)
                or (not is_s and self.pipes[pos[0] - 1][pos[1]] == "S")
            )
            and self.pipes[pos[0] - 1][pos[1]] in self.__north
        ) and not (is_s and self.pipes[pos[0] - 1][pos[1]] == "S")

    def can_east(
        self, pos: tuple[int, int], history: list[tuple[int, int]], is_s: bool = True
    ) -> bool:
        return (
            pos[1] < len(self.pipes[pos[0]]) - 1
            and (
                ((pos[0], pos[1] + 1) not in history)
                or (not is_s and self.pipes[pos[0]][pos[1] + 1] == "S")
            )
            and self.pipes[pos[0]][pos[1] + 1] in self.__east
        ) and not (is_s and self.pipes[pos[0]][pos[1] + 1] == "S")

    def can_south(
        self, pos: tuple[int, int], history: list[tuple[int, int]], is_s: bool = True
    ) -> bool:
        return (
            pos[0] < len(self.pipes) - 1
            and (
                ((pos[0] + 1, pos[1]) not in history)
                or (not is_s and self.pipes[pos[0] + 1][pos[1]] == "S")
            )
            and self.pipes[pos[0] + 1][pos[1]] in self.__south
        ) and not (is_s and self.pipes[pos[0] + 1][pos[1]] == "S")

    def can_west(
        self, pos: tuple[int, int], history: list[tuple[int, int]], is_s: bool = True
    ) -> bool:
        return (
            pos[1] > 0
            and (
                ((pos[0], pos[1] - 1) not in history)
                or (not is_s and self.pipes[pos[0]][pos[1] - 1] == "S")
            )
            and self.pipes[pos[0]][pos[1] - 1] in self.__west
        ) and not (is_s and self.pipes[pos[0]][pos[1] - 1] == "S")
    

