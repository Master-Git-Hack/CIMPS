#asistencia general
SELECT c.id AS constancia, c.id_evento, c.id_tipo_constancia, t.texto1, t.texto2, t.texto3, t.texto4, '' AS totexto4, uc.nombre AS totexto2, '' AS locacion, uc.email, genero
FROM constancia c
	INNER JOIN tipo_constancia t ON c.id_tipo_constancia = t.id
    INNER JOIN (
		SELECT id, nombre, email, genero, CASE id_tipo_usuario WHEN 2 THEN 1 WHEN 3 THEN 4 WHEN 4 THEN 5 WHEN 6 THEN 9 END AS id_tipo_constancia
        FROM usuario_constancia
        WHERE id_tipo_usuario = 6
			AND id_estado = 1 AND id_emision IN (9, 10)
            AND id NOT IN (
				SELECT user_id
				FROM ingsofti_CIMPS3.users_groups
				WHERE group_id = 2
			)
    )uc ON c.id = uc.id AND c.id_tipo_constancia = uc.id_tipo_constancia
WHERE c.id_estado = 1 AND c.id_emision IN (9, 10) AND c.id_evento = 10
;