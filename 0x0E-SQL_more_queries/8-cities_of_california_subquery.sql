-- Script that lists all the cities of California registered in the database
-- The states table contains only one record where name = California (but the id can be different, as per the example)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword

SELECT id, name -- Query to list all the cities from California
FROM cities
WHERE state_id = ( -- Query to get the id of California
      SELECT id
      FROM states
      WHERE name = "California");
