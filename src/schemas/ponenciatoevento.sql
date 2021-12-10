SELECT * 
FROM ingsofti_CIMPS3.ponencia
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	1 AS id_tipo_evento, 3 AS id_idioma, 11 AS id_locacion, 500 AS cupo_max, '2020-10-21' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.ponencia
WHERE dia = 21
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	1 AS id_tipo_evento, 3 AS id_idioma, 11 AS id_locacion, 500 AS cupo_max, '2020-10-22' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.ponencia
WHERE dia = 22
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	1 AS id_tipo_evento, 3 AS id_idioma, 11 AS id_locacion, 500 AS cupo_max, '2020-10-23' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.ponencia
WHERE dia = 23
;
