import numpy as np
from scipy.special import comb


class Pascal:
    def __init__(self, values: list[list[int]]) -> None:
        self.values = np.array(values).astype("int64")
        self.pascal = {2: np.array([1, -1])}

    def add_pascal(self, size: int) -> None:
        self.pascal[size] = np.array(
            [((-1) ** (i % 2)) * comb(size - 1, i) for i in range(size)]
        ).astype("int64")

    def get_pascal(self, size: int) -> np.ndarray:
        if size not in self.pascal:
            self.add_pascal(size)
        return self.pascal[size]

    def find_pascal(self, series: np.ndarray) -> np.ndarray:
        n = 2
        computed_values = [series[-1]]
        next_val=np.sum(series[-(n):][::-1] * self.get_pascal(n))
        while (computed_values[-1] != 0 or next_val != 0) and n < len(series):
            computed_values.append(next_val)
            next_val =np.sum(series[-(n+1):][::-1] * self.get_pascal(n+1))
            n += 1
        return np.array(computed_values[::-1]).astype("int64")

    def pred_next(self, series: np.ndarray) -> int:
        computed_values = self.find_pascal(series)
        return computed_values.sum()

    def compute_sum_preds(self) -> int:
        return np.sum(np.vectorize(self.pred_next, signature="(i) -> ()")(self.values))
