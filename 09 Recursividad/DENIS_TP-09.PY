# Práctico 9 - Aplicación de la Recursividad
# Tecnicatura Universitaria en Programación - Programación I

# 1) Factorial de un número
def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)

def mostrar_factoriales():
    numero = int(input("Ingrese un número: "))
    print(f"\nFactoriales del 1 al {numero}:\n")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")
    print()

# 2) Serie de Fibonacci
def fibonacci(n):
    # Caso base
    if n <= 1:
        return n
    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    limite = int(input("Ingrese hasta qué posición mostrar la serie: "))
    print(f"\nSerie de Fibonacci hasta la posición {limite}:\n")
    for i in range(limite):
        print(fibonacci(i), end=" ")
    print("\n")

# 3) Potencia recursiva
def potencia(base, exponente):
    # Caso base: cualquier número a la 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo
    return base * potencia(base, exponente - 1)

def probar_potencia():
    base = int(input("Base: "))
    exponente = int(input("Exponente: "))
    print(f"\n{base}^{exponente} = {potencia(base, exponente)}\n")

# 4) Conversión decimal a binario
def decimal_a_binario(n):
    # Caso base: cuando n es 0 o 1, devolverlo como string
    if n < 2:
        return str(n)
    # Caso recursivo
    return decimal_a_binario(n // 2) + str(n % 2)

def probar_decimal_a_binario():
    numero = int(input("Ingrese un número decimal: "))
    print(f"El número {numero} en binario es {decimal_a_binario(numero)}\n")

# 5) Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    # Caso base: si tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si el primer y último carácter son distintos, no lo es
    if palabra[0] != palabra[-1]:
        return False
    # Caso recursivo: verificar la subcadena sin los extremos
    return es_palindromo(palabra[1:-1])

def probar_palindromo():
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo.\n")
    else:
        print(f"{palabra} no es un palíndromo.\n")

# 6) Suma de dígitos
def suma_digitos(n):
    # Caso base: si es menor a 10, devolver el número
    if n < 10:
        return n
    # Caso recursivo: sumar el último dígito al resultado del resto
    return n % 10 + suma_digitos(n // 10)

def probar_suma_digitos():
    numero = int(input("Ingrese un número entero positivo: "))
    print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}\n")

# 7) Contar bloques en una pirámide
def contar_bloques(n):
    # Caso base: un solo bloque
    if n == 1:
        return 1
    # Caso recursivo: nivel actual + niveles superiores
    return n + contar_bloques(n - 1)

def probar_contar_bloques():
    nivel = int(input("Ingrese el número de bloques del nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(nivel)}\n")

# 8) Contar cuántas veces aparece un dígito dentro de un número
def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos
    if numero == 0:
        return 0
    # Contar si el último dígito coincide y sumar recursivamente
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

def probar_contar_digito():
    numero = int(input("Ingrese un número: "))
    digito = int(input("Ingrese el dígito a buscar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.\n")

# Menú principal
def menu():
    while True:
        print("=== MENÚ DE RECURSIVIDAD ===")
        print("1) Factorial")
        print("2) Fibonacci")
        print("3) Potencia")
        print("4) Decimal a binario")
        print("5) Palíndromo")
        print("6) Suma de dígitos")
        print("7) Contar bloques")
        print("8) Contar dígito")
        print("9) Salir")
        opcion = input("Opción: ")
        print()

        if opcion == "1":
            mostrar_factoriales()
        elif opcion == "2":
            mostrar_fibonacci()
        elif opcion == "3":
            probar_potencia()
        elif opcion == "4":
            probar_decimal_a_binario()
        elif opcion == "5":
            probar_palindromo()
        elif opcion == "6":
            probar_suma_digitos()
        elif opcion == "7":
            probar_contar_bloques()
        elif opcion == "8":
            probar_contar_digito()
        elif opcion == "9":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()
