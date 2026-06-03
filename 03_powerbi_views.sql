USE bindisa_agriculture_bi;

CREATE OR REPLACE VIEW vw_executive_kpis AS
SELECT
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(total_cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(revenue) * 100, 2) AS profit_margin_percent,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield,
    ROUND(SUM(total_cost) / SUM(area_hectares), 2) AS cost_per_hectare
FROM yearly_agriculture_data;

CREATE OR REPLACE VIEW vw_yearly_summary AS
SELECT
    year,
    ROUND(SUM(area_hectares), 2) AS total_area,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(total_cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(revenue) * 100, 2) AS profit_margin_percent
FROM yearly_agriculture_data
GROUP BY year;

CREATE OR REPLACE VIEW vw_crop_summary AS
SELECT
    crop,
    ROUND(SUM(area_hectares), 2) AS total_area,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(total_cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(revenue) * 100, 2) AS profit_margin_percent
FROM yearly_agriculture_data
GROUP BY crop;

CREATE OR REPLACE VIEW vw_region_summary AS
SELECT
    region,
    ROUND(SUM(area_hectares), 2) AS total_area,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(total_cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(revenue) * 100, 2) AS profit_margin_percent
FROM yearly_agriculture_data
GROUP BY region;

CREATE OR REPLACE VIEW vw_weather_impact AS
SELECT
    CASE
        WHEN rainfall_mm < 600 THEN 'Low Rainfall'
        WHEN rainfall_mm BETWEEN 600 AND 1000 THEN 'Normal Rainfall'
        ELSE 'High Rainfall'
    END AS rainfall_category,
    ROUND(AVG(rainfall_mm), 2) AS average_rainfall,
    ROUND(AVG(temperature_c), 2) AS average_temperature,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(SUM(profit), 2) AS total_profit
FROM yearly_agriculture_data
GROUP BY rainfall_category;

