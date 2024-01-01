import random
import time

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza

    def atacar(self, enemigo):
        pass

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=100, ataque=10, defensa=8, inteligencia=5, agilidad=6, fuerza=12)

    def atacar(self, enemigo):
        danio = self.ataque + self.fuerza - enemigo.defensa
        print(f"{self.nombre} ataca a {enemigo.nombre} y le causa {danio} de daño.")
        enemigo.vida -= danio

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=12, defensa=5, inteligencia=15, agilidad=7, fuerza=5)

    def atacar(self, enemigo):
        danio = self.ataque + self.inteligencia - enemigo.defensa
        print(f"{self.nombre} lanza un hechizo a {enemigo.nombre} y le causa {danio} de daño.")
        enemigo.vida -= danio

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=11, defensa=6, inteligencia=8, agilidad=15, fuerza=7)

    def atacar(self, enemigo):
        danio = self.ataque + self.agilidad - enemigo.defensa
        print(f"{self.nombre} dispara a {enemigo.nombre} y le causa {danio} de daño.")
        enemigo.vida -= danio

class Asesino(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=85, ataque=13, defensa=7, inteligencia=10, agilidad=14, fuerza=8)

    def atacar(self, enemigo):
        danio = self.ataque + (self.agilidad + self.inteligencia) // 2 - enemigo.defensa
        print(f"{self.nombre} ejecuta un ataque sigiloso a {enemigo.nombre} y le causa {danio} de daño.")
        enemigo.vida -= danio

class Enemigo(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)

# Función para manejar la lógica de la batalla
def batalla(jugador, enemigo):
    while jugador.vida > 0 and enemigo.vida > 0:
        if jugador.agilidad >= enemigo.agilidad:
            jugador.atacar(enemigo)
            if enemigo.vida > 0:
                enemigo.atacar(jugador)
        else:
            enemigo.atacar(jugador)
            if jugador.vida > 0:
                jugador.atacar(enemigo)
        time.sleep(1)

        print(f"{jugador.nombre}: Vida: {jugador.vida}")
        print(f"{enemigo.nombre}: Vida: {enemigo.vida}\n")

# Función para iniciar el juego
def iniciar_juego():
    print("¡Bienvenido al juego RPG!\n")
    print("Elige tu clase:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    print("4. Asesino")

    eleccion = input("Elige una opción (1-4): ")
    nombre_jugador = input("Ingresa tu nombre: ")

    clases = {
        '1': Guerrero,
        '2': Mago,
        '3': Arquero,
        '4': Asesino
    }

    jugador = clases.get(eleccion, Guerrero)(nombre_jugador)
    enemigo = Enemigo("Enemigo", vida=50, ataque=8, defensa=5, inteligencia=6, agilidad=8, fuerza=7)

    print(f"\nComienza la batalla entre {jugador.nombre} y {enemigo.nombre}!\n")
    batalla(jugador, enemigo)

    if jugador.vida <= 0:
        print("Has sido derrotado. ¡Game Over!")
    else:
        print(f"Felicidades, has derrotado a {enemigo.nombre}. ¡Has ganado!")

# Iniciar el juego
if __name__ == "__main__":
    iniciar_juego()
