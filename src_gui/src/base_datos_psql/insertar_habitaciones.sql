--Script para instalar las habitaciones en la base de datos.

INSERT INTO habitacion (numero_habitacion, tipo_habitacion, precio_noche, estado)
VALUES 
(101, 'Sencilla', 450, 'Disponible'),
(102, 'Sencilla', 400, 'Disponible'),
(103, 'Sencilla', 350, 'Disponible'),
(104, 'Sencilla', 350, 'Disponible'),
(105, 'Doble', 850, 'Disponible'),
(106, 'Doble', 830, 'Disponible'),
(201, 'Suite', 1600, 'Disponible'),
(202, 'Suite', 1200, 'Disponible'),
(203, 'Suite', 1400, 'Disponible'),
(204, 'Familiar', 1700, 'Disponible'),
(205, 'Familiar', 1800, 'Disponible'),
(206, 'Familiar', 1900, 'Disponible'),
(301, 'Deluxe', 2600, 'Disponible'),
(302, 'Deluxe', 2500, 'Disponible'),
(303, 'Deluxe', 2500, 'Disponible'),
(304, 'Suite presidencial', 3400, 'Disponible'),
(305, 'Suite presidencial', 3400, 'Disponible'),
(306, 'Suite presidencial', 3400, 'Disponible');

