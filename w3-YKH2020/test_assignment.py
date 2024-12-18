import numpy as np
import math
import pandas as pd
import pytest
from testbook import testbook


# Set up a shared notebook context to speed up tests.
@pytest.fixture(scope='module')
def tb():
    with testbook('assignment.ipynb', execute=True) as tb:
        yield tb


def test_df1(tb):
    df = tb.get("df1")
    assert hasattr(df, 'empty'), "df1 variable doesn't seem to be a dataframe"
    assert df.empty == False, "df1 variable seems to be empty"


def test_df1_dict(tb):
    result = tb.get("df1_dict")
    assert hasattr(result, 'keys'), "df1_dict does not seem to be a dictionary"
    length = len(result['age'])
    assert length == 15, f"Expected resulting dictionary to have 15 items but it has {length}"


def test_df2(tb):
    df2 = tb.get("df2")
    assert hasattr(df2, 'empty'), "df2 variable doesn't seem to be a dataframe"
    assert df2.empty == False, "df2 variable seems to be empty"


def test_df2_dropped_nan(tb):
    result = tb.get("df2")
    rows, columns = result.shape
    assert rows == 319, "df2 does not reflect the expected number of rows"


def test_df3(tb):
    result = tb.get("df3")
    assert hasattr(result, 'to_dict'), "Doesn't look like df3 is a Pandas DataFrame"
    df = pd.DataFrame.from_dict(result.to_dict())
    count, _ = df.shape
    assert count == 5, f"Expected to get 5 matching rows but got {count}"


def test_df4(tb):
    result = tb.get("df4")
    assert hasattr(result, 'to_dict'), "Doesn't look like df4 is a Pandas DataFrame"
    df = pd.DataFrame.from_dict(result.to_dict())
    count, _ = df.shape
    assert count == 20, f"Expected to get 20 matching rows but got {count}"
    assert all(df["weight"] > 150), "Expected all entries to be over 150. Some entries aren't"


def test_df5(tb):
    result = tb.get("df5")
    assert hasattr(result, 'to_dict'), "Doesn't look like df5 is a Pandas DataFrame"
    df = pd.DataFrame.from_dict(result.to_dict())
    count, _ = df.shape
    assert count == 2, f"Expected to get 2 matching rows but got {count}"
    assert df.state.to_list() == ['California', 'California'], "Doesn't look like the matching states are from California"
    assert sorted(df.weight.to_list()) == [231.0, 242.0]


def test_df6(tb):
    result = tb.get("df6")
    assert hasattr(result, 'to_dict'), "Doesn't look like df6 is a Pandas DataFrame"
    df = pd.DataFrame.from_dict(result.to_dict())
    count, _ = df.shape
    assert count == 7, f"Expected to get 7 matching rows but got {count}"
    invalid_names = [i for i in df['first'].to_list() if 'al' not in i]
    assert invalid_names == [], "Expected to have only names that have 'al' in them"


def test_df7(tb):
    result = tb.get("df7")
    assert hasattr(result, 'to_dict'), "Doesn't look like df7 is a Pandas DataFrame"
    df = pd.DataFrame.from_dict(result.to_dict())
    # this is weird, but because testbook doesn't keep types, NaN is actually a string 'nan'
    # which is what we have to check for in here
    nans, _ = df.query('weight == "nan"').shape
    assert nans == 0, f"There are still {nans} NaN left in the weight column"
    zeros, _ = df.query('weight == 0').shape
    assert zeros == 81, "Expected to have at least 81 rows with a weight of 0"


def test_df8(tb):
    result = tb.get("df8")
    assert hasattr(result, 'to_dict'), "Doesn't look like df8 is a Pandas DataFrame"
    df = pd.DataFrame.from_dict(result.to_dict())
    assert df.get('health_issue') is not None, "Couldn't find a health_issue column"
    count, _ = df.query('health_issue == 1').shape
    assert count == 14, "Expected 14 entries with a 1 in the health_issue column"


def test_df9(tb):
    result = tb.get("df9")
    assert hasattr(result, 'to_dict'), "Doesn't look like df9 is a Pandas DataFrame"
    df = pd.DataFrame.from_dict(result.to_dict())
    count, _ = df.query("state == 'N. Carolina'").shape
    bad_count, _ = df.query("state == 'North Carolina'").shape
    assert count > 0, "Expected N. Carolina but didn't find any"
    assert bad_count == 0, "Found North Carolina in state but expected N. Carolina"


def test_array_split_1(tb):
    # Get the result first
    result = tb.get("array_split_1")
    assert hasattr(result, 'tolist'), "Doesn't look like array_split_1 is a NumPy array"
    # Conver to list which is serializable
    result_items = result.tolist()
    # Now load as an array again (!) so that we can compare
    array = np.array(result_items)
    assert all(array > 15), "Not all items in array_split_1 are over 15"


def test_array_split_2(tb):
    # Get the result first
    result = tb.get("array_split_2")
    assert hasattr(result, 'tolist'), "Doesn't look like array_split_2 is a NumPy array"
    # Conver to list which is serializable
    result_items = result.tolist()
    # Now load as an array again (!) so that we can compare
    array = np.array(result_items)
    assert all(array > 15), "Not all items in array_split_2 are over 15"
