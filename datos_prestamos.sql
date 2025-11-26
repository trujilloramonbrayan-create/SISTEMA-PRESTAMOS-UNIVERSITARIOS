SELECT * FROM prestamos_prestamo;


SELECT p.id,
       u.username AS estudiante,
       p.monto_solicitado,
       p.plazo_meses,
       p.estado,
       p.fecha_solicitud
FROM prestamos_prestamo p
JOIN auth_user u ON p.estudiante_id = u.id;
