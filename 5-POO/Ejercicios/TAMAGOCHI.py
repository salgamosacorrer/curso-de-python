class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de energía: {self.nivel_energia}")
        print(f"Nivel de hambre: {self.nivel_hambre}")
        print(f"Estado de humor: {self.humor}")
        if not self.esta_vivo:
            print("¡Tu Tamagotchi ha muerto!")

    def alimentar(self):
        self.nivel_hambre -= 10
        if self.nivel_hambre < 0:
            self.nivel_hambre = 0
        self.nivel_energia -= 15
        self.verificar_estado()
        self.actualizar_humor()
    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10
        self.verificar_estado()
        self.actualizar_humor()
    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5
        self.verificar_estado()
        self.actualizar_humor()
    def verificar_estado(self):
        if self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
            #self.actualizar_humor()
        if self.nivel_energia <= 0:
            self.esta_vivo = False
            
    def actualizar_humor(self):
        # Método para actualizar el estado de ánimo (humor) del Tamagotchi según su nivel de felicidad.
        if self.nivel_felicidad >= 80:
            self.humor = "eufórico"
        elif 50 <= self.nivel_felicidad < 80:
            self.humor = "feliz"
        elif 20 <= self.nivel_felicidad < 50:
            self.humor = "indiferente"
        elif 10 <= self.nivel_felicidad < 20:
            self.humor = "triste"
        else:
            self.humor = "enojado"
        

def menu():
    print("\nAcciones disponibles:")
    print("1. Mostrar estado")
    print("2. Alimentar")
    print("3. Jugar")
    print("4. Dormir")
    print("5. Salir")

# Crear una mascota
nombre_mascota = input("Ingresa el nombre de tu Tamagotchi: ")
mi_mascota = Tamagotchi(nombre_mascota)

opcion = 0
while opcion != 5:  # 5 es la opción para salir del programa
    menu()
    opcion = int(input("Elige una acción (1-5): "))

    if opcion == 1:
        mi_mascota.mostrar_estado()
    elif opcion == 2:
        mi_mascota.alimentar()
    elif opcion == 3:
        mi_mascota.jugar()
    elif opcion == 4:
        mi_mascota.dormir()
    elif opcion == 5:
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")
