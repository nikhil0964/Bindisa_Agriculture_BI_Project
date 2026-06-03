import os
import random

import numpy as np
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

np.random.seed(42)
random.seed(42)

years = list(range(2018, 2027))

regions = [
    "Madhya Pradesh",
    "Maharashtra",
    "Rajasthan",
    "Gujarat",
    "Uttar Pradesh",
    "Punjab",
    "Haryana",
    "Karnataka",
]

crops = {
    "Wheat": {"base_price": 24000, "base_yield": 3.4, "season": "Rabi"},
    "Rice": {"base_price": 28000, "base_yield": 4.1, "season": "Kharif"},
    "Soybean": {"base_price": 42000, "base_yield": 1.8, "season": "Kharif"},
    "Maize": {"base_price": 22000, "base_yield": 3.2, "season": "Kharif"},
    "Cotton": {"base_price": 62000, "base_yield": 1.5, "season": "Kharif"},
    "Mustard": {"base_price": 51000, "base_yield": 1.4, "season": "Rabi"},
    "Sugarcane": {"base_price": 3300, "base_yield": 72.0, "season": "Annual"},
    "Groundnut": {"base_price": 56000, "base_yield": 1.9, "season": "Kharif"},
}

region_rainfall_profile = {
    "Madhya Pradesh": (650, 1100),
    "Maharashtra": (600, 1200),
    "Rajasthan": (300, 700),
    "Gujarat": (450, 950),
    "Uttar Pradesh": (650, 1050),
    "Punjab": (450, 850),
    "Haryana": (350, 750),
    "Karnataka": (550, 1150),
}

records = []

for year in years:
    inflation_factor = 1 + ((year - 2018) * 0.045)

    for region in regions:
        rainfall_low, rainfall_high = region_rainfall_profile[region]

        for crop, crop_info in crops.items():
            area_hectares = int(np.random.randint(120, 950))
            rainfall_mm = int(np.random.randint(rainfall_low, rainfall_high))
            temperature_c = round(np.random.uniform(20.0, 37.5), 1)

            base_yield = crop_info["base_yield"]
            weather_factor = 1.0

            if rainfall_mm < 550:
                weather_factor -= 0.16
            elif 650 <= rainfall_mm <= 1000:
                weather_factor += 0.09
            elif rainfall_mm > 1150:
                weather_factor -= 0.07

            if temperature_c > 34:
                weather_factor -= 0.10
            elif 24 <= temperature_c <= 31:
                weather_factor += 0.04

            operational_factor = np.random.uniform(0.90, 1.14)
            yield_tonnes_per_hectare = round(base_yield * weather_factor * operational_factor, 2)
            production_tonnes = round(area_hectares * yield_tonnes_per_hectare, 2)

            fertilizer_cost = round(area_hectares * np.random.randint(4800, 8200) * inflation_factor, 2)
            pesticide_cost = round(area_hectares * np.random.randint(1900, 4600) * inflation_factor, 2)
            irrigation_cost = round(area_hectares * np.random.randint(2600, 7200) * inflation_factor, 2)
            labor_cost = round(area_hectares * np.random.randint(6500, 12500) * inflation_factor, 2)
            storage_transport_cost = round(production_tonnes * np.random.randint(650, 1400), 2)

            total_cost = round(
                fertilizer_cost
                + pesticide_cost
                + irrigation_cost
                + labor_cost
                + storage_transport_cost,
                2,
            )

            selling_price_per_tonne = round(
                crop_info["base_price"] * inflation_factor * np.random.uniform(0.91, 1.13),
                2,
            )
            revenue = round(production_tonnes * selling_price_per_tonne, 2)
            profit = round(revenue - total_cost, 2)
            profit_margin = round((profit / revenue) * 100, 2) if revenue else 0
            cost_per_hectare = round(total_cost / area_hectares, 2)

            records.append(
                {
                    "Year": year,
                    "Company": "Bindisa Agriculture Private Limited",
                    "Region": region,
                    "Crop": crop,
                    "Season": crop_info["season"],
                    "Area_Hectares": area_hectares,
                    "Production_Tonnes": production_tonnes,
                    "Yield_Tonnes_Per_Hectare": yield_tonnes_per_hectare,
                    "Rainfall_mm": rainfall_mm,
                    "Temperature_C": temperature_c,
                    "Fertilizer_Cost": fertilizer_cost,
                    "Pesticide_Cost": pesticide_cost,
                    "Irrigation_Cost": irrigation_cost,
                    "Labor_Cost": labor_cost,
                    "Storage_Transport_Cost": storage_transport_cost,
                    "Total_Cost": total_cost,
                    "Cost_Per_Hectare": cost_per_hectare,
                    "Selling_Price_Per_Tonne": selling_price_per_tonne,
                    "Revenue": revenue,
                    "Profit": profit,
                    "Profit_Margin": profit_margin,
                }
            )

df = pd.DataFrame(records)
output_path = os.path.join(DATA_DIR, "bindisa_agriculture_yearly_data.csv")
df.to_csv(output_path, index=False)

print("Dataset created successfully.")
print(f"Rows: {len(df)}")
print(f"Saved at: {output_path}")
print(df.head())

