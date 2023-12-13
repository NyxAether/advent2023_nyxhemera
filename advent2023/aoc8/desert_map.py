import re
import numpy as np


class DesertMap:
    def __init__(
        self, directions: str, froms: list[str], tos: list[tuple[str, str]]
    ) -> None:
        self.turns = {froms[i]: tos[i] for i in range(len(froms))}
        self.directions = [0 if d == "L" else 1 for d in directions]
        self.start = "AAA"
        self.end = "ZZZ"

    def steps_start_to_end(self, start: str) -> int:
        steps = 0
        current = ""

        while self.check_end(current):
            if current == "":
                current = start
            next_val = self.turns[current][
                self.directions[steps % len(self.directions)]
            ]
            current = next_val
            steps += 1
        return steps, current

    def check_end(self, current: str) -> bool:
        return self.end != current


class AdvancedDesertMap(DesertMap):
    def __init__(
        self, directions: str, froms: list[str], tos: list[tuple[str, str]]
    ) -> None:
        super(AdvancedDesertMap, self).__init__(directions, froms, tos)
        self.start = [node for node in froms if re.match(r"^..A$", node)]
        self.end = [node for node in froms if re.match(r"^..Z$", node)]

    def advanced_steps_start_to_end(self) -> int:
        steps = np.array([self.steps_start_to_end(s)[0] for s in self.start]).astype(
            "int64"
        )

        lcm = np.lcm.reduce(steps)
        return lcm

    def check_end(self, current: str) -> bool:
        return current not in self.end
