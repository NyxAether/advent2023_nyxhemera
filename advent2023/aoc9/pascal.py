import numpy as np


class Pascal:
    def __init__(self, values: list[list[int]]) -> None:
        self.values = [np.array(value).astype("int64") for value in values]



    def find_pascal(self, series: np.ndarray) -> np.ndarray:
        
        current = series.copy()
        computed_values = [current[-1]]
        sub=np.array([1,-1])
        while any(current !=0):
            current = np.convolve(current,sub)[1:-1]
            computed_values.append(current[-1])
        return np.array(computed_values).astype("int64")

    def pred_next(self, series: np.ndarray) -> int:
        computed_values = self.find_pascal(series)
        return computed_values.sum()

    def compute_sum_preds(self) -> int:
        return sum([self.pred_next(v) for v in self.values])
