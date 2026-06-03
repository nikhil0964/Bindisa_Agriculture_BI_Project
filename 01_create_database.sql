DROP DATABASE IF EXISTS bindisa_agriculture_bi;
CREATE DATABASE bindisa_agriculture_bi;
USE bindisa_agriculture_bi;

CREATE TABLE yearly_agriculture_data (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    company VARCHAR(150) NOT NULL,
    region VARCHAR(100) NOT NULL,
    crop VARCHAR(80) NOT NULL,
    season VARCHAR(40) NOT NULL,
    area_hectares DECIMAL(12,2) NOT NULL,
    production_tonnes DECIMAL(14,2) NOT NULL,
    yield_tonnes_per_hectare DECIMAL(10,2) NOT NULL,
    rainfall_mm DECIMAL(10,2) NOT NULL,
    temperature_c DECIMAL(6,2) NOT NULL,
    fertilizer_cost DECIMAL(16,2) NOT NULL,
    pesticide_cost DECIMAL(16,2) NOT NULL,
    irrigation_cost DECIMAL(16,2) NOT NULL,
    labor_cost DECIMAL(16,2) NOT NULL,
    storage_transport_cost DECIMAL(16,2) NOT NULL,
    total_cost DECIMAL(16,2) NOT NULL,
    cost_per_hectare DECIMAL(14,2) NOT NULL,
    selling_price_per_tonne DECIMAL(14,2) NOT NULL,
    revenue DECIMAL(18,2) NOT NULL,
    profit DECIMAL(18,2) NOT NULL,
    profit_margin DECIMAL(8,2) NOT NULL
);

CREATE INDEX idx_year ON yearly_agriculture_data(year);
CREATE INDEX idx_region ON yearly_agriculture_data(region);
CREATE INDEX idx_crop ON yearly_agriculture_data(crop);
CREATE INDEX idx_season ON yearly_agriculture_data(season);

