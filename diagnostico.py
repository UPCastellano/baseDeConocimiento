from experta import *
from datetime import datetime

class DiagnosticoComputadora(KnowledgeEngine):
    # Metadata del sistema
    __author__ = "Ing. Uriel Castellanos"
    __version__ = "2.0"
    __copyright__ = f"Copyright © {datetime.now().year} Ing. Uriel Castellanos. Todos los derechos reservados."

    def __init__(self):
        super().__init__()
        self.diagnostico_resultado = ""

    @Rule(Fact(problema="pantalla_negra"))
    def problema_pantalla(self):
        self.diagnostico_resultado = {
            "titulo": "Problema con la Pantalla",
            "sugerencias": [
                "Revisa si el cable del monitor está conectado correctamente",
                "Verifica que el monitor esté encendido",
                "Comprueba si la tarjeta gráfica está bien instalada",
                "Intenta conectar el monitor a otro puerto de video"
            ],
            "gravedad": "Media",
            "icono": "🖥️"
        }

    @Rule(Fact(problema="sin_conexion_internet"))
    def problema_internet(self):
        self.diagnostico_resultado = {
            "titulo": "Problema de Conexión a Internet",
            "sugerencias": [
                "Verifica si el módem está encendido y conectado",
                "Reinicia el módem y router",
                "Comprueba si otros dispositivos tienen conexión",
                "Revisa si el cable de red está bien conectado"
            ],
            "gravedad": "Alta",
            "icono": "🌐"
        }

    @Rule(Fact(problema="teclado_no_funciona"))
    def problema_teclado(self):
        self.diagnostico_resultado = {
            "titulo": "Problema con el Teclado",
            "sugerencias": [
                "Revisa si el teclado está bien conectado",
                "Prueba con otro puerto USB",
                "Verifica si los drivers están actualizados",
                "Intenta con otro teclado si es posible"
            ],
            "gravedad": "Baja",
            "icono": "⌨️"
        }

    @Rule(Fact(problema="audio_no_funciona"))
    def problema_audio(self):
        self.diagnostico_resultado = {
            "titulo": "Problema de Audio",
            "sugerencias": [
                "Verifica si los altavoces están encendidos",
                "Comprueba si el volumen está silenciado",
                "Revisa la configuración de audio del sistema",
                "Actualiza los drivers de audio"
            ],
            "gravedad": "Baja",
            "icono": "🔊"
        }

