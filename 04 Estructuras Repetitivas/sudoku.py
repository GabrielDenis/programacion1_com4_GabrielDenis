import random

matriz = [[0 for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range(4):
        matriz[i][j] = random.randint(1,4)

for fila in matriz:
    print(fila)

for i in range(4):
    if len(matriz[i]) == len(set(matriz[i])):
        print(f"La linea {i+1} es valida")
    else:
        print(f"La linea {i+1} no es valida")

for j in range(4):
    columna = [matriz[i][j] for i in range(4)]
    if len(columna) == len(set(columna)):
        print(f"La columna {j+1} es valida")
    else:
        print(f"La columna {j+1} no es valida")