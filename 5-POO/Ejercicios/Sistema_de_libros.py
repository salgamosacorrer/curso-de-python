import json

class Libro:
    def __init__(self, titulo, autor, año_de_publicacion, unidades,disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
        self.unidades = unidades
        self.disponible = True
    def mostrar_datos(self):
        
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_de_publicacion}, Unidades: {self.unidades}, Disponible: {self.disponible}")

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []

    def mostrar_libros_disponibles(self):
       
        for libro in self.libros_disponibles:
           
              libro.mostrar_datos()
    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible and libro.unidades > 0:
                libro.unidades -= 1  # Reducir una unidad al prestar
                libro.disponible = False
                print(f"Libro '{titulo}' prestado exitosamente.")
                return
        print(f"El libro '{titulo}' no está disponible para préstamo o no hay unidades disponibles.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.unidades += 1  # Aumentar una unidad al recibir
                libro.disponible = True
                print(f"Libro '{titulo}' devuelto exitosamente.")
                return
        print(f"El libro '{titulo}' no se puede recibir, o no está en la biblioteca.")
        
    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        #print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

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
            libros.append(vars(libro))#castea libro a formato diccionario
        with open(nombre_archivo, 'w') as archivo:
            json.dump(libros, archivo, indent=4)#Toma la lista libros y la escribe en el archivo JSON proporcionado. El argumento indent=4 es opcional y agrega formato al archivo JSON para que sea legible con una sangría de 4 espacios.
        print(f"Biblioteca '{self.nombre}' guardada en el archivo '{nombre_archivo}'.")


    @staticmethod
    def cargar_biblioteca(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            data = json.load(archivo)
        biblioteca = Biblioteca("Nueva Biblioteca")
        for libro_data in data:
            libro = Libro(**libro_data)#Al utilizar **libro_data, se desempaqueta este diccionario y se pasan sus elementos como argumentos de palabras clave para el constructor de la clase Libro.
            print(libro)
            biblioteca.agregar_libro(libro)
        return biblioteca
"""
@staticmethod indica que cargar_biblioteca es un método estático en la clase Biblioteca. En este caso,
este método estático es responsable de cargar una biblioteca desde un archivo JSON 
""" 
"""
Las instancias son versiones específicas u objetos concretos de una clase. Cuando defines una clase en Python, estás creando un "molde" o una plantilla que describe cómo deberían ser los objetos de esa clase. Luego, para trabajar con estos objetos, necesitas crear instancias de esa clase.
En el contexto del código que se proporcionó:

    Clase Libro:
        Se define la estructura que un libro debe tener.
        Las instancias de esta clase representarán libros individuales con sus atributos únicos como título, autor, año de publicación, etc.

    Clase Biblioteca:
        Representa una colección de libros disponibles.
        Las instancias de esta clase representarán bibliotecas específicas que tienen su propio conjunto de libros.
 Entonces, para interactuar con libros o bibliotecas, necesitas crear instancias de estas clases:
"""
# Crear libros y bibliotecas de ejemplo 

libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, 5)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 3)

biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)

#biblioteca1.prestar_libro("El señor de los anillos")
#biblioteca1.mostrar_libros_disponibles()

#biblioteca1.guardar_biblioteca("biblioteca.json")

#biblioteca2 = Biblioteca.cargar_biblioteca("biblioteca.json")
#biblioteca2.mostrar_libros_disponibles()

def menu():
    print("\nBienvenido al sistema de bibliotecas")
    print("1. Mostrar todos los libros disponibles")
    print("2. Prestar un libro")
    print("3. Recibir un libro")
    print("4. Agregar un libro a la biblioteca")
    print("5. Quitar un libro de la biblioteca")
    print("6. Guardar biblioteca en un archivo JSON")
    print("7. Cargar biblioteca desde un archivo JSON")
    print("8. Salir")



opcion = 0
while opcion != 8:  # 8 es la opción para salir del menú
    menu()
    opcion = int(input("Elige una opción (1-8): "))

    if opcion == 1:
        biblioteca1.mostrar_libros_disponibles()
    elif opcion == 2:
        titulo = input("Ingresa el título del libro a prestar: ")
        biblioteca1.prestar_libro(titulo)
    elif opcion == 3:
        titulo = input("Ingresa el título del libro a recibir: ")
        biblioteca1.recibir_libro(titulo)
    elif opcion == 4:
        titulo = input("Ingresa el título del libro: ")
        autor = input("Ingresa el autor del libro: ")
        año_de_publicacion = int(input("Ingresa el año de publicación del libro: "))
        unidades = int(input("Ingresa el número de unidades del libro: "))
        nuevo_libro = Libro(titulo, autor, año_de_publicacion, unidades)
        biblioteca1.agregar_libro(nuevo_libro)
    elif opcion == 5:
        titulo = input("Ingresa el título del libro a quitar: ")
        biblioteca1.quitar_libro(titulo)
    elif opcion == 6:
        nombre_archivo = input("Ingresa el nombre del archivo para guardar la biblioteca: ")
        biblioteca1.guardar_biblioteca(nombre_archivo)
    elif opcion == 7:
        nombre_archivo = input("Ingresa el nombre del archivo para cargar la biblioteca: ")
        biblioteca2 = Biblioteca.cargar_biblioteca(nombre_archivo)
        biblioteca2.mostrar_libros_disponibles()
    elif opcion == 8:
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 8.")
