import random

matriz = [[0 for _ in range(5)] for _ in range(5)]

numeros = random.sample(range(1,51),25)

for n in range(5):
    for m in range(5):
        matriz[n][m] = numeros.pop()

print("Matriz inicial.")
for n in range(5):
    print(matriz[n])

numeros_bingo = random.sample(range(1,51),50)

contador = 25

while contador != 0:
    numero_sorteo = numeros_bingo.pop()
    print(f"Se sortea el: {numero_sorteo}")
    for n in range(5):
        if numero_sorteo in matriz[n]:
            indice = matriz[n].index(numero_sorteo)
            matriz[n][indice] = 0
            contador -= 1
    print("Matriz actual")
    for n in range(5):
        print(matriz[n])