import os

import pandas as pd
from sqlalchemy import create_engine


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

DB_USER = "root"
DB_PASSWORD = "your_mysql_password"
DB_HOST = "localhost"
DB_NAME = "bindisa_agriculture_bi"

csv_path = os.path.join(DATA_DIR, "bindisa_agriculture_yearly_data.csv")
df = pd.read_csv(csv_path)

df.columns = [
    "year",
    "company",
    "region",
    "crop",
    "season",
    "area_hectares",
    "production_tonnes",
    "yield_tonnes_per_hectare",
    "rainfall_mm",
    "temperature_c",
    "fertilizer_cost",
    "pesticide_cost",
    "irrigation_cost",
    "labor_cost",
    "storage_transport_cost",
    "total_cost",
    "cost_per_hectare",
    "selling_price_per_tonne",
    "revenue",
    "profit",
    "profit_margin",
]

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

df.to_sql(
    name="yearly_agriculture_data",
    con=engine,
    if_exists="append",
    index=False,
)

print("Data loaded into MySQL successfully.")

