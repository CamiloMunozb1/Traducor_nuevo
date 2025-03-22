from googletrans import Translator  # Importa la clase Translator de googletrans para realizar traducciones

class TraduccionNueva:
    try:
        def __init__(self):
            """
            Inicializa el diccionario de opciones del traductor.
            Cada opción está vinculada a un método correspondiente.
            """
            self.opciones = {
                "1": self.opcion_uno,  # Opción para ingresar una traducción
                "2": self.opcion_dos   # Opción para mostrar los idiomas disponibles
            }

        def mostrar_opciones(self):
            """
            Muestra el menú de opciones disponibles para el usuario.
            """
            print("""
                    1. Ingresar traducción.
                    2. Elegir idioma.
                """)

        def ejecutar_opciones(self):
            """
            Solicita al usuario que seleccione una opción del menú.
            Si la opción es válida, ejecuta la acción correspondiente.
            """
            while True:
                self.mostrar_opciones()
                usuario = str(input("Ingresa una opción: "))
                accion = self.opciones.get(usuario)  # Obtiene la función correspondiente a la opción ingresada
                if accion:
                    accion()  # Ejecuta la opción seleccionada
                    break
                else:
                    print("Ingresa un valor correcto entre 1-2")

        def traduccion_nueva(self):
            """
            Solicita al usuario una frase y el idioma de destino para traducir.
            Luego, usa Google Translate para obtener la traducción y la muestra en pantalla.
            """
            try:
                traduccion_new = input("Ingresa la frase o palabra a traducir: ")
                idioma_traduccion = input("Ingresa el idioma a traducir (ejemplo: 'es' para español, 'en' para inglés): ")
                traduccion = Translator()  # Crea una instancia del traductor
                resultado = traduccion.translate(traduccion_new, dest=idioma_traduccion)  # Traduce la frase
                print(f"Traducción: {resultado.text}")  # Muestra la traducción en pantalla
            except Exception as error:
                print(f"Error en el programa: {error}.")

        def mostrar_idiomas(self):
            """
            Muestra una lista de idiomas disponibles para la traducción.
            """
            idiomas_traduccion = {
                "es": "Español", "en": "Inglés", "fr": "Francés", "de": "Alemán",
                "it": "Italiano", "pt": "Portugués", "ru": "Ruso", "zh-cn": "Chino simplificado",
                "ja": "Japonés", "ko": "Coreano", "ar": "Árabe", "hi": "Hindi",
                "nl": "Neerlandés", "sv": "Sueco", "pl": "Polaco", "tr": "Turco",
                "fi": "Finés", "el": "Griego", "he": "Hebreo", "th": "Tailandés"
            }
            print("Idiomas disponibles:")
            for clave, valor in idiomas_traduccion.items():
                print(f"{clave}: {valor}")

        def opcion_uno(self):
            """
            Método que se ejecuta cuando el usuario selecciona la opción 1 (traducción).
            """
            self.traduccion_nueva()

        def opcion_dos(self):
            """
            Método que se ejecuta cuando el usuario selecciona la opción 2 (mostrar idiomas).
            """
            self.mostrar_idiomas()
    except Exception as error:
        print(f"Error en el programa: {error}.")

# Punto de entrada principal del programa
if __name__ == "__main__":
    traduccion = TraduccionNueva()  # Crea una instancia de la clase
    traduccion.ejecutar_opciones()  # Ejecuta el menú de opciones