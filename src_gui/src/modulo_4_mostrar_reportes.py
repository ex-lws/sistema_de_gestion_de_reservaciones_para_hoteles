from conexion_bd import conectar_bd

def mostrar_reportes_reservacion():
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM vista_reservaciones;")
            reportes = cursor.fetchall()

            if reportes:
                print("-- Estos son los reportes de reservación actuales --")

                # Encabezados con ajuste recomendado usando `str.format()`
                encabezados = "{:<25} | {:<35} | {:<10} | {:<30} | {:<22} | {:<20} | {:<10}".format(
                    "Nombre del cliente", "Correo del cliente", "Habitación",
                    "Fecha de reservación", "Check in", "Check out", "Monto total"
                )
                print(encabezados)
                print("-" * len(encabezados))

                # Imprimir los datos usando `str.format()`
                for reporte in reportes:
                    # Convertir valores a cadena para evitar errores
                    nombre = str(reporte[0])
                    correo = str(reporte[1])
                    habitacion = str(reporte[2])
                    fecha_reservacion = str(reporte[3]) if reporte[3] else "N/A"
                    check_in = str(reporte[4]) if reporte[4] else "N/A"
                    check_out = str(reporte[5]) if reporte[5] else "N/A"
                    monto_total = str(reporte[6]) if reporte[6] else "0.0"

                    print("{:<25} | {:<35} | {:<10} | {:<20} | {:<20} | {:<20} | {:<12}".format(
                        nombre, correo, habitacion, fecha_reservacion, check_in, check_out, monto_total
                    ))
            else:
                print("-- Aún no hay reportes... --")

            cursor.close()
        except Exception as e:
            print("-- Error al realizar la consulta: --", e)
        finally:
            conexion.close()
