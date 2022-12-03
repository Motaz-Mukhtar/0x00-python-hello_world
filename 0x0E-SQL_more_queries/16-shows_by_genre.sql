-- liss all shows, and all genres linked to that show form the database hbtn_0d_tvshows.
-- if a show doesn't have a genre, dispaly NULL in the genre column
SELECT s.`title`, g.`name`
FROM `tv_shows` AS s

	LEFT JOIN `tv_show_genres` ON
		s.`id` = `tv_show_genres`.`show_id`

	LEFT JOIN `tv_genres` AS g ON
		`tv_show_genres`.`genre_id` = g.`id`

ORDER BY s.`title`, g.`name`;
