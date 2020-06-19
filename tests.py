import unittest
from unittest.mock import Mock, patch

from hypothesis import given
from hypothesis.extra.pandas import column, data_frames

from main import sum


class TestMain(unittest.TestCase):
    @given(df=data_frames([
        column('1', dtype='float'),
        column('2', dtype='float')
    ]))
    @patch("pandas.read_csv")
    def test_sum_basic(self, read_csv_mock: Mock, df):
        read_csv_mock.return_value = df
        results = sum()
        read_csv_mock.assert_called_once()

        self.assertEqual(len(results.columns), 3)
        self.assertEqual(results['3'].dtype, 'float')


if __name__ == '__main__':
    unittest.main()
