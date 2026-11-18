import pandas as pd
import pytest

from src.data.loader import load_data


def test_load_real_data():
    df = load_data()
    assert df.shape == (12000, 18)


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_data("not_a_real_file.csv")


def test_missing_column_raises(tmp_path):
    bad = pd.DataFrame({"month": ["nov"]})
    file = tmp_path / "bad.csv"
    bad.to_csv(file, index=False)
    with pytest.raises(ValueError):
        load_data(str(file))
