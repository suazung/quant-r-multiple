


import pandas as pd

def load_and_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Clean date
    df["date"] = df["date"].str.replace("'", "", regex=False)
    df["date"] = pd.to_datetime(df["date"])

    # Sort by time
    df = df.sort_values("date").reset_index(drop=True)

    # Drop index-like columns if needed
    if "No." in df.columns:
        df = df.drop(columns=["No."])

    return df


def validate_schema(df: pd.DataFrame):
    assert "max_rr" in df.columns, "Missing max_rr column"
    assert df["max_rr"].isna().sum() == 0, "NaN found in max_rr"
    assert df["date"].is_monotonic_increasing, "Date not sorted"

    return True