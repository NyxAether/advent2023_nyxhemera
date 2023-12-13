from pathlib import Path
import os
import pytest
from advent2023.aoc_utils import parse_seeds
from advent2023.aoc5.almanach import Almanach

@pytest.fixture
def setup_data():
    fp = Path(os.path.dirname(os.path.realpath(__file__))).parent.parent / "data/tests/aoc5_test.txt"
    print(fp)
    al = Almanach(*(parse_seeds(fp)))
    print("\nSetting up resources...")
    yield al  # Provide the data to the test
    # Teardown: Clean up resources (if any) after the test
    print("\nTearing down resources...")


def test_get_position(setup_data):
    al= setup_data
    assert al.get_position(79) == 82
    assert al.get_position(14) == 43
    assert al.get_position(55) == 86
    assert al.get_position(13) == 35

def test_find_closest_position(setup_data):
    al= setup_data
    assert al.find_closest_position() == 35
