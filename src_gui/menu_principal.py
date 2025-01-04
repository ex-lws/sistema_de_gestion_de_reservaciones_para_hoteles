from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QVBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget
from PyQt5 import uic
import psycopg2
from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5 import uic
import psycopg2
from datetime import datetime
import pytz
import matplotlib.pyplot as plt


# Cargar los archivos .ui
FormMenu, WindowMenu = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\menu_principal.ui")
FormAyuda, WindowAyuda = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\ayuda.ui")
FormModulo1, WindowModulo1 = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_1.ui")
FormModulo2, WindowModulo2 = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_2.ui")
FormModulo4, WindowModulo4 = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_4.ui")
FormInformacion, WindowInformacion = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\informacion.ui")
Form, Window = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\informacion.ui")
FormVModulo3, WindowModulo3 = uic.loadUiType('C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_3.ui')
FormModulo5, WindowModulo5 = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_5.ui")
# Ventana del menú principal

class VentanaMenuPrincipal(WindowMenu, FormMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Conectar botones
        self.mostrar_ayuda.clicked.connect(self.abrir_ventana_ayuda)
        self.mostrar_habitaciones.clicked.connect(self.abrir_ventana_modulo_1)
        self.mostrar_disponibilidad.clicked.connect(self.abrir_ventana_modulo_2)
        self.consultar_reservaciones.clicked.connect(self.abrir_ventana_modulo_4)
        self.proceso_reservacion.clicked.connect(self.abrir_ventana_modulo_3)
        self.estadisticas.clicked.connect(self.abrir_ventana_modulo_5)
        self.salir_al_login.clicked.connect(self.salir)

    def abrir_ventana_ayuda(self):
        # Crear instancia de la ventana de ayuda y mostrarla
        self.ventana_ayuda = VentanaAyuda()
        self.ventana_ayuda.show()
        self.hide()  # Ocultar la ventana del menú principal (no cerrarla)

    def abrir_ventana_modulo_1(self):
        # Crear instancia de la ventana del módulo 1 y mostrarla
        self.ventana_modulo_1 = VentanaModulo1(self)  # Pasa la instancia de la ventana principal
        self.ventana_modulo_1.show()
        self.hide()  # Ocultar la ventana del menú principal

    def abrir_ventana_modulo_2(self):
        self.ventana_modulo_2 = VentanaModulo2()  # Crea la nueva ventana
        self.ventana_modulo_2.show()  # Muestra la nueva ventana
        self.hide()  # Oculta el menú principal

    def abrir_ventana_modulo_3(self):
        self.ventana_modulo_3 = VentanaModulo3()  # Crea la nueva ventana
        self.ventana_modulo_3.show()  # Muestra la nueva ventana
        self.hide()  # Oculta el menú principal

    def abrir_ventana_modulo_4(self):
        self.ventana_modulo_4 = VentanaModulo4()  # Crea la nueva ventana
        self.ventana_modulo_4.show()  # Muestra la nueva ventana
        self.hide()  # Oculta el menú principal

    def abrir_ventana_modulo_5(self):
        self.ventana_modulo_5 = ventanaModulo5()  # Crea la nueva ventana
        self.ventana_modulo_5.show()  # Muestra la nueva ventana
        self.hide()  # Oculta el menú principal

    def salir(self):
        # Lógica para salir (ejemplo: cerrar la aplicación)
        print("Saliendo al login...")
        self.close()

class VentanaAyuda(WindowAyuda, FormAyuda):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botón "Volver"
        self.boton_volver_menu.clicked.connect(self.volver_menu)
        self.easter_eg_btn.clicked.connect(self.mostrar_nueva_ventana)
        
    def volver_menu(self):
        # Regresa al menú principal
        self.close()
        self.ventana_menu = VentanaMenuPrincipal()  # Crea una nueva instancia del menú principal
        self.ventana_menu.show()

    def mostrar_nueva_ventana(self):
            # Crear y mostrar la nueva ventana
            self.nueva_ventana = AbrirInformacion()
            self.nueva_ventana.show()

# Clase para la nueva ventana
class AbrirInformacion(WindowInformacion, FormInformacion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# Conectar el botón "volver" a la función cerrar
        self.volver_btn.clicked.connect(self.cerrar)

    def cerrar(self):
        """Función para cerrar la ventana."""
        self.close()

class VentanaModulo1(WindowModulo1, FormModulo1):
    def __init__(self, ventana_menu):
        super().__init__()
        self.setupUi(self)
        # Eventos.
        self.ventana_menu = ventana_menu
        self.volver_btn.clicked.connect(self.volver_menu)
        self.mostrarHabitaciones()

    def mostrarHabitaciones(self):
        lista_habitaciones = {

        'Habitacion 101' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama king'], 
            'Precio' : 450},

        'Habitacion 102' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama queen'], 
            'Precio' : 400},

        'Habitacion 103' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama individual'], 
            'Precio' : 350},

        'Habitacion 104' : {
            'Tipo' : 'Sencilla', 
            'Características' : ['TV', 'Baño', 'Cama individual'], 
            'Precio' : 350},

        'Habitacion 105' : {
            'Tipo' : 'Doble', 
            'Características' : ['TV', 'Baño amplio', 'Comedor', 'Dos camas king', 'Wi-Fi'], 
            'Precio' : 850},

        'Habitacion 106' : {
            'Tipo' : 'Doble', 
            'Características' : ['TV', 'Baño amplio', 'Comedor', 'Dos camas individuales', 'Wi-Fi'], 
            'Precio' : 830},

        'Habitacion 201' : {
            'Tipo' : 'Suite', 
            'Características' : ['TV grande', 'Jacuzzi', 'Comedor','Cama king y sofá cama', 'Wi-Fi', 'Sistema de sonido'], 
            'Precio' : 1600},

        'Habitacion 202' : {
            'Tipo' : 'Suite', 
            'Características' : ['TV grande', 'Jacuzzi', 'Comedor','Cama queen y sofá cama', 'Wi-Fi', 'Sistema de sonido'], 
            'Precio' : 1500},

        'Habitacion 203' : {
            'Tipo' : 'Suite', 
            'Características' : ['TV grande', 'Jacuzzi', 'Comedor','Cama individual y sofá cama', 'Wi-Fi', 'Sistema de sonido'], 
            'Precio' : 1400},

        'Habitacion 204' : {
            'Tipo' : 'Familiar', 
            'Características' : ['TV grande', 'Baño amplio', 'Comedor','Dos camas individuales' , 'Wi-Fi', 'Sistema de sonido', 'Juegos de actividades para niños'],
            'Precio' : 1700},

        'Habitacion 205' : {
            'Tipo' : 'Familiar', 
            'Características' :  ['TV grande', 'Jacuzzi', 'Comedor','Dos camas individuales' , 'Wi-Fi', 'Sistema de sonido', 'Juegos de actividades para niños'],
            'Precio' : 1800},

        'Habitacion 206' : {
            'Tipo' : 'Familiar', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Dos camas individuales' , 'Wi-Fi', 'Sistema de sonido', 'Juegos de actividades para niños'], 
            'Precio' : 1900},

        'Habitacion 301' : {
            'Tipo' : 'Deluxe', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi', 'Sistema de sonido', 'Mini bar', 'Calefacción'], 
            'Precio' : 2600},

        'Habitacion 302' : {
            'Tipo' : 'Deluxe', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama queen' , 'Wi-Fi', 'Sistema de sonido', 'Mini bar', 'Calefacción'], 
            'Precio' : 2500},

        'Habitacion 303' : {
            'Tipo' : 'Deluxe', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama queen' , 'Wi-Fi', 'Sistema de sonido', 'Mini bar', 'Calefacción'],
            'Precio' : 2500},

        'Habitacion 304' : {
            'Tipo' : 'Suite precidencial', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi de alta velocidad', 'Sistema de sonido premium', 'Mini bar', 'Calefacción', 'Balcón'],
            'Precio' : 3400},

        'Habitacion 305' : {
            'Tipo' : 'Suite precidencial', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi de alta velocidad', 'Sistema de sonido premium', 'Mini bar', 'Calefacción', 'Balcón'], 
            'Precio' : 3400},

        'Habitacion 306' : {
            'Tipo' : 'Suite precidencial', 
            'Características' : ['TV grande', 'Jacuzzi y baño', 'Comedor','Cama king' , 'Wi-Fi de alta velocidad', 'Sistema de sonido premium', 'Mini bar', 'Calefacción', 'Balcón'], 
            'Precio' : 3400},

        }

        # Limpieza del widget que albergará el diccionario de habitaciones
        self.lista_habitaciones.clear()

        # Agregar cada habitación al QListWidget con un ciclo for

        for numero, detalles in lista_habitaciones.items():
            item_text = f'Número: {numero}\nTipo: {detalles["Tipo"]}\nCaracterísticas: {", ".join(detalles["Características"])}\nPrecio por noche: ${detalles["Precio"]}\n'
            self.lista_habitaciones.addItem(item_text)

    def volver_menu(self):
        # Cierra la ventana del módulo 1 y vuelve al menú principal
        self.close()
        self.ventana_menu.show()  # Muestra la ventana principal que ya está abierta
        
#C CLASE PARA MOSTRAR EL MÓDULO 2.

class VentanaModulo2(WindowModulo2, FormModulo2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Aquí puedes agregar conexiones, como botones o cualquier otro widget
        self.btn_verificar_disponibilidad_tipo.clicked.connect(self.obtener_habitaciones_disponibles_por_tipo)
        self.btn_verificar_disponibilidad_precio.clicked.connect(self.obtener_habitaciones_disponibles_por_precio)
        self.btn_verificar_disponibilidad_numero.clicked.connect(self.consultar_disponibilidad_por_numero)  
        self.btn_verificar_disponibilidad_estado.clicked.connect(self.consultar_disponibilidad_por_estado)
        self.btn_ayuda_disponibilidad.clicked.connect(self.mostrar_cuadro_dialogo)
        self.btn_volver_al_menu.clicked.connect(self.volver_menu)

    def conectar_bd(self):
        # Método original para establecer la conexión a la base de datos extraído de la versíon de consola
        try:
            conexion = psycopg2.connect(
                host = "localhost",
                dbname="bd", 
                user="postgres", 
                password="admin", 
                port="5432"
            )
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
            return None

    # Método que busca habitaciones disponibles por TIPO

    def obtener_habitaciones_disponibles_por_tipo(self):
        # Qlineedit = input del usuario
        tipo_habitacion_consulta = self.entrada_consultar_disponibilidad_tipo.text().strip().capitalize()
        
        if not tipo_habitacion_consulta:
            QMessageBox.warning(self, "ADVERTENCIA!", "Por favor ingrese un tipo de habitación válido.")
            return
        
        # Conectamos con la base de datos
        
        conexion = self.conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta personalziada
                query = "SELECT numero_habitacion, precio_noche FROM habitacion WHERE estado = 'Disponible' and tipo_habitacion = %s;"
                cursor.execute(query, (tipo_habitacion_consulta,))
                habitaciones_disponibles_por_tipo = cursor.fetchall()

                if habitaciones_disponibles_por_tipo:
                    # Si hay éxito, se limpia el Qlist
                    self.lista_habitaciones_disponibles_tipo.clear()

                    # Imprime las habitaciones en el Qlist y las añade
                    for habitacion in habitaciones_disponibles_por_tipo:
                        numero, precio = habitacion
                        self.lista_habitaciones_disponibles_tipo.addItem(f"Número: {numero}, Precio por noche: ${precio}")

                else:
                    QMessageBox.information(self, "SIN RESULTADOS", "No se encontraron habitaciones disponibles de ese tipo...")
            except Exception as e:
                QMessageBox.critical(self, "ERROR", "Error al realizar la consulta.")
                print(e)
            finally:
                cursor.close()
                conexion.close()
        else:
            QMessageBox.critical(self, "ERROR", "No se pudo conectar con la base de datos.")

        # Método que busca habitaciones disponibles por PRECIO

    def obtener_habitaciones_disponibles_por_precio(self):

        # QLineEdit para guardar el precio ingresado por el usuario = precio_maximo
        try:
            precio_maximo = float(self.entrada_consultar_precio.text().strip())
        except ValueError:
            QMessageBox.warning(self, "ADVERTENCIA", "Por favor ingrese un precio válido.")
            return

        # Conectar con la base de datos
        conexion = self.conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para buscar habitaciones disponibles con precio menor o igual al ingresado
                query = """
                SELECT numero_habitacion, tipo_habitacion, precio_noche 
                FROM habitacion 
                WHERE estado = 'Disponible' AND precio_noche <= %s;
                """
                cursor.execute(query, (precio_maximo,))
                habitaciones_disponibles_por_precio = cursor.fetchall()

                if habitaciones_disponibles_por_precio:
                    # Limpiar el widget de la lista antes de mostrar los resultados
                    self.lista_habitaciones_disponibles_precio.clear()

                    # Añadir cada habitación al QListWidget y mostralas al usuario
                    for numero, tipo, precio in habitaciones_disponibles_por_precio:
                        self.lista_habitaciones_disponibles_precio.addItem(
                            f"Número: {numero}, Tipo: {tipo}, Precio por noche: ${precio}"
                        )

                else:
                    QMessageBox.information(self, "SIN RESULTADOS", "No se encontraron habitaciones disponibles dentro del rango de precio.")
            except Exception as e:
                QMessageBox.critical(self, "ERROR", "Error al realizar la consulta.")
                print(e)
            finally:
                cursor.close()
                conexion.close()
        else:
            QMessageBox.critical(self, "ERROR", "No se pudo conectar con la base de datos.")

    # METODO QUE BUSCA DISPONIBLIDAD POR NUMERO

    def consultar_disponibilidad_por_numero(self):
        numero_habitacion_consulta = self.entrada_consultar_disponibilidad_numero.text().strip()
        
        if not numero_habitacion_consulta.isdigit():
            QMessageBox.warning(self, "ADVERTENCIA", "Por favor ingrese un número de habitación válido.")
            return
        
        numero_habitacion_consulta = str(numero_habitacion_consulta)
        
        conexion = self.conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    SELECT tipo_habitacion, precio_noche 
                    FROM habitacion 
                    WHERE estado = %s AND numero_habitacion = %s;
                """
                cursor.execute(query, ('Disponible', numero_habitacion_consulta))
                habitaciones_disponibles_por_numero = cursor.fetchone()

                if habitaciones_disponibles_por_numero:
                    tipo_habitacion, precio_noche = habitaciones_disponibles_por_numero
                    self.lista_habitaciones_disponibles_numero.clear()
                    self.lista_habitaciones_disponibles_numero.addItem(f"Habitación {numero_habitacion_consulta}: {tipo_habitacion}, Precio por noche: ${precio_noche}")
                else:
                    QMessageBox.information(self, "SIN RESULTADOS", "No se encontró una habitación disponible con ese número.")
            except Exception as e:
                QMessageBox.critical(self, "ERROR", "Error al realizar la consulta.")
                print(e)
            finally:
                cursor.close()
                conexion.close()
        else:
            QMessageBox.critical(self, "ERROR", "No se pudo conectar con la base de datos.")

    def consultar_disponibilidad_por_estado(self):
        conexion = self.conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para obtener habitaciones con estado 'Disponible' sin importar mayúsculas/minúsculas
                cursor.execute("SELECT numero_habitacion, tipo_habitacion, estado FROM habitacion WHERE LOWER(estado) = 'disponible';")
                habitaciones = cursor.fetchall()

                # Limpiar lista actual antes de agregar los nuevos datos
                self.lista_habitaciones_disponibles_estado.clear()

                if habitaciones:
                    for habitacion in habitaciones:
                        self.lista_habitaciones_disponibles_estado.addItem(f"Número: {habitacion[0]}, Tipo: {habitacion[1]}")
                else:
                    self.lista_habitaciones_disponibles_estado.addItem("No hay habitaciones disponibles.")

                cursor.close()
            except Exception as e:
                self.lista_habitaciones_disponibles_estado.addItem(f"Error al realizar la consulta: {e}")
            finally:
                conexion.close()

    def mostrar_cuadro_dialogo(self):
        # Crear un cuadro de diálogo con mensaje
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Information)  # Establecer el icono (puede ser Information, Warning, Error, etc.)
        mensaje.setText("¡La disponibilidad en gran parte depende de los húespedes y del personal de mantenimiento!")  # Texto del mensaje
        mensaje.setWindowTitle("Sobre la disponibilidad")  # Título de la ventana del cuadro de diálogo
        mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)  # Botones estándar (puedes agregar más si lo necesitas)
        
        # Mostrar el cuadro de diálogo y capturar la respuesta del usuario
        respuesta = mensaje.exec_()

        # Verificar qué botón fue presionado
        if respuesta == QMessageBox.Ok:
            print("Se presionó el botón Ok")
        elif respuesta == QMessageBox.Cancel:
            print("Se presionó el botón Cancel")
    
    def volver_menu(self):
        # Regresa al menú principal
        self.close()  # Cierra esta ventana
        self.ventana_menu = VentanaMenuPrincipal()  # Crea una nueva instancia del menú principal
        self.ventana_menu.show()

class VentanaModulo3(FormVModulo3, WindowModulo3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz
        self.initUI()
        self.btn_volver_menu.clicked.connect(self.volver_menu)

    def conectar_bd(self):
        # Método original para establecer la conexión a la base de datos extraído de la versíon de consola
        try:
            conexion = psycopg2.connect(
                host = "localhost",
                dbname="bd", 
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

        reservacion = {
            'check_in': self.input_check_in_reservacion.text(),
            'check_out': self.input_check_out_reservacion.text(),
            'fecha_reservacion': self.input_fecha_reservacion.text(),
            'total': self.input_total_reservacion.text(),
            'numero_habitacion': self.input_numero_habitacion.text()
        }

        pago = {
            'fecha_pago': self.input_fecha_pago_reservacion.text(),
            'monto_pagado': self.input_monto_pagado_reservacion.text(),
            'metodo_pago': self.input_metodo_pago_reservacion.text()
        }

        return cliente, reservacion, pago
    
    def insertar_datos(self, cliente, reservacion, pago):
        cursor = None  # Inicializar cursor
        conn = None    # Inicializar conexión

        try:
            conn = psycopg2.connect(
                dbname='bd',
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

            # Insertar datos en la tabla de reservación
            query_reservacion = """
            INSERT INTO reservacion (
                check_in,
                check_out,
                fecha_reservacion,
                total,
                id_cliente,
                numero_habitacion
            )
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_reservacion;
            """
            cursor.execute(query_reservacion, (
                check_in,
                check_out,
                fecha_reservacion,
                reservacion['total'],
                id_cliente,
                reservacion['numero_habitacion']
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
                fecha_pago,
                float(pago['monto_pagado']),  # Convertir a float si es necesario
                pago['metodo_pago'],
                id_reservacion  # Usar el id de la reservación creada anteriormente
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
        cliente, reservacion, pago = self.recoger_datos()
        self.insertar_datos(cliente, reservacion, pago)

    def volver_menu(self):
        # Regresa al menú principal
        self.close()  # Cierra esta ventana
        self.ventana_menu = VentanaMenuPrincipal()  # Crea una nueva instancia del menú principal
        self.ventana_menu.show()

class VentanaModulo4(WindowModulo4, FormModulo4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_volver_menu.clicked.connect(self.volver_menu)
        self.mostrar_reportes_reservacion()
        self.btn_habilitar_habitacion.clicked.connect(self.habilitar_habitacion)
        

    def cerrar(self):
        """Función para cerrar la ventana."""
        self.close()

    def conectar_bd(self):
        try:
            conexion = psycopg2.connect(
                host="localhost",
                dbname="bd",
                user="postgres",
                password="admin",
                port="5432"
            )
            print("Conexión exitosa")
            return conexion
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al conectar a la base de datos: {e}")
            print(f"Error al conectar: {e}")
            return None

    def mostrar_reportes_reservacion(self):
        conexion = self.conectar_bd()
        if conexion:
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute("SELECT * FROM reporte_reservacion_basico;")
                        reportes = cursor.fetchall()

                        # Limpiar la lista antes de agregar nuevos elementos
                        self.lista_reportes.clear()

                        if reportes:
                            for reporte in reportes:

                                nombre_completo = str(reporte[0]) if reporte[0] else "N/A"
                                numero_habitacion = str(reporte[1])
                                tipo_habitacion = str(reporte[2])
                                check_in = str(reporte[3])
                                check_out = str(reporte[4])
                                total = str (reporte[5])
                                fecha_pago = str (reporte[6])
                                monto_pagado = str (reporte[7])
                                
                                # Crear un texto para cada reporte con los datos de la reservación
                                item_text = (
                                    f"Nombre del huésped: {nombre_completo}\n"
                                    f"Número de habitación: {numero_habitacion}\n"
                                    f"Tipo de habitación: {tipo_habitacion}\n"
                                    f"Check in: {check_in}\n"
                                    f"Check out: {check_out}\n"
                                    f"Monto total: {total}\n"
                                    f"Fecha de pago: {fecha_pago}\n"
                                    f"Monto pagado: {monto_pagado}\n"
                                    
                                )

                                # Mostrar el texto en la consola antes de agregarlo al QListWidget
                                print(item_text)

                                # Agregar el item al QListWidget
                                self.lista_reportes.addItem(item_text)

                        else:
                            self.lista_reportes.addItem("Aún no hay reportes de reservación disponibles.")
                except (Exception,) as e:
                    QMessageBox.critical(self, "Error", f"Error al realizar la consulta: {e}")
                finally:
                    conexion.close()

    def habilitar_habitacion(self):
        # Variable que recoge los datos del input de UI
        numero_habitacion_para_habilitar = self.input_numero_habitacion_habilitar.text().strip()

        # Validar que el input sea un número
        if not numero_habitacion_para_habilitar.isdigit():
            QMessageBox.warning(self, "ADVERTENCIA", "Por favor, ingrese un número de habitación válido para habilitarla.")
            return

        # Convertimos este input a string para poder usarlo en el query
        numero_habitacion_para_habilitar = str(numero_habitacion_para_habilitar)
        
        conexion = self.conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM reservacion WHERE numero_habitacion = %s;"
                cursor.execute(query, (numero_habitacion_para_habilitar,))

                # Confirmar la eliminación
                conexion.commit()
                QMessageBox.information(self, "ÉXITO", f"La habitación {numero_habitacion_para_habilitar} ha sido habilitada correctamente.")
            
            except Exception as e:
                QMessageBox.critical(self, "ERROR", "Error al realizar la operación de habilitación de la habitación.")
                print(e)
            finally:
                cursor.close()
                conexion.close()
        else:
            QMessageBox.critical(self, "ERROR", "No se pudo conectar con la base de datos.")

    def volver_menu(self):
        # Regresa al menú principal
        self.close()  # Cierra esta ventana
        self.ventana_menu = VentanaMenuPrincipal()  # Crea una nueva instancia del menú principal
        self.ventana_menu.show()

class ventanaModulo5(FormModulo5, WindowModulo5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_volver_menu.clicked.connect(self.volver_menu)
        self.btn_ocupacion.clicked.connect(self.tasaOcupacion)
        self.btn_reservadas.clicked.connect(self.tasaHabitacionMasReservada)
        self.btn_estancia.clicked.connect(self.tasaPromedioEstancia)

    def cerrar(self):
        """Función para cerrar la ventana."""
        self.close()

    def conectar_bd(self):
        try:
            conexion = psycopg2.connect(
                host="localhost",
                dbname="bd",
                user="postgres",
                password="admin",
                port="5432"
            )
            print("Conexión exitosa")
            return conexion
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al conectar a la base de datos: {e}")
            print(f"Error al conectar: {e}")
            return None
        
    def tasaOcupacion(self):
        conexion = self.conectar_bd()
        if conexion:
            print("Conexión exitosa a la base de datos.")
            cursor = conexion.cursor()
            print ("--Mostrando gráficas sobr la tasa de ocupación del hotel.--")

            # Consulta para obtener el número total de habitaciones y las habitaciones ocupadas
            cursor.execute("SELECT COUNT(*) FROM habitacion")
            total_habitaciones = cursor.fetchone()[0]
            
            # Contar habitaciones con estado distinto a 'Disponible' (ocupadas o reservadas)
            cursor.execute("SELECT COUNT(*) FROM habitacion WHERE estado != 'Disponible'")
            habitaciones_ocupadas = cursor.fetchone()[0]

            # Calcular tasa de ocupación
            tasa = (habitaciones_ocupadas / total_habitaciones) * 100
            print(f"Tasa de ocupación: {tasa:.2f}%")

            # Graficar
            categorias = ['Ocupadas', 'Disponibles']
            valores = [habitaciones_ocupadas, total_habitaciones - habitaciones_ocupadas]

            plt.bar(categorias, valores, color=['red', 'green'])
            plt.title("Tasa de Ocupación")
            plt.ylabel("Número de Habitaciones")
            plt.show()

    def tasaHabitacionMasReservada(self):
        conexion = self.conectar_bd()
        if conexion: 
            cursor = conexion.cursor()
            print("--Mostrando gráfica sobre las habitaciones más reservadas.--")

            # Consulta para obtener las habitaciones más reservadas
            cursor.execute("SELECT tipo_habitacion, COUNT(*) AS habitaciones_ocupadas FROM habitacion WHERE estado != 'Disponible' GROUP BY tipo_habitacion ORDER BY habitaciones_ocupadas DESC")

            # Obtener todos los resultados de la consulta
            tipos_habitacion_reservadas = cursor.fetchall()

            # Separar los tipos de habitación y las cantidades de habitaciones ocupadas
            tipos = [fila[0] for fila in tipos_habitacion_reservadas]  # tipo_habitacion
            ocupadas = [fila[1] for fila in tipos_habitacion_reservadas]  # habitaciones_ocupadas

            # Mostrar la gráfica
            plt.bar(tipos, ocupadas, color='blue')
            plt.title("Tipos de Habitación Más Reservados")
            plt.xlabel("Tipo de Habitación")
            plt.ylabel("Número de Habitaciones Ocupadas")
            plt.xticks(rotation=45)  # Rotar las etiquetas del eje x si son largas
            plt.tight_layout()  # Ajustar el espaciado para que todo se vea bien
            plt.show()

    def tasaPromedioEstancia(self):
        conexion = self.conectar_bd()
        if conexion: 
            cursor = conexion.cursor()
            print("--Mostrando gráfico sobre el tiempo promedio de estancia de los huéspedes.--")

            # Consulta para obtener el tiempo promedio de estancia
            cursor.execute("SELECT AVG(EXTRACT(DAY FROM (check_out - check_in))) AS promedio_estancia FROM reservacion")

            # Obtener el resultado de la consulta
            promedio_estancia = cursor.fetchone()[0]

            # Mostrar la gráfica
            # Dado que es un solo valor, usaremos una gráfica de barras de una sola barra
            plt.bar(['Promedio de Estancia'], [promedio_estancia], color='green')
            plt.title("Promedio de Estancia de los Huéspedes")
            plt.ylabel("Días de Estancia Promedio")
            plt.tight_layout()  # Ajustar el espaciado para que todo se vea bien
            plt.show()

    def volver_menu(self):
        # Regresa al menú principal
        self.close()  # Cierra esta ventana
        self.ventana_menu = VentanaMenuPrincipal()  # Crea una nueva instancia del menú principal
        self.ventana_menu.show()

class MostrarInformacion(Window, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configurar la UI

        # Conectar el botón "volver" a la función cerrar
        self.volver_btn.clicked.connect(self.cerrar)

    def cerrar(self):
        """Función para cerrar la ventana."""
        self.close()

# Inicializar la aplicación
if __name__ == "__main__":
    app = QApplication([])

    # Crear la instancia del menú principal
    ventana_menu = VentanaMenuPrincipal()
    ventana_menu.show()

    app.exec_()
