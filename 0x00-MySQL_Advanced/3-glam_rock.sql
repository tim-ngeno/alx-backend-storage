-- List all bands with `Glam rock` as their main style ranked by longevity

SELECT band_name,
       IFNULL(split - formed, 2022 - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
AND formed IS NOT NULL
AND (split IS NULL OR split >= formed)
ORDER BY lifespan DESC;
