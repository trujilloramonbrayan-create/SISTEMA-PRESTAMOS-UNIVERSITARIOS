SELECT * FROM notificaciones_notificacion;

SELECT 
    n.id,
    u.username AS usuario,
    n.titulo,
    n.mensaje,
    n.tipo,
    n.leida,
    n.fecha_creacion
FROM notificaciones_notificacion n
JOIN auth_user u ON n.usuario_id = u.id
ORDER BY n.fecha_creacion DESC;

