import os

import pandas as pd
import streamlit as st


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "bindisa_agriculture_yearly_data.csv")

st.set_page_config(
    page_title="Bindisa Agriculture BI System",
    page_icon="🌾",
    layout="wide",
)

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

st.title("Bindisa Agriculture Private Limited")
st.subheader("Yearly Agricultural Data Analytics and Business Intelligence System")

with st.sidebar:
    st.header("Filters")
    years = sorted(df["Year"].unique())
    crops = sorted(df["Crop"].unique())
    regions = sorted(df["Region"].unique())
    seasons = sorted(df["Season"].unique())

    selected_years = st.multiselect("Year", years, default=years)
    selected_crops = st.multiselect("Crop", crops, default=crops)
    selected_regions = st.multiselect("Region", regions, default=regions)
    selected_seasons = st.multiselect("Season", seasons, default=seasons)

filtered = df[
    df["Year"].isin(selected_years)
    & df["Crop"].isin(selected_crops)
    & df["Region"].isin(selected_regions)
    & df["Season"].isin(selected_seasons)
]

total_revenue = filtered["Revenue"].sum()
total_profit = filtered["Profit"].sum()
total_cost = filtered["Total_Cost"].sum()
total_production = filtered["Production_Tonnes"].sum()
average_yield = filtered["Yield_Tonnes_Per_Hectare"].mean()
profit_margin = (total_profit / total_revenue * 100) if total_revenue else 0

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Total Cost", f"₹{total_cost:,.0f}")
col4.metric("Total Production", f"{total_production:,.0f} tonnes")
col5.metric("Average Yield", f"{average_yield:.2f} t/ha")
col6.metric("Profit Margin", f"{profit_margin:.2f}%")

st.divider()

yearly_summary = (
    filtered.groupby("Year", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
        Production=("Production_Tonnes", "sum"),
    )
    .sort_values("Year")
)

crop_summary = (
    filtered.groupby("Crop", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
        Average_Yield=("Yield_Tonnes_Per_Hectare", "mean"),
    )
    .sort_values("Profit", ascending=False)
)

region_summary = (
    filtered.groupby("Region", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
        Production=("Production_Tonnes", "sum"),
    )
    .sort_values("Revenue", ascending=False)
)

left, right = st.columns(2)

with left:
    st.subheader("Yearly Revenue Trend")
    st.line_chart(yearly_summary, x="Year", y="Revenue")

with right:
    st.subheader("Yearly Profit Trend")
    st.line_chart(yearly_summary, x="Year", y="Profit")

left, right = st.columns(2)

with left:
    st.subheader("Crop-wise Profit")
    st.bar_chart(crop_summary, x="Crop", y="Profit")

with right:
    st.subheader("Region-wise Revenue")
    st.bar_chart(region_summary, x="Region", y="Revenue")

st.subheader("Weather Impact Data")
weather_view = filtered[
    [
        "Year",
        "Region",
        "Crop",
        "Season",
        "Rainfall_mm",
        "Temperature_C",
        "Yield_Tonnes_Per_Hectare",
        "Revenue",
        "Profit",
    ]
]
st.dataframe(weather_view, use_container_width=True)

st.subheader("Complete Filtered Dataset")
st.dataframe(filtered, use_container_width=True)

