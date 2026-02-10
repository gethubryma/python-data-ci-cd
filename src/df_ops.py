import pandas as pd


def build_dataframe() -> pd.DataFrame:
    data = {
        "age": [25, 30, 22, 45, 35, 28, 50, 41],
        "salaire": [2800.0, 3200.0, 2100.0, 5000.0, 3800.0, 2600.0, 6200.0, 4500.0],
        "departement": ["IT", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    }
    return pd.DataFrame(data)


def _check_columns(df: pd.DataFrame, required: list[str]) -> None:
    """Vérifie que le DataFrame contient les colonnes attendues."""
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Colonnes manquantes dans le DataFrame : {missing}")


def mean_age(df: pd.DataFrame) -> float:
    _check_columns(df, ["age"])
    return float(df["age"].mean())


def mean_salary(df: pd.DataFrame) -> float:
    _check_columns(df, ["salaire"])
    return float(df["salaire"].mean())


def filter_by_department(df: pd.DataFrame, dept: str) -> pd.DataFrame:
    _check_columns(df, ["departement"])
    return df[df["departement"] == dept]


def row_count(df: pd.DataFrame) -> int:
    return len(df)
