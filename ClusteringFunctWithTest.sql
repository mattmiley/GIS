
--CREATE FUNCTION WITH THIS
CREATE OR REPLACE FUNCTION getclusters(minlat numeric,maxlat numeric,minlon numeric,maxlon numeric) 
RETURNS TABLE 
(point_count INT,
geom geometry)     
AS 
$func$ 
SELECT 
ST_NumGeometries(gc),
ST_Centroid(gc) AS centroid
FROM (
SELECT unnest(ST_ClusterWithin(QP.geom, 0.25 )) gc
FROM (SELECT geom FROM points 
WHERE ST_Intersects(ST_PolygonFromText(concat('POLYGON(( ' , minlon , ' ' , minlat , ',' , maxlon , ' ' , minlat , ',' , maxlon , ' ' , maxlat , ',' , minlon , ' ' , maxlat , ',' , minlon , ' ' , minlat , '))'),4326), geom )) QP
) f
$func$ 
LANGUAGE sql;


--TEST WITH THESE
SELECT * FROM getclusters(39.5,41.5,-76.5, -73);
SELECT * FROM getclusters(36.5,44,-80, -70);
SELECT * FROM getclusters(30,50,-80, -50);