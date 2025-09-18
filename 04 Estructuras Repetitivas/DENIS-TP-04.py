# 1) Imprimir enteros de 0 a 100
for i in range(101):
    print(i)

# 2) Cantidad de digitos de un numero
num = int(input("Ingrese un numero entero: "))
print("Cantidad de digitos:", len(str(abs(num))))

# 3) Suma de numeros entre dos valores excluyendolos
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("La suma es:", suma)

# 4) Sumar numeros hasta que el usuario ponga 0
total = 0
while True:
    n = int(input("Ingrese un numero (0 para salir): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)

# 5) Juego de adivinar numero
import random
secreto = random.randint(0, 9)
intentos = 0
acierto = False
while not acierto:
    n = int(input("Adivine el numero (0-9): "))
    intentos += 1
    if n == secreto:
        acierto = True
print(f"Adivinaste en {intentos} intentos")

# 6) Numeros pares de 0 a 100 en orden decreciente
for i in range(100, -1, -2):
    print(i)

# 7) Suma desde 0 hasta un numero dado
n = int(input("Ingrese un numero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma es:", suma)

# 8) Contar pares, impares, positivos y negativos en 100 numeros
cantidad = 5  # cambiar este numero para probar con menos
pares = impares = positivos = negativos = 0
for i in range(cantidad):
    n = int(input("Ingrese un numero: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Media de 100 numeros
cantidad = 5  # cambiar este numero para probar con menos
suma = 0
for i in range(cantidad):
    n = int(input("Ingrese un numero: "))
    suma += n
print("Media:", suma / cantidad)

# 10) Invertir los digitos de un numero
num = input("Ingrese un numero: ")
print("Invertido:", num[::-1])
