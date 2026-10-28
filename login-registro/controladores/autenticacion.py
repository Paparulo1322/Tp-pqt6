"""Servicio de autenticación SIMULADO, en memoria.

No es un sistema de producción: los usuarios se pierden al cerrar la app,
no hay límite de intentos, ni sesiones, ni base de datos.
Lo que sí hace bien desde ahora: nunca guarda la contraseña, solo su hash con sal.

Este módulo no importa nada de PyQt6: no sabe que existen las pantallas.
"""
import hashlib
import hmac
import os

LONGITUD_MINIMA_PASSWORD = 8
ITERACIONES = 600_000


class ServicioAutenticacion:

    def __init__(self):
        # "juan@gmail.com" -> {"nombre": ..., "apellido": ..., "sal": ..., "hash": ...}
        self._usuarios = {}

    def registrar(self, nombre, apellido, usuario, password):
        """Registra un usuario. Lanza ValueError si algo no cumple las reglas."""
        clave = self._normalizar(usuario)
        minimo = LONGITUD_MINIMA_PASSWORD

        if not nombre.strip() or not apellido.strip():
            raise ValueError("Completá tu nombre y apellido.")
        if not clave:
            raise ValueError("Completá tu usuario o gmail electrónico.")
        if len(password) < minimo:
            raise ValueError(f"La contraseña necesita al menos {minimo} caracteres.")
        if clave in self._usuarios:
            raise ValueError("Ese usuario ya está registrado.")

        sal = os.urandom(16)
        self._usuarios[clave] = {
            "nombre": nombre.strip(),
            "apellido": apellido.strip(),
            "sal": sal,
            "hash": self._calcular_hash(password, sal),
        }

    def autenticar(self, usuario, password):
        """True solo si el usuario existe y la contraseña coincide."""
        datos = self._usuarios.get(self._normalizar(usuario))
        if datos is None:
            return False
        hash_calculado = self._calcular_hash(password, datos["sal"])
        return hmac.compare_digest(hash_calculado, datos["hash"])

    def nombre_de(self, usuario):
        """Nombre de pila de un usuario registrado (o None)."""
        datos = self._usuarios.get(self._normalizar(usuario))
        return datos["nombre"] if datos else None

    @staticmethod
    def _normalizar(usuario):
        return usuario.strip().lower()

    @staticmethod
    def _calcular_hash(password, sal):
        return hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), sal, ITERACIONES
        )
