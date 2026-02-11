import pytest
import pandas as pd

from src.df_ops import (
    build_dataframe,
    mean_age,
    mean_salary,
    filter_by_department,
    row_count,
)


def test_build_dataframe():
    df = build_dataframe()

    # Colonnes
    assert list(df.columns) == ["age", "salaire", "departement"]

    # 8 lignes
    assert len(df) == 8

    # Types 
    assert pd.api.types.is_integer_dtype(df["age"])
    assert pd.api.types.is_float_dtype(df["salaire"])
    assert pd.api.types.is_string_dtype(df["departement"])



def test_means():
    df = build_dataframe()
    assert mean_age(df) == 34.5
    assert mean_salary(df) == pytest.approx(3775.0)


def test_filter_by_department_it():
    df = build_dataframe()
    filtered = filter_by_department(df, "IT")

    assert len(filtered) == 4
    assert (filtered["departement"] == "IT").all()


def test_row_count():
    df = build_dataframe()
    assert row_count(df) == 8

def test_missing_columns_all_functions():
    df1 = pd.DataFrame({"salaire": [1000.0]})
    df2 = pd.DataFrame({"age": [25]})
    df3 = pd.DataFrame({"age": [25], "salaire": [2000.0]})

    with pytest.raises(ValueError):
        mean_age(df1)

    with pytest.raises(ValueError):
        mean_salary(df2)

    with pytest.raises(ValueError):
        filter_by_department(df3, "IT")
