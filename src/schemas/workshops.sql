SELECT u.id, u.gender, name, email, nombre_interno AS taller
FROM users u
	INNER JOIN asistentes_por_fecha af ON u.id = id_user
	INNER JOIN eventos e ON e.id = id_evento
WHERE emision = 2021
	AND id_tipo_evento = 2 AND u.gaffete = 1;