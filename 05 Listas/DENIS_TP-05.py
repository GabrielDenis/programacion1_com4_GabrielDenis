#Práctico 5: Listas

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
lista_multiplos = list(range(4, 101, 4))
print("Lista de múltiplos de 4:", lista_multiplos)

# 2) Crear una lista con cinco elementos y mostrar el penúltimo.
lista_favoritos = ["pizza", 3, [1,2,3], "fútbol", True]
print("Penúltimo elemento:", lista_favoritos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista.
lista_vacia = []
lista_vacia.append("python")
lista_vacia.append("es")
lista_vacia.append("tremendo")
print("Lista después de los append:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales”.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista de animales modificada:", animales)

# 5) Analizar el siguiente programa.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print("Lista resultante:", numeros)

# Explicación:
print("Explicación:")
print("Primero se crea una lista con los números 8, 15, 3, 22 y 7.")
print("La función max(numeros) obtiene el valor más grande de la lista, que es 22.")
print("El método remove elimina ese valor máximo de la lista.")
print("Se imprime la lista sin el número 22, [8, 15, 3, 7].")

# 6) Crear una lista con números del 10 al 30 de 5 en 5 y mostrar los dos primeros.
lista_saltos = list(range(10, 31, 5))
print("Lista con saltos de 5:", lista_saltos)
print("Dos primeros elementos:", lista_saltos[0], lista_saltos[1])

# 7) Reemplazar los valores centrales de la lista “autos”.
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupé"]
print("Lista de autos modificada:", autos)

# 8) Crear lista vacía “dobles” y agregar el doble de 5, 10 y 15.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

# 9) Trabajar con lista anidada “compras”.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Lista de compras modificada:", compras)

# 10) Crear una lista anidada con los elementos dados.
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Ejercicio Lista anidada:", lista_anidada)
