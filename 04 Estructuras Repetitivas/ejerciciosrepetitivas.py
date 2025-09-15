import random

######################## EJERCICIO 1 ##########################

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

print("=== Encriptador de Mensajes ===")
for i in range(1, 6):
    mensaje_encriptado = ""
    mensaje = input(f"Ingrese el mensaje {i}: ").lower()
    desplazamiento = int(input("Ingrese el desplazamiento: "))

    for letra in mensaje:
        if letra in alfabeto:
            posicion = alfabeto.index(letra)
            nueva_posicion = (posicion + desplazamiento) % len(alfabeto)
            mensaje_encriptado += alfabeto[nueva_posicion]
        else:
            mensaje_encriptado += letra

    print(f"Mensaje {i} encriptado: {mensaje_encriptado}\n")

######################## EJERCICIO 2 ##########################

opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

jugador = 0
maquina = 0

print("=== Juego: Piedra, Papel o Tijera ===")

while True:
    opcion = int(input("Elige: 1 (Piedra), 2 (Papel), 3 (Tijera): "))
    if opcion not in opciones:
        continue

    bot = random.randint(1, 3)

    print(f"Jugador eligió: {opciones[opcion]}")
    print(f"Bot eligió: {opciones[bot]}")

    if (opcion == 1 and bot == 3) or (opcion == 2 and bot == 1) or (opcion == 3 and bot == 2):
        jugador += 1
    elif opcion != bot:
        maquina += 1

    print(f"Puntaje -> Jugador: {jugador} | Bot: {maquina}\n")

    salir = int(input("Presione 4 para salir o cualquier otro número para continuar: "))
    if salir == 4:
        break
