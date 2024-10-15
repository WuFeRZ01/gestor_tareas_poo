class Usuario:
    def _init_(self, nombre_usuario, contrasena, correo):
        """Inicializa el usuario con nombre de usuario, contraseña y correo."""
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo = correo

    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña ingresada coincide con la actual."""
        return self.contrasena == contrasena

class Gestortareas:
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