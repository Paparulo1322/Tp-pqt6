from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QLineEdit, QWidget

RUTA_UI = Path(__file__).parent / "login.ui"


class VentanaLogin(QWidget):
    """Controla la pantalla de inicio de sesión. El diseño vive en login.ui."""

    def __init__(self, servicio):
        super().__init__()
        uic.loadUi(RUTA_UI, self)
        self.servicio = servicio
        self._conectar_eventos()

    def _conectar_eventos(self):
        self.btn_login.clicked.connect(self.iniciar_sesion)
        self.input_password.returnPressed.connect(self.iniciar_sesion)
        self.chk_mostrar_password.toggled.connect(self.alternar_password)

    def iniciar_sesion(self):
        usuario = self.input_usuario.text().strip()
        password = self.input_password.text()

        error = self._validar(usuario, password)
        if error:
            self._mostrar_mensaje(error, "error")
            return

        if self.servicio.autenticar(usuario, password):
            nombre = self.servicio.nombre_de(usuario)
            self._mostrar_mensaje(f"Sesión iniciada como {nombre} (simulación).", "exito")
        else:
            self._mostrar_mensaje("Usuario o contraseña incorrectos.", "error")

    def alternar_password(self, visible):
        modo = QLineEdit.EchoMode.Normal if visible else QLineEdit.EchoMode.Password
        self.input_password.setEchoMode(modo)

    def limpiar(self):
        """Deja la pantalla lista para volver a usarse."""
        self.input_password.clear()
        self.chk_mostrar_password.setChecked(False)
        self._mostrar_mensaje("")
        self.input_usuario.setFocus()

    def _validar(self, usuario, password):
        if not usuario:
            return "Ingresá tu usuario o correo electrónico."
        if not password:
            return "Ingresá tu contraseña."
        return None

    def _mostrar_mensaje(self, texto, tipo="info"):
        self.label_mensaje.setText(texto)
        self.label_mensaje.setProperty("tipo", tipo)
        self.label_mensaje.style().unpolish(self.label_mensaje)
        self.label_mensaje.style().polish(self.label_mensaje)
