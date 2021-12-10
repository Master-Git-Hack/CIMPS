SELECT *
FROM users u
	LEFT JOIN ingsofti_CIMPS3.order o ON u.id = o.users_id
#WHERE u.active = 1
	#AND o.id_emision = 9
    #AND o.id_estado = 1
    #AND o.accepted = 1
;
SELECT u.id,
	u.tittle, u.name, u.email, u.city, u.afiliation_name, u.afiliation_adress, u.gaffete,
	o.type_payment, o.image, o.bank, o.reference, o.tax_number, o.date, o.folio, o.clave_rastreo, o.accepted
FROM users u
	LEFT JOIN ingsofti_CIMPS3.order o ON u.id = o.users_id
WHERE u.active = 1
	AND o.id_emision = 9
    AND o.id_estado = 1
    AND o.accepted = 1
;
