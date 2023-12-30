import random

def juego_adivina_numero():
    numero_secreto = random.randint(1, 10)
    vidas = 5
    
    print("¡Bienvenido al juego Adivina el Número!")
    print("Tienes que adivinar un número entre 1 y 10.")
    
    while vidas > 0:
        print(f"Tienes {vidas} vidas.")
        intento = int(input("Ingresa tu número: "))
        
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print("¡Felicidades! ¡Has adivinado el número!")
            return
        
        vidas -= 1
    
    print(f"¡Has perdido! El número secreto era {numero_secreto}.")

# Juego inicial
juego_adivina_numero()

while True:
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente != "s":
        break
    juego_adivina_numero()
