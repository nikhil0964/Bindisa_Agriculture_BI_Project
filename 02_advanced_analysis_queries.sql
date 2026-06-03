USE bindisa_agriculture_bi;

-- 1. Basic data audit
SELECT COUNT(*) AS total_records FROM yearly_agriculture_data;

SELECT
    MIN(year) AS first_year,
    MAX(year) AS latest_year,
    COUNT(DISTINCT region) AS total_regions,
    COUNT(DISTINCT crop) AS total_crops
FROM yearly_agriculture_data;

-- 2. Executive KPI summary
SELECT
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(total_cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(revenue) * 100, 2) AS profit_margin_percent,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield
FROM yearly_agriculture_data;

-- 3. Yearly financial performance
SELECT
    year,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(total_cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(revenue) * 100, 2) AS profit_margin_percent
FROM yearly_agriculture_data
GROUP BY year
ORDER BY year;

-- 4. Crop-wise profitability
SELECT
    crop,
    ROUND(SUM(area_hectares), 2) AS total_area,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM yearly_agriculture_data
GROUP BY crop
ORDER BY total_profit DESC;

-- 5. Region-wise business intelligence
SELECT
    region,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(profit_margin), 2) AS average_profit_margin
FROM yearly_agriculture_data
GROUP BY region
ORDER BY total_revenue DESC;

-- 6. Best crop by year using window function
WITH crop_year_profit AS (
    SELECT
        year,
        crop,
        SUM(profit) AS total_profit
    FROM yearly_agriculture_data
    GROUP BY year, crop
),
ranked_crops AS (
    SELECT
        year,
        crop,
        total_profit,
        RANK() OVER (PARTITION BY year ORDER BY total_profit DESC) AS profit_rank
    FROM crop_year_profit
)
SELECT
    year,
    crop,
    ROUND(total_profit, 2) AS total_profit
FROM ranked_crops
WHERE profit_rank = 1
ORDER BY year;

-- 7. Year-over-year revenue growth
WITH yearly_revenue AS (
    SELECT
        year,
        SUM(revenue) AS total_revenue
    FROM yearly_agriculture_data
    GROUP BY year
)
SELECT
    year,
    ROUND(total_revenue, 2) AS total_revenue,
    ROUND(LAG(total_revenue) OVER (ORDER BY year), 2) AS previous_year_revenue,
    ROUND(
        (total_revenue - LAG(total_revenue) OVER (ORDER BY year))
        / LAG(total_revenue) OVER (ORDER BY year) * 100,
        2
    ) AS revenue_growth_percent
FROM yearly_revenue
ORDER BY year;

-- 8. Cost distribution
SELECT 'Fertilizer Cost' AS cost_category, ROUND(SUM(fertilizer_cost), 2) AS amount FROM yearly_agriculture_data
UNION ALL
SELECT 'Pesticide Cost', ROUND(SUM(pesticide_cost), 2) FROM yearly_agriculture_data
UNION ALL
SELECT 'Irrigation Cost', ROUND(SUM(irrigation_cost), 2) FROM yearly_agriculture_data
UNION ALL
SELECT 'Labor Cost', ROUND(SUM(labor_cost), 2) FROM yearly_agriculture_data
UNION ALL
SELECT 'Storage and Transport Cost', ROUND(SUM(storage_transport_cost), 2) FROM yearly_agriculture_data;

-- 9. Weather impact by rainfall category
SELECT
    CASE
        WHEN rainfall_mm < 600 THEN 'Low Rainfall'
        WHEN rainfall_mm BETWEEN 600 AND 1000 THEN 'Normal Rainfall'
        ELSE 'High Rainfall'
    END AS rainfall_category,
    ROUND(AVG(yield_tonnes_per_hectare), 2) AS average_yield,
    ROUND(SUM(production_tonnes), 2) AS total_production,
    ROUND(SUM(profit), 2) AS total_profit
FROM yearly_agriculture_data
GROUP BY rainfall_category
ORDER BY average_yield DESC;

-- 10. Top 10 most profitable crop-region combinations
SELECT
    region,
    crop,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(revenue) * 100, 2) AS profit_margin_percent
FROM yearly_agriculture_data
GROUP BY region, crop
ORDER BY total_profit DESC
LIMIT 10;

