import psycopg2
from datetime import datetime
from conexion_bd import conectar_bd
import pytz

# Primera version para poder recoger datos del usuario por medio de inputs y agregarlos a la base de datos


def mostrar_instrucciones_reservacion():
    print ("==================")
    print ("Ingresa los siguientes datos:")
    print ("==================")

def recoger_datos():
    # Información necesaria para generar un reporte de reservación:

    # Recoger información del cliente
    print("--Información del cliente--")
    print("--Solicite la siguiente información:--")
    nombres_cliente = input("Nombre o nombres del cliente: ")
    apellido_paterno_cliente = input("Apellido paterno del cliente: ")
    apellido_materno_cliente = input("Apellido materno del cliente: ")
    correo_cliente = input("Correo electrónico del cliente: ")
    telefono_cliente = input("Teléfono del cliente: ")
    direccion_cliente = input("Dirección de cliente: ")

    # Recoger información de la habitación
    print("--Información de la habitación--")
    print("--Solicite la siguiente información:--")
    numero_habitacion = input("Número de habitación: ")
    tipo_habitacion = input("Tipo de la habitación: ")
    precio_noche_habitacion = input("Precio por noche: ")
    estado_habitacion = input("Disponibilidad: ")

    # Recoger información sobre la reservación
    print("Información propia del reporte--")
    print("--Solicite la siguiente información:--")
    check_in = input("Fecha de check in: ")
    check_out = input("Fecha de check out: ")
    fecha_reservacion = input("Fecha de reservación: ")
    precio_total = input("Monto total: ")

    # Recoger información sobre el método de pago
    print("Información acerca del pago--")
    print("--Solicite la siguiente información:--")
    fecha_pago = input("Fecha de pago: ")
    monto_pagado = input("Monto abonado: ")
    metodo_pago = input("Método de pago: ")

    #Retornamos los datos guardados con diccionarios dentro de diccionarios
    
    return {
        'cliente': {
            'nombres': nombres_cliente,
            'apellido_paterno': apellido_paterno_cliente,
            'apellido_materno': apellido_materno_cliente,
            'correo': correo_cliente,
            'telefono': telefono_cliente,
            'direccion': direccion_cliente
        },
        'habitacion': {
            'numero_habitacion': numero_habitacion,
            'tipo_habitacion': tipo_habitacion,
            'precio_noche': precio_noche_habitacion,
            'estado': estado_habitacion
        },
        'reservacion': {
            'check_in': check_in,
            'check_out': check_out,
            'fecha_reservacion': fecha_reservacion,
            'total': precio_total
        },
        'pago': {
            'fecha_pago': fecha_pago,
            'monto_pagado': monto_pagado,
            'metodo_pago': metodo_pago
        }
    }

def insertar_datos(cliente, habitacion, reservacion, pago):
    cursor = None  # Inicializar cursor
    conn = None    # Inicializar conexión

    try:
        conn = psycopg2.connect(
            dbname='bd_reservaciones',
            user='postgres',
            password='admin',
            host='localhost'
        )
        cursor = conn.cursor()

        # Obtener la zona horaria para el timestamp with time zone
        tz = pytz.timezone('America/New_York')  # Cambia a tu zona horaria

        # Convertir las fechas
        fecha_reservacion = datetime.now(tz)  # timestamp with time zone
        fecha_pago = datetime.now(tz)  # timestamp with time zone

        # Convertir check_in y check_out a timestamp without time zone
        check_in = datetime.strptime(reservacion['check_in'], '%Y-%m-%d %H:%M:%S')
        check_out = datetime.strptime(reservacion['check_out'], '%Y-%m-%d %H:%M:%S')

        # Insertar datos en la tabla de cliente
        query_cliente = """
        INSERT INTO cliente (
            nombres, 
            apellido_materno, 
            apellido_paterno, 
            correo, 
            telefono, 
            direccion
        )
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_cliente;
        """
        cursor.execute(query_cliente, (
            cliente['nombres'],
            cliente['apellido_paterno'],
            cliente['apellido_materno'],
            cliente['correo'],
            cliente['telefono'],
            cliente['direccion']
        ))
        id_cliente = cursor.fetchone()[0]

        # Insertar datos en la tabla de habitacion
        query_habitacion = """
        INSERT INTO habitacion (
            numero_habitacion, 
            tipo_habitacion, 
            precio_noche, 
            estado
        )
        VALUES (%s, %s, %s, %s) RETURNING id_habitacion;
        """
        cursor.execute(query_habitacion, (
            habitacion['numero_habitacion'],
            habitacion['tipo_habitacion'],
            habitacion['precio_noche'],
            habitacion['estado']
        ))
        id_habitacion = cursor.fetchone()[0]

        # Insertar datos en la tabla de reservación
        query_reservacion = """
        INSERT INTO reservacion (
            check_in,
            check_out,
            fecha_reservacion,
            total,
            id_cliente,
            id_habitacion
        )
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_reservacion;
        """
        cursor.execute(query_reservacion, (
            check_in,  # timestamp without time zone
            check_out,  # timestamp without time zone
            fecha_reservacion,  # timestamp with time zone
            reservacion['total'],
            id_cliente,
            id_habitacion
        ))
        id_reservacion = cursor.fetchone()[0]

        # Insertar datos en la tabla de pago
        query_pago = """
        INSERT INTO pago (
            fecha_pago,
            monto_pagado,
            metodo_pago,
            id_reservacion
        )
        VALUES (%s, %s, %s, %s) RETURNING id_pago;
        """
        cursor.execute(query_pago, (
            fecha_pago,  # timestamp with time zone
            pago['monto_pagado'],
            pago['metodo_pago'],
            id_reservacion  # Asegúrate de pasar id_reservacion aquí
        ))

        id_pago = cursor.fetchone()[0]

        # Guardar cambios
        conn.commit()
        print("Cliente, habitación, reservación y pago insertados con éxito.")
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        conn.rollback()  # Deshacer cambios en caso de error
    finally:
        if cursor:
            cursor.close()  # Asegúrate de cerrar el cursor solo si está abierto
        if conn:
            conn.close()  # Asegúrate de cerrar la conexión solo si está abierta

def actualizar_estado_habitacion(numero_habitacion):

    conexion = conectar_bd()
    
    if conexion:

        try:
            cursor = conexion.cursor()
            # Cambiar el estado de la habitacion a ocupada
            query = """
                UPDATE habitacion
                SET estado = 'Ocupada'
                WHERE numero_habitacion = %s AND estado = 'Disponible';
            """
            cursor.execute(query, (numero_habitacion,))
            conexion.commit()  # Confirmar los cambios en la base de datos

            if cursor.rowcount > 0:
                print ("--Actualización de la habitación exitosa.--")
                print(f"--La habitación {numero_habitacion} ha sido marcada como ocupada.--")
            else:
                print(f"--No se encontró una habitación disponible con el número {numero_habitacion}.")
            
        except Exception as e:
            print(f"--Error al actualizar el estado de la habitación: {e}")
        finally:
            conexion.close()
    else:
        print("--La conexión a la base de datos falló.--")

