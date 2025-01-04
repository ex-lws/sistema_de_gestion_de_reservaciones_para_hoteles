from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic

Form, Window = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\ayuda.ui")

FormInformacion, WindowInformacion = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\informacion.ui")

class MostrarAyuda(Window, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.easter_eg_btn.clicked.connect(self.mostrar_nueva_ventana)

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

# Inicializar la aplicación y mostrar la ventana
if __name__ == "__main__":
    app = QApplication([])
    ventana = MostrarAyuda()
    ventana.show()
    app.exec_()
