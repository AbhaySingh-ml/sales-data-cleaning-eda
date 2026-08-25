from pathlib import Path


def generate_sales_report(
    sales_summary,
    monthly_revenue,
    top_products_revenue,
    top_products_quantity,
    customer_summary,
    country_summary,
    charts_dir,
    output_path
):
    """
    Generate an automated Markdown sales report.
    """

    charts_dir = Path(charts_dir)
    output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # Convert sales summary
    # -------------------------

    sales_metrics = dict(
        zip(
            sales_summary["Metric"],
            sales_summary["Value"]
        )
    )

    total_revenue = sales_metrics["Total Revenue"]
    total_orders = sales_metrics["Total Orders"]
    total_quantity = sales_metrics["Total Quantity"]
    average_order_value = sales_metrics["Average Order Value"]

    # -------------------------
    # Customer metrics
    # -------------------------

    number_of_customers = customer_summary["Customer ID"].nunique()

    average_customer_spend = customer_summary["total_spend"].mean()

    # -------------------------
    # Top product
    # -------------------------

    top_product = top_products_revenue.iloc[0]

    # -------------------------
    # Top country
    # -------------------------

    top_country = country_summary.sort_values(
        "revenue",
        ascending=False
    ).iloc[0]

    # -------------------------
    # Peak revenue month
    # -------------------------

    peak_month = monthly_revenue.loc[
        monthly_revenue["Revenue"].idxmax()
    ]

    # -------------------------
    # Build report
    # -------------------------

    report = f"""# Sales Analysis Report

## 1. Executive Summary

This report provides an analysis of sales performance across revenue,
orders, products, customers, and geographic markets.

### Key Findings

- **Total Revenue:** {total_revenue:,.2f}
- **Total Orders:** {total_orders:,.0f}
- **Total Quantity Sold:** {total_quantity:,.0f}
- **Average Order Value:** {average_order_value:,.2f}
- **Number of Customers:** {number_of_customers:,}
- **Average Customer Spend:** {average_customer_spend:,.2f}

The highest-revenue product was **{top_product["Description"]}**,
generating **{top_product["revenue"]:,.2f}** in revenue.

The highest-revenue country was **{top_country["Country"]}**,
generating **{top_country["revenue"]:,.2f}** in revenue.

The strongest revenue month was **{peak_month["Month"]}**,
with revenue of **{peak_month["Revenue"]:,.2f}**.

---

## 2. Sales Performance

### Overall KPIs

| Metric | Value |
|---|---:|
| Total Revenue | {total_revenue:,.2f} |
| Total Orders | {total_orders:,.0f} |
| Total Quantity Sold | {total_quantity:,.0f} |
| Average Order Value | {average_order_value:,.2f} |
| Number of Customers | {number_of_customers:,} |
| Average Customer Spend | {average_customer_spend:,.2f} |

### Monthly Revenue

![Monthly Revenue Trend](../results/charts/monthly_revenue.png)

---

## 3. Product Analysis

### Top Products by Revenue

| Product | Quantity Sold | Revenue |
|---|---:|---:|
"""

    for _, row in top_products_revenue.head(10).iterrows():
        report += (
            f'| {row["Description"]} '
            f'| {row["quantity_sold"]:,.0f} '
            f'| {row["revenue"]:,.2f} |\n'
        )

    report += """
### Top Products by Quantity Sold

![Top Products by Revenue](../results/charts/top_products_revenue.png)

![Top Products by Quantity](../results/charts/top_products_quantity.png)

---

## 4. Customer Analysis

### Customer Overview

- **Number of Customers:** {customers:,}
- **Average Customer Spend:** {avg_customer_spend:,.2f}

### Customer Revenue Distribution

![Customer Revenue Distribution](../results/charts/customer_revenue_distribution.png)

---

## 5. Geographic Analysis

### Top Countries by Revenue

| Country | Orders | Quantity Sold | Revenue |
|---|---:|---:|---:|
""".format(
        customers=number_of_customers,
        avg_customer_spend=average_customer_spend
    )

    for _, row in country_summary.sort_values(
        "revenue",
        ascending=False
    ).head(10).iterrows():

        report += (
            f'| {row["Country"]} '
            f'| {row["orders"]:,.0f} '
            f'| {row["quantity_sold"]:,.0f} '
            f'| {row["revenue"]:,.2f} |\n'
        )

    report += """
### Revenue by Country

![Revenue by Country](../results/charts/revenue_by_country.png)

---

## 6. Conclusion

The analysis provides a consolidated view of sales performance across
products, customers, time periods, and geographic markets.

The generated charts and tables can be reused for further business
analysis and reporting.

---

*Report generated automatically using Python, Pandas, and Matplotlib.*
"""

    output_path.write_text(
        report,
        encoding="utf-8"
    )

    return output_path