-- Temperatures #2
-- Script that displays the max temperature of each state.
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
