-- Crear la tabla habitacion
CREATE TABLE habitacion (
    numero_habitacion VARCHAR(10) PRIMARY KEY,
    tipo_habitacion VARCHAR(50) NOT NULL,
    precio_noche NUMERIC(10, 2) NOT NULL,
    estado VARCHAR(20) DEFAULT 'Disponible'
);

-- Crear la tabla cliente
CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT
);

-- Crear la tabla reservacion con ON DELETE CASCADE
CREATE TABLE reservacion (
    id_reservacion SERIAL PRIMARY KEY,
    check_in TIMESTAMP NOT NULL,
    check_out TIMESTAMP NOT NULL,
    fecha_reservacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(10, 2) NOT NULL,
    id_cliente INTEGER REFERENCES cliente(id_cliente) ON DELETE CASCADE,  -- ON DELETE CASCADE agregado
    numero_habitacion VARCHAR(10) REFERENCES habitacion(numero_habitacion) ON DELETE CASCADE  -- ON DELETE CASCADE agregado
);

-- Crear la tabla pago con ON DELETE CASCADE
CREATE TABLE pago (
    id_pago SERIAL PRIMARY KEY,
    fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    monto_pagado NUMERIC(10, 2) NOT NULL,
    metodo_pago VARCHAR(50),
    id_reservacion INTEGER REFERENCES reservacion(id_reservacion) ON DELETE CASCADE  -- ON DELETE CASCADE agregado
);
