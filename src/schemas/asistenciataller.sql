SELECT *
FROM users
;
SELECT *
FROM eventos
;
SELECT *, COUNT(e.id) AS asistencia
FROM users u
	INNER JOIN asistentes_por_fecha af ON u.id = id_user
	INNER JOIN eventos e ON e.id = id_evento
WHERE id_tipo_evento = 2
GROUP BY e.id
;
SELECT name, email, city, afiliation_name, afiliation_adress, gaffete, nombre_interno AS taller
FROM users u
	INNER JOIN asistentes_por_fecha af ON u.id = id_user
	INNER JOIN eventos e ON e.id = id_evento
WHERE emision = 2020
	AND id_tipo_evento = 2
;
SELECT u.id, name, email, e.id AS idtaller, nombre_interno AS taller
FROM users u
	INNER JOIN asistentes_por_fecha af ON u.id = id_user
	INNER JOIN eventos e ON e.id = id_evento
WHERE emision = 2020
	AND id_tipo_evento = 2
;
