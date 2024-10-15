from gestordetareas.view.console import UIConsola
from gestordetareas.view.console import Gestortareas
if __name__ == "_main_":
    Gestortareas = Gestortareas()
    consola = UIConsola(Gestortareas)
    consola.ejecutar_app()