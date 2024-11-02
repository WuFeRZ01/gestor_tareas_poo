class Usuario:
    def __init__(self, nombre_usuario, contrasena, correo):
        """Inicializa el usuario con nombre, contraseña y correo."""
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo = correo

    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña ingresada coincide con la registrada."""
        return self.contrasena == contrasena


class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite, prioridad):
        """Inicializa una tarea con su información básica."""
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.completada = False

    def editar_tarea(self, titulo, descripcion, fecha_limite, prioridad):
        """Permite editar los atributos de una tarea."""
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad


class Categoria:
    def __init__(self, nombre, descripcion):
        """Inicializa una categoría con nombre y descripción."""
        self.nombre = nombre
        self.descripcion = descripcion
        self.tareas = []

    def agregar_tarea(self, tarea):
        """Agrega una tarea a la categoría."""
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        """Elimina una tarea de la categoría."""
        self.tareas.remove(tarea)


class GestorTareas:
    def __init__(self):
        """Inicializa el gestor con usuarios y tareas vacías."""
        self.usuarios = {}
        self.categorias = {}

    def registrar_usuario(self, nombre_usuario, contrasena, correo):
        """Registra un nuevo usuario."""
        if nombre_usuario in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena, correo)
            print(f"Usuario {nombre_usuario} registrado exitosamente.")

    def iniciar_sesion(self, nombre_usuario, contrasena):
        """Inicia sesión para un usuario registrado."""
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.verificar_contrasena(contrasena):
            print(f"Bienvenido, {nombre_usuario}.")
            return usuario
        else:
            print("Usuario o contraseña incorrectos.")
            return None

    def cambiar_contrasena(self, nombre_usuario, correo, nueva_contrasena):
        """Cambia la contraseña de un usuario si el correo es correcto."""
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.correo == correo:
            usuario.contrasena = nueva_contrasena
            print("Contraseña cambiada exitosamente.")
        else:
            print("Correo incorrecto.")

    def crear_categoria(self, nombre, descripcion):
        """Crea una nueva categoría."""
        if nombre in self.categorias:
            print("La categoría ya existe.")
        else:
            self.categorias[nombre] = Categoria(nombre, descripcion)
            print(f"Categoría '{nombre}' creada.")

    def generar_informe(self):
        """Genera un informe en consola con las tareas agrupadas por categoría."""
        print("\n=== Informe de Tareas por Categoría ===")
        for nombre, categoria in self.categorias.items():
            print(f"\nCategoría: {nombre}")
            for tarea in categoria.tareas:
                estado = "Completada" if tarea.completada else "Pendiente"
                print(f"  - {tarea.titulo} ({estado})")

