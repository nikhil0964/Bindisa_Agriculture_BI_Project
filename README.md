# Yearly Agricultural Data Analytics and Business Intelligence System

## Company

Bindisa Agriculture Private Limited

## Project Overview

This project is a professional agriculture analytics and business intelligence system designed for yearly crop, cost, revenue, profit, weather, and yield analysis. It uses Python for data generation, analytics, visual reporting, Excel dashboard export, and machine learning. MySQL is used as the SQL data warehouse. Power BI and Advanced Excel are used for business intelligence dashboards.

## Technology Stack

- Python
- MySQL / Advanced SQL
- Advanced Excel
- Power BI
- Machine Learning

## Folder Structure

```text
Bindisa_Agriculture_BI_Project/
├── data/
├── docs/
├── excel/
├── powerbi/
├── python/
├── reports/
└── sql/
```

## How To Run

1. Install Python.
2. Install required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl sqlalchemy pymysql
```

3. Open terminal inside the project folder.
4. Generate dataset:

```bash
python python/generate_data.py
```

5. Run analytics:

```bash
python python/analytics.py
```

6. Run machine learning prediction:

```bash
python python/yield_prediction.py
```

7. Create professional Excel workbook:

```bash
python python/create_excel_dashboard.py
```

8. Open MySQL Workbench and run:

```text
sql/01_create_database.sql
sql/02_advanced_analysis_queries.sql
sql/03_powerbi_views.sql
```

9. Load CSV data into MySQL:

```bash
python python/load_data_to_mysql.py
```

10. Open Power BI Desktop and connect to MySQL database:

```text
Database: bindisa_agriculture_bi
```

Use the SQL views for dashboard creation.

## Project Modules

- Yearly agriculture dataset generation
- Data cleaning and validation
- Exploratory data analysis
- Revenue, cost, profit, and production analysis
- Crop-wise performance analysis
- Region-wise performance analysis
- Weather impact analysis
- Year-over-year growth analysis
- SQL data warehouse
- Advanced SQL views and window functions
- Advanced Excel dashboard workbook
- Power BI dashboard design
- Machine learning yield prediction

## Final Dashboard KPIs

- Total Revenue
- Total Profit
- Total Cost
- Profit Margin %
- Total Production
- Average Yield
- Best Performing Crop
- Best Performing Region
- Cost Per Hectare
- Revenue Growth %
- Rainfall Impact on Yield

