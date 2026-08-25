import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load and combine both sheets from the Online Retail II dataset."""

    df_2009_2010 = pd.read_excel(
        file_path,
        sheet_name="Year 2009-2010"
    )

    df_2010_2011 = pd.read_excel(
        file_path,
        sheet_name="Year 2010-2011"
    )

    df = pd.concat(
        [df_2009_2010, df_2010_2011],
        ignore_index=True
    )

    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove exact duplicate transaction rows."""

    return df.drop_duplicates().copy()


def remove_invalid_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only valid positive-quantity and positive-price sales."""

    mask = (
        (df["Quantity"] > 0)
        & (df["Price"] > 0)
        & (~df["Invoice"].astype(str).str.startswith("C"))
    )

    return df.loc[mask].copy()


def generate_cleaning_summary(
    raw_df: pd.DataFrame,
    cleaned_df: pd.DataFrame
) -> dict:
    """Generate a summary of the cleaning process."""

    duplicate_rows = raw_df.duplicated().sum()

    invalid_sales = (
        (raw_df["Quantity"] <= 0)
        | (raw_df["Price"] <= 0)
        | (raw_df["Invoice"].astype(str).str.startswith("C"))
    ).sum()

    summary = {
        "raw_rows": len(raw_df),
        "duplicate_rows": int(duplicate_rows),
        "invalid_sales_rows": int(invalid_sales),
        "clean_rows": len(cleaned_df),
        "rows_removed": len(raw_df) - len(cleaned_df),
    }

    return summary

def clean_sales_data(file_path: str) -> tuple[pd.DataFrame, dict]:
    """Run the complete sales-data cleaning pipeline."""

    raw_df = load_data(file_path)

    df = remove_duplicates(raw_df)

    df = remove_invalid_sales(df)

    summary = generate_cleaning_summary(
        raw_df,
        df
    )

    return df, summary


if __name__ == "__main__":
    file_path = "../../data/raw/online_retail_II.xlsx"

    cleaned_df, summary = clean_sales_data(file_path)

    print("Cleaning Summary")
    print("-" * 30)

    for key, value in summary.items():
        print(f"{key}: {value:,}")