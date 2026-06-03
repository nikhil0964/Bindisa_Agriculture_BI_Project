import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)

data_path = os.path.join(DATA_DIR, "bindisa_agriculture_yearly_data.csv")
df = pd.read_csv(data_path)

print("\nBINDISA AGRICULTURE PRIVATE LIMITED")
print("Yearly Agricultural Data Analytics")
print("-" * 60)
print("\nFirst 5 records:")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

yearly_summary = (
    df.groupby("Year")
    .agg(
        Total_Area=("Area_Hectares", "sum"),
        Total_Production=("Production_Tonnes", "sum"),
        Average_Yield=("Yield_Tonnes_Per_Hectare", "mean"),
        Total_Revenue=("Revenue", "sum"),
        Total_Cost=("Total_Cost", "sum"),
        Total_Profit=("Profit", "sum"),
    )
    .reset_index()
)
yearly_summary["Profit_Margin_Percent"] = (
    yearly_summary["Total_Profit"] / yearly_summary["Total_Revenue"] * 100
).round(2)

crop_summary = (
    df.groupby("Crop")
    .agg(
        Total_Area=("Area_Hectares", "sum"),
        Total_Production=("Production_Tonnes", "sum"),
        Average_Yield=("Yield_Tonnes_Per_Hectare", "mean"),
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
    )
    .reset_index()
    .sort_values("Total_Profit", ascending=False)
)

region_summary = (
    df.groupby("Region")
    .agg(
        Total_Production=("Production_Tonnes", "sum"),
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit_Margin=("Profit_Margin", "mean"),
    )
    .reset_index()
    .sort_values("Total_Revenue", ascending=False)
)

cost_summary = df[
    [
        "Fertilizer_Cost",
        "Pesticide_Cost",
        "Irrigation_Cost",
        "Labor_Cost",
        "Storage_Transport_Cost",
    ]
].sum().reset_index()
cost_summary.columns = ["Cost_Category", "Amount"]

yearly_summary.to_csv(os.path.join(DATA_DIR, "yearly_summary.csv"), index=False)
crop_summary.to_csv(os.path.join(DATA_DIR, "crop_summary.csv"), index=False)
region_summary.to_csv(os.path.join(DATA_DIR, "region_summary.csv"), index=False)
cost_summary.to_csv(os.path.join(DATA_DIR, "cost_summary.csv"), index=False)

sns.set_theme(style="whitegrid", palette="Set2")

plt.figure(figsize=(11, 6))
sns.lineplot(data=yearly_summary, x="Year", y="Total_Revenue", marker="o", linewidth=2.5)
plt.title("Yearly Revenue Trend - Bindisa Agriculture Private Limited")
plt.xlabel("Year")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig(os.path.join(REPORTS_DIR, "yearly_revenue_trend.png"), dpi=160)
plt.close()

plt.figure(figsize=(11, 6))
sns.barplot(data=crop_summary, x="Crop", y="Total_Profit")
plt.title("Crop-wise Profit Performance")
plt.xlabel("Crop")
plt.ylabel("Total Profit")
plt.xticks(rotation=35)
plt.tight_layout()
plt.savefig(os.path.join(REPORTS_DIR, "crop_profit_performance.png"), dpi=160)
plt.close()

plt.figure(figsize=(11, 6))
sns.barplot(data=region_summary, x="Region", y="Total_Revenue")
plt.title("Region-wise Revenue Performance")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=35)
plt.tight_layout()
plt.savefig(os.path.join(REPORTS_DIR, "region_revenue_performance.png"), dpi=160)
plt.close()

plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x="Rainfall_mm",
    y="Yield_Tonnes_Per_Hectare",
    hue="Season",
    size="Area_Hectares",
    alpha=0.75,
)
plt.title("Rainfall Impact on Crop Yield")
plt.xlabel("Rainfall mm")
plt.ylabel("Yield Tonnes Per Hectare")
plt.tight_layout()
plt.savefig(os.path.join(REPORTS_DIR, "rainfall_yield_impact.png"), dpi=160)
plt.close()

print("\nYearly Summary:")
print(yearly_summary)
print("\nTop Crops by Profit:")
print(crop_summary.head())
print("\nTop Regions by Revenue:")
print(region_summary.head())
print("\nAnalytics completed successfully.")

