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

    # Colonnes
    assert list(df.columns) == ["age", "salaire", "departement"]

    # Nombre de lignes
    assert len(df) == 8

    # Types cohérents
    assert pd.api.types.is_integer_dtype(df["age"])
    assert pd.api.types.is_float_dtype(df["salaire"])

    # Vérifier que la colonne departement contient bien des strings
    assert df["departement"].map(type).eq(str).all()


def test_means():
    df = build_dataframe()
    assert mean_age(df) == pytest.approx(34.5)
    assert mean_salary(df) == pytest.approx(3775.0)


def test_filter_by_department_it():
    df = build_dataframe()
    filtered = filter_by_department(df, "IT")

    assert len(filtered) == 4
    assert (filtered["departement"] == "IT").all()


def test_row_count():
    df = build_dataframe()
    assert row_count(df) == 8


def test_mean_salary_missing_column():
    df = pd.DataFrame({"age": [25, 30]})  # manque "salaire"
    with pytest.raises(ValueError):
        mean_salary(df)
