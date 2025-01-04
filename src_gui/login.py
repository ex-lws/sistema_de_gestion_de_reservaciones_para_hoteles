from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
import os

ui_path = os.path.join(os.path.dirname(__file__), "C:\\Users\\guich\OneDrive\\Documentos\\Desarrollo\\Python\\proyecto\\gui\\login.ui")
Form, Window = uic.loadUiType(ui_path)

class Login(Window, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.guardar_datos.clicked.connect(self.entrar)

    def entrar(self):
        nombre_usuario = self.nombre_usuario.text()
        contrasena_usuario = self.contrasea_usuario.text()

        usuario_correcto = "Luis Alberto"
        contrasena_correcta = "12345"

        if nombre_usuario == usuario_correcto and contrasena_usuario == contrasena_correcta:
            QMessageBox.information(self, "Éxito", "¡Ingreso exitoso!")
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")
            self.reject() 
