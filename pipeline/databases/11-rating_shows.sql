-- Rotten tomatoes
-- lists all shows by their rating. 
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
GROUP BY title
ORDER BY rating DESC;
