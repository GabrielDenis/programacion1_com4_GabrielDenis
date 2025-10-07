# Practico 2 - Funciones en Python
import math

# Ejercicio 1
# Crear una funcion que imprima Hola Mundo
def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

# Ejercicio 2
# Crear una funcion que reciba un nombre y devuelva un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# Ejercicio 3
# Crear una funcion que reciba nombre apellido edad y residencia y los muestre formateados
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4
# Crear dos funciones para calcular el area y el perimetro de un circulo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo: "))
print(f"Area: {calcular_area_circulo(radio):.2f}")
print(f"Perimetro: {calcular_perimetro_circulo(radio):.2f}")

# Ejercicio 5
# Crear una funcion que convierta segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas")

# Ejercicio 6
# Crear una funcion que imprima la tabla de multiplicar del numero recibido
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

# Ejercicio 7
# Crear una funcion que devuelva una tupla con suma resta multiplicacion y division
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")

# Ejercicio 8
# Crear una funcion que calcule el indice de masa corporal
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

# Ejercicio 9
# Crear una funcion que convierta grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Ingrese la temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

# Ejercicio 10
# Crear una funcion que calcule el promedio de tres numeros
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
