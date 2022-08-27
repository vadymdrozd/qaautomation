import pytest
import pandas
from pathlib import Path
from game_dice import Game


def pytest_generate_tests(metafunc):
    if 'negative' in metafunc.function.__name__:
        incorrect_test_data = tuple(
            pandas.read_csv(Path('test_data', f'{metafunc.function.__name__}.csv'), delimiter=",").itertuples(index=False,
                                                                                                              name=None))
        metafunc.parametrize("first, second, third", incorrect_test_data)
    elif 'positive' in metafunc.function.__name__:
        correct_test_data = tuple(
            pandas.read_csv(Path('test_data', f'{metafunc.function.__name__}.csv'), delimiter=",").itertuples(index=False,
                                                                                                              name=None))
        metafunc.parametrize("first, second, third, result", correct_test_data)


class TestDicesCombinations:
    def test_positive_combinations(self,
                                   first: int,
                                   second: int,
                                   third: int,
                                   result: int):
        dice_game = Game().throw(first, second, third)
        assert result == dice_game, f'Incorrect game result - {dice_game}. Should be {result}'

    def test_negative_combinations(self,
                                   first: int,
                                   second: int,
                                   third: int):
        with pytest.raises(ValueError):
            Game().throw(first, second, third)
