class Usuario:
    def _init_(self, nombre_usuario, contrasena, correo):
        """Inicializa el usuario con nombre de usuario, contraseña y correo."""
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo = correo

    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña ingresada coincide con la actual."""
        return self.contrasena == contrasena

class SistemaAutenticacion:
    def _init_(self):
        """Inicializa el sistema de autenticación con un diccionario de usuarios."""
        self.usuarios = {}

    def registrar_usuario(self, nombre_usuario, contrasena, correo):
        """Registra un nuevo usuario en el sistema."""
        if nombre_usuario in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena, correo)
            print(f"Usuario {nombre_usuario} registrado exitosamente.")

    def iniciar_sesion(self, nombre_usuario, contrasena):
        """Permite al usuario iniciar sesión si la contraseña es correcta."""
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.verificar_contrasena(contrasena):
            print(f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def cambiar_contrasena(self, nombre_usuario, correo, nueva_contrasena):
        """Permite cambiar la contraseña si el correo coincide."""
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.correo == correo:
            usuario.contrasena = nueva_contrasena
            print("Contraseña cambiada exitosamente.")
        else:
            print("Correo incorrecto.")


class Tarea:
    pass

class Categoria:
    pass

class Informe:
    pass

import sys

class UIConsola:

    def _init_(self, sistema_autenticacion):
        self.sistema_autenticacion = sistema_autenticacion
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
        self.sistema_autenticacion.registrar_usuario(nombre, contrasena, correo)

    def cambiar_contraseña(self):
        nombre = input("Nombre de usuario: ")
        correo = input("Correo electrónico: ")
        nueva_contrasena = input("Nueva contraseña: ")
        self.sistema_autenticacion.cambiar_contrasena(nombre, correo, nueva_contrasena)

    def iniciar_sesion(self):
        nombre = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        self.sistema_autenticacion.iniciar_sesion(nombre, contrasena)

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
        

if _name_ == "_main_":
    sistema_autenticacion = SistemaAutenticacion()
    consola = UIConsola(sistema_autenticacion)
    consola.ejecutar_app()