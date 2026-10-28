# Login y registro con PyQt6

Aplicación de escritorio con dos pantallas diseñadas en Qt Designer y controladas
con clases de Python. Trabajo práctico de Programación Orientada a Objetos.

> **Importante:** la autenticación es una SIMULACIÓN. Los usuarios viven en
> memoria y se pierden al cerrar la aplicación. No es un sistema seguro ni
> apto para datos reales.

## Capturas
![Login](capturas/login.png)
![Registro](capturas/registro.png)

## Requisitos
- Python 3.10 o más nuevo

## Instalación

Windows (PowerShell):

    py -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

macOS / Linux:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt

## Ejecución

    python main.py

Siempre desde la carpeta del proyecto.

## Funcionalidades
- [x] Login y registro diseñados en Qt Designer (`.ui`) y cargados con `uic.loadUi()`
- [x] Una clase por pantalla (`VentanaLogin`, `VentanaRegistro`) y una ventana que las alterna (`VentanaPrincipal`)
- [x] Mostrar / ocultar contraseña (en el registro, las dos)
- [x] Enter en la contraseña equivale a hacer clic en el botón
- [x] Validación de formularios con mensajes claros (un error por vez)
- [x] Servicio de autenticación simulado, compartido por las dos pantallas
- [x] Contraseñas con hash PBKDF2-SHA256 y sal; nunca en texto plano
- [x] Mensaje genérico ante un login fallido (no revela si el usuario existe)
- [x] Estilos en `estilos.qss` con paleta naranja

## Paleta de colores

| Uso                          | Color     |
|------------------------------|-----------|
| Botón principal              | `#EA580C` |
| Botón principal · hover      | `#C2410C` |
| Botón principal · pressed    | `#9A3412` |
| Botón principal · disabled   | `#FDBA74` |
| Fondo de la ventana          | `#FFF7ED` |
| Tarjeta                      | `#FFFFFF` |
| Texto principal / secundario | `#1C1917` / `#57534E` |
| Bordes                       | `#E7E5E4` (foco: `#EA580C`) |
| Error / Éxito                | `#B91C1C` / `#15803D` |

El botón principal usa exactamente el estilo pedido (`#EA580C`, hover `#C2410C`,
pressed `#9A3412`, radio 8px, padding 12px, texto blanco en negrita). Se aplica
a `btn_login` y `btn_registrar`, que siguen la convención de nombres de la guía.

## Estructura

    main.py                    arranca la app y carga los estilos
    ventanas/
      login.ui                 diseño del login
      registro.ui              diseño del registro
      estilos.qss              apariencia de toda la app
      ventana_login.py         VentanaLogin
      ventana_registro.py      VentanaRegistro
      ventana_principal.py     VentanaPrincipal (QStackedWidget)
    controladores/
      autenticacion.py         ServicioAutenticacion (no importa PyQt6)
    capturas/                  imágenes para el README

## Decisiones de diseño
- El `.ui` describe, Python decide; lo único que comparten es el `objectName`.
- Los estilos viven en un solo archivo `.qss`. Python solo indica el *tipo* de
  mensaje (`info`, `error`, `exito`) con una propiedad y el QSS decide el color.
- `VentanaPrincipal` es quien conoce las dos pantallas y crea el único servicio
  que comparten. Ninguna pantalla sabe que la otra existe.
- Error y éxito se distinguen por el texto, no solo por el color.

## Limitaciones conocidas
- Los usuarios no persisten al cerrar la app.
- No hay límite de intentos de login, sesiones ni recuperación de contraseña.
- Al llegar MySQL, solo debería cambiar el interior de `ServicioAutenticacion`.

## Autores
(Juan Esteban Vallini)
