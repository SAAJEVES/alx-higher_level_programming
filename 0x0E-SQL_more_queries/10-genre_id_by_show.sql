-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
--	Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
--		Each record should display: tv_shows.title - tv_show_genres.genre_id
--		Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--		You can use only one SELECT statement
--		The database name will be passed as an argument of the mysql command

/* DROP TABLE IF EXISTS `tv_genres`;
CREATE TABLE `tv_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `tv_show_genres`;
CREATE TABLE `tv_show_genres` (
  `show_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  KEY `show_id` (`show_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `tv_show_genres_ibfk_1` FOREIGN KEY (`show_id`) REFERENCES `tv_shows` (`id`),
  CONSTRAINT `tv_show_genres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `tv_genres` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `tv_shows`;
CREATE TABLE `tv_shows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;*/

USE hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show_genres
JOIN tv_shows 
ON tv_show_genres.show_id = tv_shows.id 
ORDER BY tv_shows.title, tv_show_genres.genre_id;

