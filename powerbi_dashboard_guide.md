# Power BI Dashboard Guide

## Data Source

Connect Power BI Desktop to MySQL.

```text
Server: localhost
Database: bindisa_agriculture_bi
```

Import these tables and views:

```text
yearly_agriculture_data
vw_executive_kpis
vw_yearly_summary
vw_crop_summary
vw_region_summary
vw_weather_impact
```

## Dashboard Pages

### Page 1: Executive Overview

Use cards for:

- Total Revenue
- Total Profit
- Total Cost
- Profit Margin %
- Total Production
- Average Yield

Use visuals:

- Line chart: Total Revenue by Year
- Bar chart: Total Profit by Crop
- Bar chart: Total Revenue by Region
- Donut chart: Cost Distribution

### Page 2: Yearly Performance

Use:

- Line chart: Revenue by Year
- Line chart: Profit by Year
- Column chart: Production by Year
- Matrix: Year, Total Revenue, Total Cost, Total Profit, Profit Margin %

### Page 3: Crop Analysis

Use:

- Bar chart: Total Profit by Crop
- Bar chart: Average Yield by Crop
- Table: Crop, Total Area, Total Production, Total Revenue, Total Profit
- Slicer: Crop

### Page 4: Region Analysis

Use:

- Map or filled map: Revenue by Region
- Bar chart: Profit by Region
- Table: Region, Production, Revenue, Profit, Profit Margin
- Slicer: Region

### Page 5: Weather Impact

Use:

- Scatter chart: Rainfall vs Yield
- Scatter chart: Temperature vs Yield
- Bar chart: Average Yield by Rainfall Category
- Table: Rainfall Category, Average Yield, Total Production, Total Profit

## Recommended DAX Measures

```DAX
Total Revenue = SUM(yearly_agriculture_data[revenue])
```

```DAX
Total Profit = SUM(yearly_agriculture_data[profit])
```

```DAX
Total Cost = SUM(yearly_agriculture_data[total_cost])
```

```DAX
Total Production = SUM(yearly_agriculture_data[production_tonnes])
```

```DAX
Average Yield = AVERAGE(yearly_agriculture_data[yield_tonnes_per_hectare])
```

```DAX
Profit Margin % = DIVIDE([Total Profit], [Total Revenue]) * 100
```

```DAX
Cost Per Hectare = DIVIDE([Total Cost], SUM(yearly_agriculture_data[area_hectares]))
```

## Professional Design Tips

- Use a clean agriculture-inspired color theme: green, white, charcoal, and gold.
- Keep KPI cards at the top.
- Use slicers for Year, Region, Crop, and Season.
- Use consistent number formatting.
- Use short, clear chart titles.
- Add the company name to the report header.

