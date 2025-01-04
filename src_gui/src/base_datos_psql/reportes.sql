CREATE OR REPLACE VIEW reporte_reservacion_basico AS
SELECT
    c.nombres || ' ' || c.apellido_paterno AS nombre_cliente,
    h.numero_habitacion,
    h.tipo_habitacion,
    r.check_in,
    r.check_out,
    r.total AS monto_total,
    p.fecha_pago,
    p.monto_pagado
FROM
    cliente c
JOIN
    reservacion r ON c.id_cliente = r.id_cliente
JOIN
    habitacion h ON r.numero_habitacion = h.numero_habitacion
LEFT JOIN
    pago p ON r.id_reservacion = p.id_reservacion;
