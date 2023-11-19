-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
--	Each record should display: <TV Show genre> - <Number of shows linked to this genre>
--	First column must be called genre
--	Second column must be called number_of_shows
--	Don’t display a genre that doesn’t have any shows linked
--	Results must be sorted in descending order by the number of shows linked
--	You can use only one SELECT statement
--	The database name will be passed as an argument of the mysql command
SELECT 
(SELECT tv_genres.name FROM tv_genres AS tg  JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id) AS genre, COUNT(tv_shows.id) AS number_of_shows 
FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY number_of_shows DESC;
