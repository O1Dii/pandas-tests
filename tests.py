import unittest
from unittest.mock import Mock, patch

import pandas as pd
from numpy import nan

from main import sum


class TestMain(unittest.TestCase):
    @patch("pandas.read_csv")
    def test_sum_basic(self, read_csv_mock: Mock):
        read_csv_mock.return_value = pd.DataFrame({'1': [1, 2, 3], '2': [3, 2, 1]})
        results = sum()
        read_csv_mock.assert_called_once()

        pd.testing.assert_frame_equal(results, pd.DataFrame({'1': [1, 2, 3], '2': [3, 2, 1], '3': [4, 4, 4]}))

    @patch("pandas.read_csv")
    def test_sum_with_nan(self, read_csv_mock: Mock):
        read_csv_mock.return_value = pd.DataFrame({'1': [nan, nan, 3], '2': [3, nan, 1]})
        results = sum()
        read_csv_mock.assert_called_once()

        pd.testing.assert_frame_equal(results, pd.DataFrame({'1': [nan, nan, 3], '2': [3, nan, 1], '3': [nan, nan, 4]}))

    @patch("pandas.read_csv")
    def test_sum_with_strings(self, read_csv_mock: Mock):
        read_csv_mock.return_value = pd.DataFrame({'1': ['a', 2, 3], '2': [3, 2, 1]})

        with self.assertRaises(TypeError):
            sum()

        read_csv_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
