-- Funcion y trigger para poder actualizar a ocupada una habitacion tras una reservacion --

CREATE OR REPLACE FUNCTION actualizar_estado_habitacion()
RETURNS TRIGGER AS $$
BEGIN
    -- Cambiar el estado de la habitación a 'Ocupado'
    UPDATE habitacion
    SET estado = 'Ocupado'
    WHERE numero_habitacion = NEW.numero_habitacion;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_actualizar_estado_habitacion
AFTER INSERT ON reservacion
FOR EACH ROW
EXECUTE FUNCTION actualizar_estado_habitacion();

-- Funcion y trigger para poder actualizar a disponible una habitacion tras borrar una reservacion -- 

CREATE OR REPLACE FUNCTION actualizar_estado_habitacion_al_borrar()
RETURNS TRIGGER AS $$
BEGIN
    -- Cambiar el estado de la habitación a 'Disponible' cuando se elimina una reservación
    UPDATE habitacion
    SET estado = 'Disponible'
    WHERE numero_habitacion = OLD.numero_habitacion;
    
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_borrar_reservacion
AFTER DELETE ON reservacion
FOR EACH ROW
EXECUTE FUNCTION actualizar_estado_habitacion_al_borrar();
