import pytest
import pandas as pd

from src.df_ops import (
    build_dataframe,
    mean_age,
    mean_salary,
    filter_by_department,
    row_count,
)


def test_build_dataframe_structure_and_types():
    df = build_dataframe()

    # Colonnes attendues
    assert list(df.columns) == ["age", "salaire", "departement"]

    # 8 lignes
    assert len(df) == 8

    # Types cohérents (int / float / string)
    assert pd.api.types.is_integer_dtype(df["age"])
    assert pd.api.types.is_float_dtype(df["salaire"])
    assert pd.api.types.is_object_dtype(df["departement"])  # string en pandas = object


def test_means():
    df = build_dataframe()

    assert mean_age(df) == pytest.approx(34.5)
    assert mean_salary(df) == pytest.approx(3775.0)


def test_filter_by_department_it():
    df = build_dataframe()

    filtered = filter_by_department(df, "IT")

    # Nombre de lignes IT attendu
    assert len(filtered) == 4

    # Toutes les lignes doivent être IT
    assert (filtered["departement"] == "IT").all()


def test_row_count():
    df = build_dataframe()
    assert row_count(df) == 8
