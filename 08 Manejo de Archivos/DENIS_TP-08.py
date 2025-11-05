# Práctica de Programación I - Manejo de archivos de texto, listas y diccionarios

import os

FILENAME = "productos.txt"

# Crea productos.txt con 3 productos si no existe
def crear_archivo_inicial():
    if os.path.exists(FILENAME):
        return

    productos_iniciales = [
        "Lapicera,120.5,30",
        "Cuaderno,250,15",
        "Regla,75,50"
    ]

    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            for linea in productos_iniciales:
                f.write(linea + "\n")
    except OSError as e:
        print(f"Error al crear {FILENAME}: {e}")

# Lee el archivo y devuelve las líneas sin saltos de línea
def leer_archivo():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            lineas = [ln.strip() for ln in f.readlines() if ln.strip()]
        return lineas
    except FileNotFoundError:
        return []
    except OSError as e:
        print(f"Error al leer {FILENAME}: {e}")
        return []

# Convierte una línea "nombre,precio,cantidad" en un diccionario
def linea_a_dict(linea):
    partes = [p.strip() for p in linea.split(",")]
    nombre = partes[0] if len(partes) > 0 else ""

    # Conversión segura de precio y cantidad
    precio = 0.0
    cantidad = 0
    if len(partes) > 1:
        try:
            precio = float(partes[1]) if partes[1] != "" else 0.0
        except ValueError:
            precio = 0.0
    if len(partes) > 2:
        try:
            cantidad = int(float(partes[2])) if partes[2] != "" else 0
        except ValueError:
            cantidad = 0

    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

# Carga todos los productos del archivo en una lista de diccionarios
def cargar_productos_en_lista():
    lineas = leer_archivo()
    productos = [linea_a_dict(ln) for ln in lineas]
    return productos

# Muestra los productos con el formato solicitado
def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.\n")
        return

    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Agrega un producto nuevo al archivo sin borrar el contenido
def agregar_producto_al_archivo():
    print("\n--- Agregar un nuevo producto ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Nombre vacío. Operación cancelada.\n")
        return

    precio_raw = input("Precio: ").strip()
    cantidad_raw = input("Cantidad: ").strip()

    # Validación básica de datos
    try:
        precio = float(precio_raw)
    except ValueError:
        print("Precio inválido. Usando 0.0")
        precio = 0.0

    try:
        cantidad = int(float(cantidad_raw))
    except ValueError:
        print("Cantidad inválida. Usando 0")
        cantidad = 0

    linea = f"{nombre},{precio},{cantidad}"

    try:
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(linea + "\n")
        print("Producto agregado correctamente.\n")
    except OSError as e:
        print(f"Error al escribir en {FILENAME}: {e}")

# Busca un producto por nombre (sin distinguir mayúsculas)
def buscar_producto_por_nombre(productos):
    if not productos:
        print("No hay productos cargados.\n")
        return

    q = input("Nombre a buscar: ").strip().lower()
    encontrados = [p for p in productos if p["nombre"].lower() == q]

    if not encontrados:
        print("No se encontró el producto.\n")
        return

    for p in encontrados:
        print("Producto encontrado:")
        print(f"  Nombre: {p['nombre']}")
        print(f"  Precio: ${p['precio']}")
        print(f"  Cantidad: {p['cantidad']}\n")

# Sobrescribe el archivo con los productos que estén en la lista
def guardar_productos(productos):
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            for p in productos:
                linea = f"{p['nombre']},{p['precio']},{p['cantidad']}"
                f.write(linea + "\n")
        print(f"{FILENAME} actualizado correctamente.\n")
    except OSError as e:
        print(f"Error al escribir {FILENAME}: {e}")

# Menú principal del programa
def menu():
    crear_archivo_inicial()

    while True:
        print("=== MENÚ ===")
        print("1) Crear archivo inicial (si no existe)")
        print("2) Leer y mostrar productos")
        print("3) Agregar producto (append)")
        print("4) Cargar productos en lista")
        print("5) Buscar producto por nombre")
        print("6) Guardar productos (sobrescribir desde lista)")
        print("7) Salir")
        opt = input("Opción: ").strip()
        print()

        if opt == "1":
            crear_archivo_inicial()
            print(f"{FILENAME} creado si no existía.\n")

        elif opt == "2":
            productos = cargar_productos_en_lista()
            mostrar_productos(productos)
            print()

        elif opt == "3":
            agregar_producto_al_archivo()

        elif opt == "4":
            productos = cargar_productos_en_lista()
            print(f"Se cargaron {len(productos)} productos en la lista.\n")

        elif opt == "5":
            productos = cargar_productos_en_lista()
            buscar_producto_por_nombre(productos)

        elif opt == "6":
            productos = cargar_productos_en_lista()
            if not productos:
                print("No hay productos para guardar.\n")
            else:
                guardar_productos(productos)

        elif opt == "7":
            print("Saliendo.")
            break

        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()
