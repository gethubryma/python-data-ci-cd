import pandas as pd


def build_dataframe() -> pd.DataFrame:
    data = {
        "age": [25, 30, 22, 45, 35, 28, 50, 41],
        "salaire": [2800.0, 3200.0, 2100.0, 5000.0, 3800.0, 2600.0, 6200.0, 4500.0],
        "departement": ["IT", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    }

    df = pd.DataFrame(data)
    return df

def mean_age(df: pd.DataFrame) -> float:
    if "age" not in df.columns:
        raise ValueError("Le DataFrame doit contenir la colonne 'age'")
    return float(df["age"].mean())


def mean_salary(df: pd.DataFrame) -> float:
    if "salaire" not in df.columns:
        raise ValueError("Le DataFrame doit contenir la colonne 'salaire'")
    return float(df["salaire"].mean())


def filter_by_department(df: pd.DataFrame, dept: str) -> pd.DataFrame:
    if "departement" not in df.columns:
        raise ValueError("Le DataFrame doit contenir la colonne 'departement'")
    return df[df["departement"] == dept].copy()


def row_count(df: pd.DataFrame) -> int:
    return int(len(df))



