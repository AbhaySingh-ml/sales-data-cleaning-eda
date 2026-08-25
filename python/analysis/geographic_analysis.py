import pandas as pd


def create_country_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create country-level sales metrics.
    """

    df = df.copy()

    # Calculate transaction-level revenue
    df["Revenue"] = df["Quantity"] * df["Price"]

    country_summary = (
        df.groupby("Country", as_index=False)
        .agg(
            revenue=("Revenue", "sum"),
            orders=("Invoice", "nunique"),
            quantity_sold=("Quantity", "sum")
        )
    )

    return country_summary


def get_top_countries_by_revenue(
    country_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the top countries ranked by revenue.
    """

    return (
        country_summary
        .sort_values("revenue", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def get_top_countries_by_orders(
    country_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the top countries ranked by number of orders.
    """

    return (
        country_summary
        .sort_values("orders", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def get_top_markets(
    country_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the top markets ranked by revenue.
    
    This is intentionally based on revenue because
    revenue represents commercial market importance.
    """

    return (
        country_summary
        .sort_values("revenue", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )