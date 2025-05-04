-- Write SQL script that ranks country origins of bands
-- Ordered by the number
-- Column must be orign

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
