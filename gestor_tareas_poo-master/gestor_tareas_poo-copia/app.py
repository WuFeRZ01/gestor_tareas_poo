from gestordetareas.model.gestordetareas import GestorTareas  # Importa correctamente el gestor
from gestordetareas.view.console import UIConsola  # Importa la UI de consola

if __name__ == "__main__":
    gestor = GestorTareas()  # Crea una instancia del gestor
    consola = UIConsola(gestor)  # Pasa el gestor a la consola
    consola.ejecutar_app()  # Inicia la aplicación
