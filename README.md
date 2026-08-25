# Sales Data Cleaning, EDA & Automated Reporting qqq1

An end-to-end Python data analytics project that transforms raw transactional retail data into structured business insights, visualizations, and an automatically generated sales report.

The project covers the complete analytical workflow from data cleaning and validation to sales, product, customer, and geographic analysis, followed by visualization and automated reporting.

---

## Business Objective

The objective is to analyze transactional retail data and answer practical business questions such as:

- What is the overall sales performance?
- How does revenue change over time?
- Which products generate the most revenue?
- Which products sell the highest quantity?
- Which customers contribute the most revenue?
- How many orders does each customer place?
- Which countries generate the most revenue?
- How can the analytical results be converted into a reusable automated report?

The project separates data preparation, analytical logic, visualization, and reporting into independent Python modules.

---

## Project Workflow

```text
Raw Transactional Data
        │
        ▼
Data Cleaning & Validation
        │
        ▼
   Cleaned Sales Data
        │
        ├───────────────┐
        ▼               ▼
 Sales Analysis   Product Analysis
        │               │
        └───────┬───────┘
                ▼
        Customer Analysis
                │
                ▼
       Geographic Analysis
                │
                ▼
          Visualization
                │
                ▼
       Automated Reporting
                │
                ▼
      Sales Analysis Report
```

---

## Dataset

The project uses the **Online Retail II** transactional dataset.

The dataset contains retail transaction records with information including:

| Column | Description |
|---|---|
| `Invoice` | Transaction/invoice identifier |
| `StockCode` | Product identifier |
| `Description` | Product description |
| `Quantity` | Number of units purchased |
| `InvoiceDate` | Transaction date and time |
| `Price` | Unit price |
| `Customer ID` | Customer identifier |
| `Country` | Customer's country |

> The raw dataset is intentionally excluded from version control because of its size.

---

## Analytical Modules

### 1. Data Cleaning

The first stage prepares the raw transactional data for analysis.

The cleaning workflow handles data-quality issues and produces a structured dataset suitable for downstream analysis.

The cleaned dataset is generated locally under:

```
data/processed/cleaned_sales.csv
```

> The raw and processed datasets are excluded from Git because of their file sizes.

---

### 2. Sales Analysis

The sales analysis focuses on overall business performance and revenue trends.

**Key metrics include:**

- Total revenue
- Total orders
- Total quantity sold
- Average order value
- Monthly revenue

**Verified Results**

| Metric | Value |
|---|---:|
| Total Revenue | 20,476,260.45 |
| Total Orders | 40,077 |
| Total Quantity Sold | 11,205,148 |
| Average Order Value | 510.92 |

The analysis also produces a monthly revenue dataset used for trend visualization.

---

### 3. Product Analysis

Product-level analysis evaluates product performance from two perspectives:

**Revenue Performance**

Identifies products that generate the highest revenue.

**Quantity Performance**

Identifies products that sell the highest number of units.

Keeping these analyses separate is important because the product with the highest sales quantity is not necessarily the product generating the highest revenue.

**Outputs include:**

- Top products by revenue
- Top products by quantity
- Product-level revenue
- Product-level quantity sold

---

### 4. Customer Analysis

Customer-level analysis examines purchasing behavior and customer value.

**The analysis includes:**

- Number of customers
- Total customer spend
- Top customers by spend
- Orders per customer
- Average customer spend

**Verified Results**

| Metric | Value |
|---|---:|
| Number of Customers | 5,878 |
| Average Customer Spend | 2,955.90 |

This converts transaction-level data into a customer-level view of business activity.

---

### 5. Geographic Analysis

Geographic analysis evaluates sales performance across countries.

**The analysis examines:**

- Revenue by country
- Orders by country
- Quantity sold by country
- Country-level sales contribution

This helps identify important geographic markets and differences in sales activity between countries.

---

## Visualization

The visualization layer converts analytical results into business-oriented charts.

The project generates the following visualizations:

- Monthly Revenue Trend
- Top Products by Revenue
- Top Products by Quantity
- Customer Revenue Distribution
- Revenue by Country

All charts are generated programmatically using Python and saved under:

```
results/charts/
```

---

## Automated Reporting

One of the main engineering components of this project is the automated reporting layer.

Instead of manually copying analytical results and charts into a report, the project uses a reusable Python report generator.

**The reporting workflow is:**

```text
Analytical DataFrames
        +
Generated Charts
        │
        ▼
  Report Generator
        │
        ▼
  sales_report.md
```

The report generator receives the outputs from the analytical modules and assembles them into a structured Markdown report.

The final report is generated at:

```
reports/sales_report.md
```

**The report contains:**

- Executive summary
- Sales KPIs
- Monthly revenue analysis
- Product analysis
- Customer analysis
- Geographic analysis
- Generated visualizations

This makes the reporting process reproducible instead of manually assembled.

---

## Generated Outputs

The project produces reusable analytical outputs including:

```
results/
├── sales_summary.csv
│
└── charts/
    ├── monthly_revenue.png
    ├── top_products_revenue.png
    ├── top_products_quantity.png
    ├── customer_revenue_distribution.png
    └── revenue_by_country.png
```

The automated report is generated under:

```
reports/
└── sales_report.md
```

---

## Python Architecture

The project separates responsibilities across different modules.

```
python/
│
├── cleaning/
│   └── clean_sales_data.py
│
├── analysis/
│   ├── sales_analysis.py
│   ├── product_analysis.py
│   ├── customer_analysis.py
│   └── geographic_analysis.py
│
├── visualization/
│   └── charts.py
│
└── reports/
    └── generate_report.py
```

The architecture follows a separation-of-concerns approach:

```text
Cleaning
   │
   ▼
Analysis
   │
   ▼
Visualization
   │
   ▼
Reporting
```

Each layer has a distinct responsibility rather than placing the entire workflow inside one large notebook or script.

---

## Project Structure

```
sales-data-cleaning-eda/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── data/
│   ├── raw/                  # Local raw dataset
│   └── processed/            # Locally generated cleaned dataset
│
├── notebooks/
│   └── sales_eda.ipynb       # Main exploratory analysis
│
├── python/
│   ├── __init__.py
│   │
│   ├── cleaning/
│   │   ├── __init__.py
│   │   └── clean_sales_data.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── sales_analysis.py
│   │   ├── product_analysis.py
│   │   ├── customer_analysis.py
│   │   └── geographic_analysis.py
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   └── charts.py
│   │
│   └── reports/
│       ├── __init__.py
│       └── generate_report.py
│
├── results/
│   ├── sales_summary.csv
│   └── charts/
│
└── reports/
    └── sales_report.md
```

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
cd sales-data-cleaning-eda
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Linux / WSL**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add the dataset

Place the source dataset inside:

```
data/raw/
```

> The raw dataset and generated processed dataset are excluded from Git because of their size.

### 6. Run the notebook

Open:

```
notebooks/sales_eda.ipynb
```

and execute the analysis workflow.

### 7. Generate the report

The reporting module can be used to generate the final Markdown report from the analytical outputs.

---

## Technical Stack

| Category | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Data Input | OpenPyXL |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |

---

## Project Outcome

This project demonstrates an end-to-end data analytics workflow rather than isolated Pandas operations.

**The final pipeline connects:**

```text
Raw Data
   │
   ▼
Data Cleaning
   │
   ▼
Business Analysis
   │
   ▼
Customer / Product / Geographic Analysis
   │
   ▼
Visualization
   │
   ▼
Automated Reporting
```

The resulting workflow can be adapted to similar transactional sales datasets and can serve as a foundation for further analytics, dashboards, or machine learning applications.

---

## Future Extensions

Potential extensions include:

- Interactive dashboard development
- Sales forecasting
- Customer segmentation
- Customer lifetime value analysis
- Customer churn prediction
- Product recommendation systems
- Automated scheduled reporting
- Deployment as a data analytics application

---

## Author

**Abhay Singh**
MCA — AI/ML

Interested in building data-driven systems at the intersection of machine learning, business analytics, and financial technology.
