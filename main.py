import sys
from PyQt5.QtWidgets import QApplication, QDialog
from src_gui.login import Login
from src_gui.menu_principal import VentanaMenuPrincipal

def main():
    app = QApplication(sys.argv)

    # Mostrar ventana de login
    # La clase Login es la autenticación
    entrar = Login()
    if entrar.exec_() == QDialog.Accepted:
        # Si el login es exitoso, se entra al menú principal
        menu = VentanaMenuPrincipal()
        menu.show()
        sys.exit(app.exec_())
    else:
        print("Cierre de la aplicación.")

if __name__ == "__main__":
    main()
