import json

class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []

    def mostrar_libros_disponibles(self):
        print(f'Libros disponibles en la biblioteca {self.nombre}:')
        for libro in self.libros_disponibles:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Año de Publicación: {libro.año_publicacion}, Disponible: {libro.disponible}, Unidades: {libro.unidades}")

    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f"Libro '{titulo}' prestado exitosamente.")
                return
        print(f"El libro '{titulo}' no está disponible para préstamo.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f"Libro '{titulo}' devuelto exitosamente.")
                return
        print(f"El libro '{titulo}' no se puede recibir, o no está en la biblioteca.")

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                print(f"Libro '{titulo}' eliminado de la biblioteca.")
                return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

    def guardar_biblioteca(self, nombre_archivo):
        libros = []
        for libro in self.libros_disponibles:
            libros.append(vars(libro))
        with open(nombre_archivo, 'w') as archivo:
            json.dump(libros, archivo, indent=4)
        print(f"Biblioteca '{self.nombre}' guardada en el archivo '{nombre_archivo}'.")

    @staticmethod
    def cargar_biblioteca(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            data = json.load(archivo)
        biblioteca = Biblioteca("Nueva Biblioteca")
        for libro_data in data:
            libro = Libro(**libro_data)
            biblioteca.agregar_libro(libro)
        return biblioteca

# Crear libros y bibliotecas de ejemplo
libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, 5)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 3)

biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)

biblioteca1.prestar_libro("El señor de los anillos")
biblioteca1.mostrar_libros_disponibles()

biblioteca1.guardar_biblioteca("biblioteca.json")

biblioteca2 = Biblioteca.cargar_biblioteca("biblioteca.json")
biblioteca2.mostrar_libros_disponibles()
