import pandas as pd


def create_customer_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create customer-level sales metrics.
    """

    df = df.copy()

    # Customer-level analysis requires a valid Customer ID
    df = df.dropna(subset=["Customer ID"])

    # Calculate transaction-level revenue
    df["Revenue"] = df["Quantity"] * df["Price"]

    customer_summary = (
        df.groupby("Customer ID", as_index=False)
        .agg(
            total_spend=("Revenue", "sum"),
            orders=("Invoice", "nunique"),
            quantity_sold=("Quantity", "sum")
        )
    )

    return customer_summary


def get_top_customers_by_spend(
    customer_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return the top customers ranked by total spend.
    """

    return (
        customer_summary
        .sort_values("total_spend", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def calculate_average_customer_spend(
    customer_summary: pd.DataFrame
) -> float:
    """
    Calculate the average total spend per customer.
    """

    return customer_summary["total_spend"].mean()


def get_customers_by_order_count(
    customer_summary: pd.DataFrame,
    n: int = 10
) -> pd.DataFrame:
    """
    Return customers with the highest number of orders.
    """

    return (
        customer_summary
        .sort_values("orders", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )