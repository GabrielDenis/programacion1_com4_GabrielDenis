# Practico 6 - Estructuras de datos complejas

# Ejercicio 1
# Agregar nuevas frutas al diccionario
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Ejercicio 1 - Diccionario actualizado")
print(precios_frutas)

# Ejercicio 2
# Actualizar precios de algunas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print("\nEjercicio 2 - Diccionario con precios actualizados")
print(precios_frutas)

# Ejercicio 3
# Crear una lista solo con los nombres de las frutas
frutas = list(precios_frutas.keys())

print("\nEjercicio 3 - Lista de frutas")
print(frutas)

# Ejercicio 4
# Programa para almacenar y consultar numeros telefonicos
agenda = {}

for i in range(5):
  nombre = input("Ingrese el nombre del contacto: ")
  numero = input("Ingrese el numero de telefono: ")
  agenda[nombre] = numero

consulta = input("Ingrese el nombre a consultar: ")
if consulta in agenda:
  print(f"El numero de {consulta} es {agenda[consulta]}")
else:
  print("El nombre no existe en la agenda")

# Ejercicio 5
# Mostrar palabras unicas y cantidad de apariciones
frase = input("Ingrese una frase: ").lower().split()
palabras_unicas = set(frase)

# Crear un diccionario con cantidad de apariciones
frecuencia = {}
for palabra in frase:
  if palabra in frecuencia:
    frecuencia[palabra] += 1
  else:
    frecuencia[palabra] = 1

print("\nEjercicio 5 - Palabras unicas")
print(palabras_unicas)
print("Frecuencia de palabras")
print(frecuencia)

# Ejercicio 6
# Cargar nombres de alumnos y sus notas, luego mostrar promedio
alumnos = {}

for i in range(3):
  nombre = input("Ingrese el nombre del alumno: ")
  notas = tuple(float(input(f"Ingrese nota {j+1}: ")) for j in range(3))
  alumnos[nombre] = notas

print("\nEjercicio 6 - Promedios")
for nombre, notas in alumnos.items():
  promedio = sum(notas) / len(notas)
  print(f"{nombre}: promedio {promedio:.2f}")

# Ejercicio 7
# Sets con aprobados de Parcial 1 y Parcial 2
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

print("\nEjercicio 7")
print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# Ejercicio 8
# Diccionario con productos y stock
stock = {'Pan': 20, 'Leche': 10, 'Queso': 5}

producto = input("Ingrese un producto: ")

if producto in stock:
  print(f"Stock actual de {producto}: {stock[producto]}")
  agregar = int(input("Ingrese cantidad a agregar: "))
  stock[producto] += agregar
else:
  nuevo_stock = int(input("Producto no existe, ingrese cantidad inicial: "))
  stock[producto] = nuevo_stock

print("\nEjercicio 8 - Stock actualizado")
print(stock)

# Ejercicio 9
# Agenda de eventos con clave como tupla (dia, hora)
agenda_eventos = {
  ('Lunes', '10:00'): 'Reunion',
  ('Martes', '14:00'): 'Clase de programacion',
  ('Viernes', '18:00'): 'Gimnasio'
}

dia = input("Ingrese un dia: ")
hora = input("Ingrese una hora (hh:mm): ")

if (dia, hora) in agenda_eventos:
  print(f"Evento: {agenda_eventos[(dia, hora)]}")
else:
  print("No hay evento programado")

# Ejercicio 10
# Invertir un diccionario de paises y capitales
paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo'}
invertido = {capital: pais for pais, capital in paises.items()}

print("\nEjercicio 10 - Diccionario invertido")
print(invertido)
