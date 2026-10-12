
-- View 1: Temperatura média por localização (In/Out)
CREATE OR REPLACE VIEW avg_temperature_location AS
SELECT
    location_type,
    AVG(temp) AS avg_temperature
FROM temperature_readings
GROUP BY location_type;


-- View 2: Quantidade de registros por hora do dia
CREATE OR REPLACE VIEW readings_per_hour AS
SELECT
    EXTRACT(HOUR FROM noted_date) AS hour,
    COUNT(*) AS total_readings
FROM temperature_readings
GROUP BY EXTRACT(HOUR FROM noted_date)
ORDER BY hour;


-- View 3: Temperaturas mínima e máxima por dia
CREATE OR REPLACE VIEW daily_temperature_extremes AS
SELECT
    DATE(noted_date) AS reading_date,
    MIN(temp) AS min_temperature,
    MAX(temp) AS max_temperature
FROM temperature_readings
GROUP BY DATE(noted_date)
ORDER BY reading_date;