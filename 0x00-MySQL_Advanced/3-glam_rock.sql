-- SQL script that lists all bands with Glam roch as their main style
SELECT band_name,
       (YEAR('2022-01-01') - formed) AS lifespan
FROM metal_bands
WHERE split LIKE '%Glam rock%'
ORDER BY lifespan DESC;
