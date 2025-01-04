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

FormModulo5, WindowModulo5 = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_5.ui")

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
            plt.tight_layout()
            plt.show()
