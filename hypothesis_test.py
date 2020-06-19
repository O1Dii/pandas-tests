from hypothesis import given
from hypothesis.extra.pandas import data_frames, column
from main import sum
import pandas


@given(data_frames([
    column('1', dtype='float'),
    column('2', dtype='float')
]))
def test_sum(monkeypatch, df):
    with monkeypatch.context() as context:
        def read_csv_mock(*args):
            return df

        context.setattr(pandas, 'read_csv', read_csv_mock)

        result = sum()

    assert len(result.columns) == 3
    assert result['3'].dtype == 'float'
