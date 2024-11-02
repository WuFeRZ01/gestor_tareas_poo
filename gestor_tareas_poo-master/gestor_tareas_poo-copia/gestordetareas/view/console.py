import sys
from gestordetareas.model.gestordetareas import GestorTareas, Tarea, Categoria

class UIConsola:
    def __init__(self, gestor_tareas):
        """Inicializa la interfaz de consola."""
        self.gestor_tareas = gestor_tareas
        self.opciones = {
            "1": self.crear_cuenta,
            "2": self.cambiar_contraseña,
            "3": self.iniciar_sesion,
            "4": self.crear_tarea,
            "5": self.editar_tarea,
            "6": self.crear_categoria,
            "7": self.agrupar_tareas_por_categoria,
            "8": self.eliminar_tarea,
            "9": self.generar_informe,
            "0": self.salir
        }

    def mostrar_menu(self):
        """Muestra el menú principal."""
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear cuenta")
        print("2. Cambiar contraseña")
        print("3. Iniciar sesión")
        print("4. Crear tarea")
        print("5. Editar tarea")
        print("6. Crear categoría de tareas")
        print("7. Agrupar tareas por categorías")
        print("8. Eliminar tarea")
        print("9. Generar informe")
        print("0. Salir")

    def ejecutar_app(self):
        """Ejecuta la aplicación y muestra el menú en un bucle."""
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción: ").strip()  # Limpiamos espacios en blanco
            if opcion.isdigit() and opcion in self.opciones:
                accion = self.opciones[opcion]
                try:
                    accion()
                except Exception as e:
                    print(f"Ocurrió un error: {e}")
            else:
                print("Opción no válida, intenta de nuevo.")

    def crear_cuenta(self):
        """Permite crear una nueva cuenta de usuario."""
        nombre = input("Nombre de usuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        correo = input("Correo electrónico: ").strip()
        self.gestor_tareas.registrar_usuario(nombre, contrasena, correo)

    def cambiar_contraseña(self):
        """Permite cambiar la contraseña de un usuario."""
        nombre = input("Nombre de usuario: ").strip()
        correo = input("Correo electrónico: ").strip()
        nueva_contrasena = input("Nueva contraseña: ").strip()
        self.gestor_tareas.cambiar_contrasena(nombre, correo, nueva_contrasena)

    def iniciar_sesion(self):
        """Permite al usuario iniciar sesión."""
        nombre = input("Nombre de usuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        self.gestor_tareas.iniciar_sesion(nombre, contrasena)

    def crear_tarea(self):
        """Permite crear una nueva tarea."""
        if not self.gestor_tareas.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
        titulo = input("Título de la tarea: ").strip()
        descripcion = input("Descripción: ").strip()
        fecha_limite = input("Fecha límite (YYYY-MM-DD): ").strip()
        prioridad = input("Prioridad (Alta, Media, Baja): ").strip()
        self.gestor_tareas.crear_tarea(titulo, descripcion, fecha_limite, prioridad)

    def editar_tarea(self):
        """Permite editar una tarea existente."""
        if not self.gestor_tareas.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
        titulo = input("Título de la tarea a editar: ").strip()
        nueva_descripcion = input("Nueva descripción: ").strip()
        nueva_fecha = input("Nueva fecha límite (YYYY-MM-DD): ").strip()
        nueva_prioridad = input("Nueva prioridad (Alta, Media, Baja): ").strip()
        self.gestor_tareas.editar_tarea(titulo, nueva_descripcion, nueva_fecha, nueva_prioridad)

    def crear_categoria(self):
        """Permite crear una nueva categoría de tareas."""
        if not self.gestor_tareas.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
        nombre = input("Nombre de la categoría: ").strip()
        descripcion = input("Descripción: ").strip()
        self.gestor_tareas.crear_categoria(nombre, descripcion)

    def agrupar_tareas_por_categoria(self):
        """Agrupa las tareas por categoría."""
        if not self.gestor_tareas.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
        self.gestor_tareas.mostrar_tareas_por_categoria()

    def eliminar_tarea(self):
        """Permite eliminar una tarea existente."""
        if not self.gestor_tareas.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
        titulo = input("Título de la tarea a eliminar: ").strip()
        self.gestor_tareas.eliminar_tarea(titulo)

    def generar_informe(self):
        """Genera un informe de las tareas del usuario actual."""
        if not self.gestor_tareas.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
        self.gestor_tareas.generar_informe()

    @staticmethod
    def salir():
        """Cierra la aplicación."""
        print("Saliendo de la aplicación. ¡Hasta luego!")
        sys.exit(0)

