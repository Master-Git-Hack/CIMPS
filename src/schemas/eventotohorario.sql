SELECT * 
FROM ingsofti_CIMPS3.eventos
;
#articulo dia 1
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 1 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-21'
	AND id_tipo_evento = 3
;
#articulo dia 2
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 1 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-22'
	AND id_tipo_evento = 3
;
#articulo dia 3
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 1 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-23'
	AND id_tipo_evento = 3
;
#taller
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT e.id AS id_evento, fecha, estado, h.id AS id_horario, 1 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos e
	JOIN ingsofti_CIMPS3.horarios_por_emision h
WHERE id_tipo_evento = 2
	AND id_locacion IN (14, 15, 16, 17, 18, 19)
    AND h.id NOT IN (10, 11, 14, 20, 21)
ORDER BY fecha, id_evento, id_horario
;
#ponencia dia 1
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 0 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-21'
	AND id_tipo_evento = 1
;
#ponencia dia 2
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 0 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-22'
	AND id_tipo_evento = 1
;
#ponencia dia 3
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 0 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-23'
	AND id_tipo_evento = 1
;
#magistral dia 1
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 0 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-21'
	AND id_tipo_evento = 6
;
#magistral dia 2
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 0 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-22'
	AND id_tipo_evento = 6
;
#magistral dia 3
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT id AS id_evento, fecha, estado, 10 AS id_horario, 0 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos
WHERE fecha = '2020-10-23'
	AND id_tipo_evento = 6
;
#taller individual
INSERT INTO horarios_por_evento(
	id_evento, fecha, estado, id_horario, eventos_en_paralelo
)
SELECT e.id AS id_evento, fecha, estado, h.id AS id_horario, 1 AS eventos_en_paralelo
FROM ingsofti_CIMPS3.eventos e
	JOIN ingsofti_CIMPS3.horarios_por_emision h
WHERE id_tipo_evento = 2
	AND e.id = 291
    AND h.id NOT IN (10, 11, 14, 20, 21)
ORDER BY fecha, id_evento, id_horario
;
