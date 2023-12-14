import numpy as np


class Pascal:
    def __init__(self, values: list[list[int]]) -> None:
        self.values = [np.array(value).astype("int64") for value in values]

    def find_pascal(self, series: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        current = series.copy()
        computed_next = [current[-1]]
        computed_prev = [current[0]]

        sub = np.array([1, -1])
        while any(current != 0):
            current = np.convolve(current, sub)[1:-1]
            computed_next.append(current[-1])
            computed_prev.append(current[0])
        return np.array(computed_prev).astype("int64"), np.array(computed_next).astype(
            "int64"
        )

    def pred_next(self, series: np.ndarray) -> int:
        _, computed_values = self.find_pascal(series)
        return computed_values.sum()

    def pred_prev(self, series: np.ndarray) -> int:
        computed_values, _ = self.find_pascal(series)
        return (
            computed_values
            * np.array([(-1) ** (i % 2) for i in range(len(computed_values))])
        ).sum()

    def compute_sum_preds(self) -> int:
        return sum((self.pred_next(v) for v in self.values))

    def compute_sum_prevs(self) -> int:
        return sum((self.pred_prev(v) for v in self.values))
