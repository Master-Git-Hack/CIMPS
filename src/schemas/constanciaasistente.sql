#asistencia general
SELECT c.id AS constancia, c.id_evento, c.id_tipo_constancia, t.texto1, t.texto2, t.texto3, t.texto4, '' AS totexto4, uc.nombre AS totexto2, '' AS locacion, uc.email, genero
FROM constancia c
	INNER JOIN tipo_constancia t ON c.id_tipo_constancia = t.id
    INNER JOIN (
		SELECT id, nombre, email, genero, CASE id_tipo_usuario WHEN 2 THEN 1 WHEN 3 THEN 4 WHEN 4 THEN 5 WHEN 6 THEN 9 END AS id_tipo_constancia
        FROM usuario_constancia
        WHERE id_tipo_usuario = 6
			AND id_estado = 1 AND id_emision = 9
            AND id NOT IN (
				SELECT user_id
				FROM ingsofti_CIMPS3.users_groups
				WHERE group_id = 2
			)
    )uc ON c.id = uc.id AND c.id_tipo_constancia = uc.id_tipo_constancia
WHERE c.id_estado = 1 AND c.id_emision = 9 AND c.id_evento = 10
;
SELECT *
FROM users
;
		SELECT *
        FROM usuario_constancia
        WHERE id_tipo_usuario = 6
;

# consulta para saber quienes son los asistentes por taller que pagaron, de aqui deberia generarse un insert en constancia
SELECT c.id AS constancia, ae.id_taller AS id_evento, c.id_tipo_constancia,
	t.texto1, t.texto2, 'For <hisher> attendance at the workshop entitled as:' AS texto3, '<intitulado>' AS texto4, ae.nombretaller AS totexto4, uc.nombre AS totexto2,
    '' AS locacion, uc.email, uc.genero, 
    o.accepted, ae.id_taller
FROM constancia c
	INNER JOIN tipo_constancia t ON c.id_tipo_constancia = t.id
    INNER JOIN (
		SELECT id, nombre, email, genero, CASE id_tipo_usuario WHEN 2 THEN 1 WHEN 3 THEN 4 WHEN 4 THEN 5 WHEN 6 THEN 9 END AS id_tipo_constancia
        FROM usuario_constancia
        WHERE id_tipo_usuario = 6
			AND id_estado = 1 AND id_emision = 9
            AND id NOT IN (
				SELECT user_id
				FROM ingsofti_CIMPS3.users_groups
				WHERE group_id = 2
			)
    )uc ON c.id = uc.id AND c.id_tipo_constancia = uc.id_tipo_constancia
    LEFT JOIN (
			SELECT u.id, name, email, e.id AS id_taller, nombre_interno AS nombretaller
		FROM users u
			INNER JOIN asistentes_por_fecha af ON u.id = id_user
			INNER JOIN eventos e ON e.id = id_evento
		WHERE emision = 2020
			AND id_tipo_evento = 2
	)ae ON ae.id = c.id
    LEFT JOIN ingsofti_CIMPS3.order o ON o.users_id = c.id
WHERE c.id_estado = 1 AND c.id_emision = 9
	AND ae.id_taller IS NOT NULL
ORDER BY constancia, id_evento
;

#despues del insert consultamos los asistentes al taller
SELECT c.id AS constancia, c.id_evento, c.id_tipo_constancia,
	t.texto1, t.texto2, 'For <hisher> attendance at the workshop entitled as:' AS texto3, '<intitulado>' AS texto4, ae.nombretaller AS totexto4, uc.nombre AS totexto2,
    '' AS locacion, uc.email, uc.genero
FROM constancia c
	INNER JOIN tipo_constancia t ON c.id_tipo_constancia = t.id
    INNER JOIN (
		SELECT id, nombre, email, genero, CASE id_tipo_usuario WHEN 2 THEN 1 WHEN 3 THEN 4 WHEN 4 THEN 5 WHEN 6 THEN 9 END AS id_tipo_constancia
        FROM usuario_constancia
        WHERE id_tipo_usuario = 6
			AND id_estado = 1 AND id_emision = 9
            AND id NOT IN (
				SELECT user_id
				FROM ingsofti_CIMPS3.users_groups
				WHERE group_id = 2
			)
    )uc ON c.id = uc.id AND c.id_tipo_constancia = uc.id_tipo_constancia
    INNER JOIN (
			SELECT u.id, name, email, e.id AS id_taller, nombre_interno AS nombretaller
		FROM users u
			INNER JOIN asistentes_por_fecha af ON u.id = id_user
			INNER JOIN eventos e ON e.id = id_evento
		WHERE emision = 2020
			AND id_tipo_evento = 2
	)ae ON ae.id = c.id AND ae.id_taller = id_evento
WHERE c.id_estado = 1 AND c.id_emision = 9
ORDER BY constancia, id_evento
;
