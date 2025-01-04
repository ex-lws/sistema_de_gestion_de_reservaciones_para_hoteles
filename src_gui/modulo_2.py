from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QVBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget
from PyQt5 import uic
import psycopg2

# Cargar el archivo modulo_2.ui 
Form, Window = uic.loadUiType('C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_2.ui')

# Creamos la clase del módulo 2
class VentanaDisponibilidad(Window, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Aquí va la conección de los botones de TODAS LAS PESTAÑAS:
        self.btn_verificar_disponibilidad_tipo.clicked.connect(self.obtener_habitaciones_disponibles_por_tipo)
        self.btn_verificar_disponibilidad_precio.clicked.connect(self.obtener_habitaciones_disponibles_por_precio)
        self.btn_verificar_disponibilidad_numero.clicked.connect(self.consultar_disponibilidad_por_numero)  
        self.btn_verificar_disponibilidad_estado.clicked.connect(self.consultar_disponibilidad_por_estado)
        self.btn_ayuda_disponibilidad.clicked.connect(self.mostrar_cuadro_dialogo)

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
        
        numero_habitacion_consulta = int(numero_habitacion_consulta)
        
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



if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaDisponibilidad()
    ventana.show()
    app.exec_()