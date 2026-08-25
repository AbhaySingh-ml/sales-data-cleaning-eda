import pandas as pd


def create_product_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create product-level sales metrics.

    Returns:
        DataFrame containing:
        - StockCode
        - Description
        - quantity_sold
        - revenue
    """

    df = df.copy()

    # Calculate transaction-level revenue
    df["Revenue"] = df["Quantity"] * df["Price"]

    # Select the most frequent description for each product
    canonical_description = (
        df.groupby("StockCode")["Description"]
        .agg(lambda x: x.mode().iloc[0])
    )

    # Aggregate sales metrics by product
    product_summary = (
        df.groupby("StockCode", as_index=False)
        .agg(
            quantity_sold=("Quantity", "sum"),
            revenue=("Revenue", "sum")
        )
    )

    # Attach canonical product descriptions
    product_summary["Description"] = (
        product_summary["StockCode"]
        .map(canonical_description)
    )

    return product_summary[
        ["StockCode", "Description", "quantity_sold", "revenue"]
    ]


def get_top_products_by_revenue(
    product_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the top products ranked by revenue.
    """

    return (
        product_summary
        .sort_values("revenue", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )

def get_top_products_by_revenue(
    product_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the top products ranked by revenue.
    """

    return (
        product_summary
        .sort_values("revenue", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )

def get_top_products_by_quantity(
    product_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the top products ranked by quantity sold.
    """

    return (
        product_summary
        .sort_values("quantity_sold", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def get_worst_products_by_revenue(
    product_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the products with the lowest revenue.
    """

    return (
        product_summary
        .sort_values("revenue", ascending=True)
        .head(n)
        .reset_index(drop=True)
    )


def calculate_revenue_contribution(
    product_summary: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate each product's percentage contribution
    to total revenue.
    """

    total_revenue = product_summary["revenue"].sum()

    product_summary = product_summary.copy()

    product_summary["revenue_contribution_pct"] = (
        product_summary["revenue"] / total_revenue * 100
    )

    return product_summary