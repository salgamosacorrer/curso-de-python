import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    maquina = random.choice(opciones)
    
    print("¡Bienvenido al juego Piedra, Papel o Tijeras!")
    print("Las opciones son: piedra, papel o tijeras.")
    jugador = input("Ingrese su jugada: ").lower()
    
    if jugador not in opciones:
        print("Jugada no válida. Por favor, ingrese piedra, papel o tijeras.")
        return
    
    print(f"La máquina eligió: {maquina}")
    
    if jugador == maquina:
        print("Empate.")
    elif (jugador == "piedra" and maquina == "tijeras") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijeras" and maquina == "papel"):
        print("¡Ganaste!")
    else:
        print("¡La máquina gana!")
    
# Juego inicial
jugar_piedra_papel_tijeras()

while True:
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente != "s":
        break
    jugar_piedra_papel_tijeras()
