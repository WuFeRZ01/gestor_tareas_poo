import sys
from gestordetareas.model.gestordetareas import Gestortareas

class UIConsola:

    def _init_(self, gestortareas):
        self.gestortareas = gestortareas
        # Opciones del menú
        self.opciones = {
            "1": self.crear_cuenta,
            "2": self.cambiar_contraseña,
            "3": self.iniciar_sesion,
            "4": self.crear_tarea,
            "5": self.editar_tarea,
            "6": self.crear_categoria,
            "7": self.agrupar_tareas_por_categoria,
            "8": self.eliminar_tarea,
            "9": self.generar_informe_pdf,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear cuenta")
        print("2. Cambiar contraseña")
        print("3. Iniciar sesión")
        print("4. Crear tarea")
        print("5. Editar tarea")
        print("6. Crear categoría de tareas")
        print("7. Agrupar tareas por categorías")
        print("8. Eliminar tarea")
        print("9. Generar informe en PDF")
        print("0. Salir")
        
        """"se puede implementar una excepcion si se escoge algun numero que no este en el menú principal"""
        
    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("Opción no válida, intenta de nuevo.")

    def crear_cuenta(self):
        nombre = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        correo = input("Correo electrónico: ")
        self.gestortareas.registrar_usuario(nombre, contrasena, correo)

    def cambiar_contraseña(self):
        nombre = input("Nombre de usuario: ")
        correo = input("Correo electrónico: ")
        nueva_contrasena = input("Nueva contraseña: ")
        self.gestortareas.cambiar_contrasena(nombre, correo, nueva_contrasena)

    def iniciar_sesion(self):
        nombre = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        self.gestortareas.iniciar_sesion(nombre, contrasena)

    def crear_tarea(self):
        print("Funcionalidad de crear tarea no implementada.")

    def editar_tarea(self):
        print("Funcionalidad de editar tarea no implementada.")

    def crear_categoria(self):
        print("Funcionalidad de crear categoría no implementada.")

    def agrupar_tareas_por_categoria(self):
        print("Funcionalidad de agrupar tareas no implementada.")

    def eliminar_tarea(self):
        print("Funcionalidad de eliminar tarea no implementada.")

    def generar_informe_pdf(self):
        print("Funcionalidad de generar informe en PDF no implementada.")

    @staticmethod
    def salir():
        print("Saliendo de la aplicación. ¡Hasta luego!")
        sys.exit(0)
        