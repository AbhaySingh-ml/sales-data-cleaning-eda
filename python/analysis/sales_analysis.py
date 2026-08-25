import pandas as pd


def calculate_total_revenue(df: pd.DataFrame) -> float:
    """Calculate total revenue from sales transactions."""

    revenue = (df["Quantity"] * df["Price"]).sum()

    return float(revenue)


def calculate_total_orders(df: pd.DataFrame) -> int:
    """Calculate the number of unique orders."""

    return int(df["Invoice"].nunique())

def calculate_total_quantity(df: pd.DataFrame) -> int:
    """Calculate total quantity sold."""

    return int(df["Quantity"].sum())


def calculate_average_order_value(df: pd.DataFrame) -> float:
    """Calculate average revenue per order."""

    total_revenue = calculate_total_revenue(df)
    total_orders = calculate_total_orders(df)

    return total_revenue / total_orders


def calculate_monthly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total revenue by month."""

    monthly_revenue = (
        df.assign(
            Month=df["InvoiceDate"].dt.to_period("M"),
            Revenue=df["Quantity"] * df["Price"]
        )
        .groupby("Month", as_index=False)["Revenue"]
        .sum()
    )

    return monthly_revenue


def calculate_monthly_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate unique orders by month."""

    monthly_orders = (
        df.assign(
            Month=df["InvoiceDate"].dt.to_period("M")
        )
        .groupby("Month")["Invoice"]
        .nunique()
        .reset_index(name="Orders")
    )

    return monthly_orders