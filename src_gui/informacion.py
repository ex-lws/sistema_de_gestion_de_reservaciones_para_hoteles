from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

# Cargar el archivo .ui de Qt Designer
Form, Window = uic.loadUiType("C:\\Users\\guich\\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\informacion.ui")

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
    ventana = MostrarInformacion() 
    ventana.show() 
    app.exec_() 
