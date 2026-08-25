import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_monthly_revenue(
    monthly_revenue: pd.DataFrame,
    output_dir: Path
):
    output_dir.mkdir(parents=True, exist_ok=True)

    data = monthly_revenue.copy()

    # Convert Pandas Period values to timestamps for Matplotlib
    data["Month"] = data["Month"].dt.to_timestamp()

    plt.figure(figsize=(12, 6))

    plt.plot(
        data["Month"],
        data["Revenue"],
        marker="o"
    )

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_path = output_dir / "monthly_revenue.png"
    plt.savefig(output_path, dpi=150)
    plt.show()
    plt.close()

    return output_path


def plot_top_products_by_revenue(
    top_products_revenue: pd.DataFrame,
    output_dir: Path
):
    output_dir.mkdir(parents=True, exist_ok=True)

    data = top_products_revenue.sort_values(
        "revenue",
        ascending=True
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        data["Description"],
        data["revenue"]
    )

    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    plt.tight_layout()

    output_path = output_dir / "top_products_revenue.png"
    plt.savefig(output_path, dpi=150)
    plt.show()
    plt.close()

    return output_path


def plot_top_products_by_quantity(
    top_products_quantity: pd.DataFrame,
    output_dir: Path
):
    output_dir.mkdir(parents=True, exist_ok=True)

    data = top_products_quantity.sort_values(
        "quantity_sold",
        ascending=True
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        data["Description"],
        data["quantity_sold"]
    )

    plt.title("Top 10 Products by Quantity Sold")
    plt.xlabel("Quantity Sold")
    plt.ylabel("Product")
    plt.tight_layout()

    output_path = output_dir / "top_products_quantity.png"
    plt.savefig(output_path, dpi=150)
    plt.show()
    plt.close()

    return output_path


def plot_customer_revenue_distribution(
    customer_summary: pd.DataFrame,
    output_dir: Path
):
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))

    plt.hist(
        customer_summary["total_spend"],
        bins=30
    )

    plt.title("Customer Revenue Distribution")
    plt.xlabel("Customer Spend")
    plt.ylabel("Number of Customers")
    plt.tight_layout()

    output_path = output_dir / "customer_revenue_distribution.png"
    plt.savefig(output_path, dpi=150)
    plt.show()
    plt.close()

    return output_path


def plot_revenue_by_country(
    country_summary: pd.DataFrame,
    output_dir: Path,
    n: int = 10
):
    output_dir.mkdir(parents=True, exist_ok=True)

    data = (
        country_summary
        .sort_values("revenue", ascending=True)
        .tail(n)
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        data["Country"],
        data["revenue"]
    )

    plt.title("Top 10 Countries by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Country")
    plt.tight_layout()

    output_path = output_dir / "revenue_by_country.png"
    plt.savefig(output_path, dpi=150)
    plt.show()
    plt.close()

    return output_path