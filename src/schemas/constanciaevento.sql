SELECT c.id AS constancia, c.id_evento, c.id_tipo_constancia, t.texto1, t.texto2, t.texto3, t.texto4, e.nombre_interno AS totexto4, e.contacto AS totexto2, e.id_locacion, uc.email
#SELECT *
FROM constancia c
	INNER JOIN tipo_constancia t ON c.id_tipo_constancia = t.id
    INNER JOIN eventos e ON e.id = c.id_evento AND t.id_tipo_evento = e.id_tipo_evento
    INNER JOIN (
		SELECT id, email, genero, CASE id_tipo_usuario WHEN 2 THEN 1 WHEN 3 THEN 4 WHEN 4 THEN 5 END AS id_tipo_constancia
        FROM usuario_constancia
        WHERE id_tipo_usuario != 6
			AND id_estado = 1 AND id_emision = 9
    )uc ON c.id = uc.id AND c.id_tipo_constancia = uc.id_tipo_constancia
WHERE c.id_tipo_constancia IN (1, 2, 4, 5)
	AND c.id_estado = 1 AND c.id_emision = 9
	AND c.id < 10000000
UNION ALL
SELECT c.id AS constancia, c.id_evento, c.id_tipo_constancia, t.texto1, t.texto2, t.texto3, t.texto4, e.nombre_interno AS totexto4, e.contacto AS totexto2, e.id_locacion, '' AS email
#SELECT *
FROM constancia c
	INNER JOIN tipo_constancia t ON c.id_tipo_constancia = t.id
    INNER JOIN eventos e ON e.id = c.id_evento
WHERE c.id_tipo_constancia IN (1, 2, 4, 5)
	AND c.id_estado = 1 AND c.id_emision = 9
    AND t.id_estado = 1 AND t.id_emision = 9
	AND c.id > 9999999
ORDER BY id_evento
;
