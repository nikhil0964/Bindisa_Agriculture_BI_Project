# Advanced Excel Dashboard Guide

## Workbook

The Python script creates:

```text
excel/Bindisa_Agriculture_Advanced_Dashboard.xlsx
```

## Sheets

- Dashboard
- Raw_Data
- Yearly_Summary
- Crop_Summary
- Region_Summary
- Cost_Summary

## Recommended Manual Enhancements

After opening the workbook in Excel:

1. Convert Raw_Data into an Excel Table.
2. Insert Pivot Tables from Raw_Data.
3. Add slicers for Year, Region, Crop, and Season.
4. Add conditional formatting to Profit Margin.
5. Add a green-white professional theme.

## Useful Excel Formulas

```excel
=SUM(Raw_Data[Revenue])
```

```excel
=SUM(Raw_Data[Profit])
```

```excel
=SUM(Raw_Data[Profit])/SUM(Raw_Data[Revenue])
```

```excel
=AVERAGE(Raw_Data[Yield_Tonnes_Per_Hectare])
```

```excel
=XLOOKUP(MAX(Crop_Summary[Total_Profit]),Crop_Summary[Total_Profit],Crop_Summary[Crop])
```

```excel
=RANK.EQ([@Total_Profit],Crop_Summary[Total_Profit],0)
```

## Pivot Table Ideas

- Revenue by Year
- Profit by Crop
- Production by Region
- Cost by Category
- Yield by Season
- Profit Margin by Crop

