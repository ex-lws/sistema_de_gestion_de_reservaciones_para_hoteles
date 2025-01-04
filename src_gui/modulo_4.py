from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QListWidgetItem
from PyQt5 import uic
import psycopg2
from datetime import datetime

FormModulo4, WindowModulo4 = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\modulo_4.ui")

class VentanaModulo4(WindowModulo4, FormModulo4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_volver_menu.clicked.connect(self.volver_a_menu_principal)
        self.mostrar_reportes_reservacion()

    def cerrar(self):
        """Función para cerrar la ventana."""
        self.close()

    def conectar_bd(self):
        try:
            conexion = psycopg2.connect(
                host="localhost",
                dbname="bd_reservaciones",
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
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM vista_reservaciones;")
                reportes = cursor.fetchall()

                # Limpiar la lista antes de agregar nuevos elementos
                self.lista_reportes.clear()

                if reportes:
                    for reporte in reportes:
                        # Suponiendo que los datos del reporte sean:
                        nombre = str(reporte[0])
                        correo = str(reporte[1])
                        habitacion = str(reporte[2])
                        fecha_reservacion = str(reporte[3]) if reporte[3] else "N/A"
                        check_in = str(reporte[4]) if reporte[4] else "N/A"
                        check_out = str(reporte[5]) if reporte[5] else "N/A"
                        monto_total = str(reporte[6]) if reporte[6] else "0.0"

                        # Formatear la fecha de reservación para mostrar solo la fecha sin la hora
                        if fecha_reservacion != "N/A":
                            try:
                                fecha_reservacion = datetime.strptime(fecha_reservacion, "%Y-%m-%d %H:%M:%S").date()
                            except ValueError:
                                pass  # Si no se puede formatear, dejarla como está

                        # Crear un texto para cada reporte con los datos de la reservación
                        item_text = (
                            f"Cliente: {nombre}\n"
                            f"Correo: {correo}\n"
                            f"Habitación: {habitacion}\n"
                            f"Fecha de reservación: {fecha_reservacion}\n"
                            f"Check-in: {check_in}\n"
                            f"Check-out: {check_out}\n"
                            f"Monto total: ${monto_total}\n"
                        )

                        # Mostrar el texto en la consola antes de agregarlo al QListWidget
                        print(item_text)

                        # Agregar el item al QListWidget
                        item = QListWidgetItem(item_text)
                        self.lista_reportes.addItem(item)

                else:
                    self.lista_reportes.addItem("Aún no hay reportes de reservación disponibles.")

                cursor.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al realizar la consulta: {e}")
            finally:
                conexion.close()


# Inicializar la aplicación y mostrar la ventana
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaModulo4()
    ventana.show()
    app.exec_()
