import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5 import uic
import psycopg2
from datetime import datetime
import pytz

# Cargar el archivo modulo_2.ui 
FormVModulo3, WindowModulo3 = uic.loadUiType('C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_3.ui')

class VentanaModulo3(FormVModulo3, WindowModulo3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz
        self.initUI()

    def conectar_bd(self):
        # Método original para establecer la conexión a la base de datos extraído de la versíon de consola
        try:
            conexion = psycopg2.connect(
                host = "localhost",
                dbname="bd_reservaciones", 
                user="postgres", 
                password="admin", 
                port="5432"
            )
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
            return None

    def initUI(self):
        # Conectar el botón de guardar datos con la función correspondiente
        self.btn_insertar_datos_reservacion.clicked.connect(self.guardar_datos)

    def recoger_datos(self):
        # Recoger datos de las pestañas
        cliente = {
            'nombres': self.input_nombres_cliente.text(),
            'apellido_paterno': self.input_apellido_paterno_cliente.text(),
            'apellido_materno': self.input_apellido_materno_cliente.text(),
            'correo': self.input_correo_cliente.text(),
            'telefono': self.input_telefono_cliente.text(),
            'direccion': self.input_direccion_cliente.text()
        }

        habitacion = {
            'numero_habitacion': self.input_numero_habitacion.text(),
            'tipo_habitacion': self.input_tipo_habitacion.text(),
            'precio_noche': self.input_precio_habitacion.text(),
            'estado': self.input_estado_habitacion.text()
        }

        reservacion = {
            'check_in': self.input_check_in_reservacion.text(),
            'check_out': self.input_check_out_reservacion.text(),
            'fecha_reservacion': self.input_fecha_reservacion.text(),
            'total': self.input_total_reservacion.text()
        }

        pago = {
            'fecha_pago': self.input_fecha_pago_reservacion.text(),
            'monto_pagado': self.input_monto_pagado_reservacion.text(),
            'metodo_pago': self.input_metodo_pago_reservacion.text()
        }

        return cliente, habitacion, reservacion, pago
    
    def insertar_datos(self, cliente, habitacion, reservacion, pago):
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

            # Insertar datos en la base de datos
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

            conn.commit()
            QMessageBox.information(self, "Éxito", "Los datos se han guardado correctamente.")
        
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            conn.rollback()  # Deshacer cambios en caso de error
            QMessageBox.warning(self, "Error", "Hubo un problema al guardar los datos.")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def guardar_datos(self):
        cliente, habitacion, reservacion, pago = self.recoger_datos()
        self.insertar_datos(cliente, habitacion, reservacion, pago)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaModulo3()
    ventana.show()
    sys.exit(app.exec_())