-- Best genre
SELECT tv_genres.name, SUM(rate) as rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.show_id=tv_show_ratings.show_id
GROUP BY name
ORDER by rating DESC;
