SELECT *
FROM ingsofti_CIMPS3.taller
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 14 AS id_locacion, 40 AS cupo_max, '2020-10-21' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 1'
	AND dia = 21
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 14 AS id_locacion, 40 AS cupo_max, '2020-10-22' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 1'
	AND dia = 22
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 14 AS id_locacion, 40 AS cupo_max, '2020-10-23' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 1'
	AND dia = 23
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 15 AS id_locacion, 40 AS cupo_max, '2020-10-21' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 2'
	AND dia = 21
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 15 AS id_locacion, 40 AS cupo_max, '2020-10-22' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 2'
	AND dia = 22
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 15 AS id_locacion, 40 AS cupo_max, '2020-10-23' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 2'
	AND dia = 23
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 16 AS id_locacion, 40 AS cupo_max, '2020-10-21' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 3'
	AND dia = 21
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 16 AS id_locacion, 40 AS cupo_max, '2020-10-22' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 3'
	AND dia = 22
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 16 AS id_locacion, 40 AS cupo_max, '2020-10-23' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 3'
	AND dia = 23
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 17 AS id_locacion, 40 AS cupo_max, '2020-10-21' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 4'
	AND dia = 21
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 17 AS id_locacion, 40 AS cupo_max, '2020-10-22' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 4'
	AND dia = 22
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 17 AS id_locacion, 40 AS cupo_max, '2020-10-23' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 4'
	AND dia = 23
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 18 AS id_locacion, 40 AS cupo_max, '2020-10-21' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 5'
	AND dia = 21
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 18 AS id_locacion, 40 AS cupo_max, '2020-10-22' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 5'
	AND dia = 22
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 18 AS id_locacion, 40 AS cupo_max, '2020-10-23' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 5'
	AND dia = 23
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 19 AS id_locacion, 40 AS cupo_max, '2020-10-21' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 6'
	AND dia = 21
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 19 AS id_locacion, 40 AS cupo_max, '2020-10-22' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 6'
	AND dia = 22
;
INSERT INTO eventos(
	nombre_externo, nombre_interno, descripcion, emision, contacto, id_titular, requisitos,
	id_tipo_evento, id_idioma, id_locacion, cupo_max, fecha, estado, moderador
)
SELECT nombre AS nombre_externo, nombre AS nombre_interno, '' AS descripcion, emision, contacto, 1 AS id_titular, '' AS requisitos,
	2 AS id_tipo_evento, 3 AS id_idioma, 19 AS id_locacion, 40 AS cupo_max, '2020-10-23' AS fecha, 1 AS estado, 'Por definir' AS moderador	
FROM ingsofti_CIMPS3.taller
WHERE locacion = 'Taller 6'
	AND dia = 23
;
