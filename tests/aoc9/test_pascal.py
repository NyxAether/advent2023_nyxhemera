from advent2023.aoc9.pascal import Pascal


def test_compute_sum_preds():
    assert Pascal([[10, 13, 16, 21, 30, 45]]).compute_sum_preds() == 68
    assert Pascal([[30, 35, 41, 47, 52]]).compute_sum_preds() == 55
    assert Pascal([[3, 4, 6, 12, 24, 43, 69]]).compute_sum_preds() == 101
    assert (
        Pascal(
            [[10, 13, 16, 21, 30, 45],
             [30, 35, 41, 47, 52],
             [3, 4, 6, 12, 24, 43, 69]]
        ).compute_sum_preds()
        == 224
    )
def test_compute_sum_prevs():
    assert Pascal([[10, 13, 16, 21, 30, 45]]).compute_sum_prevs() == 5
    assert Pascal([[30, 35, 41, 47, 52]]).compute_sum_prevs() == 27
    assert Pascal([[3, 4, 6, 12, 24, 43, 69]]).compute_sum_prevs() == -1
    assert (
        Pascal(
            [[10, 13, 16, 21, 30, 45],
             [30, 35, 41, 47, 52],
             [3, 4, 6, 12, 24, 43, 69]]
        ).compute_sum_prevs()
        == 31
    )
