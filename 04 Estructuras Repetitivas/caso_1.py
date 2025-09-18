flag = True
titulos = []
ejemplares = []

while flag:

    print("Bienvenido, elija las siguientes opciones:")
    print("1.Ingresar libros iniciales")
    print("2.Cargar ejemplares")
    print("3.Ver catalogo completo")
    print("4.Consultar disponibilidad")
    print("5.Listar agotados")
    print("6.Agregar titulo nuevo")
    print("7.Actualizar ejemplares (Prestamo/Devolucion)")
    print("8.Ver catalogo con ejemplares disponibles")
    print("9.Salir")

    opcion = input("")

    if opcion.isdigit() == False:
        print("Error: debe ingresar un numero valido entre 1 y 9")
        continue
    else:
        opt = int(opcion)

    if opt == 1:
        titulos = []
        ejemplares = []

        while True:
            num = input("Cuantos libros desea ingresar: ")

            if num.isdigit() == False or int(num) <= 0:
                print("Error: ingrese un numero entero positivo")
                continue

            num = int(num)

            for n in range(num):
                libro = input("Ingrese el titulo del libro: ").strip()

                if libro == "":
                    print("Error: el titulo no puede estar vacio")
                    continue

                if libro in titulos:
                    print("Error: el titulo ya existe en el catalogo")
                    continue

                copias = input("Cuantas copias tiene el libro: ")

                if copias.isdigit() == False or int(copias) < 0:
                    print("Error: la cantidad de copias debe ser un numero entero >= 0")
                    continue

                titulos.append(libro)
                ejemplares.append(int(copias))

            salir = input("Si no desea añadir mas ingrese 0: ")

            if salir == "0":
                break

    elif opt == 2:
        if len(titulos) == 0:
            print("No hay libros cargados")
        else:
            for n in range(len(titulos)):
                copias = input(f"Ingrese las copias disponibles de {titulos[n]}: ")

                if copias.isdigit():
                    ejemplares[n] = int(copias)
                else:
                    print("Error: debe ingresar un numero entero")

    elif opt == 3:
        if len(titulos) == 0:
            print("El catalogo esta vacio")
        else:
            for n in range(len(titulos)):
                print(f"{titulos[n]}: {ejemplares[n]} copias")

    elif opt == 4:
        titulo = input("Ingrese el titulo a consultar: ").strip()

        if titulo in titulos:
            i = titulos.index(titulo)
            print(f"{titulos[i]}: {ejemplares[i]} copias disponibles")
        else:
            print("El titulo no existe en el catalogo")

    elif opt == 5:
        agotados = False

        for n in range(len(titulos)):
            if ejemplares[n] == 0:
                print(f"{titulos[n]} agotado")
                agotados = True
        if not agotados:
            print("No hay libros agotados")

    elif opt == 6:
        titulo = input("Ingrese el nuevo titulo: ").strip()

        if titulo == "":
            print("Error: el titulo no puede estar vacio")
        elif titulo not in titulos:
            copias = input("Ingrese el numero de copias: ")

            if copias.isdigit() and int(copias) >= 0:
                titulos.append(titulo)
                ejemplares.append(int(copias))
                print(f"Titulo {titulo} agregado con {copias} copias")
            else:
                print("Error: la cantidad de copias debe ser un numero entero >= 0")
        else:
            print("El titulo ya existe en el catalogo")

    elif opt == 7:
        titulo = input("Ingrese el titulo a actualizar: ").strip()

        if titulo in titulos:
            i = titulos.index(titulo)
            print("1.Prestamo")
            print("2.Devolucion")
            act = input("")
            if act == "1":
                cantidad = input("Ingrese la cantidad a prestar: ")

                if cantidad.isdigit() and int(cantidad) > 0:
                    cantidad = int(cantidad)

                    if cantidad <= ejemplares[i]:
                        ejemplares[i] -= cantidad
                        print(f"Se prestaron {cantidad} ejemplares de {titulo}")
                    else:
                        print("Error: no hay suficientes ejemplares disponibles")
                else:
                    print("Error: la cantidad debe ser un numero entero positivo")
            elif act == "2":
                cantidad = input("Ingrese la cantidad a devolver: ")

                if cantidad.isdigit() and int(cantidad) >= 1:
                    cantidad = int(cantidad)
                    ejemplares[i] += cantidad
                    print(f"Se devolvieron {cantidad} ejemplares de {titulo}")
                else:
                    print("Error: la devolucion debe ser al menos 1 ejemplar")
            else:
                print("Error: opcion invalida")
        else:
            print("El titulo no existe en el catalogo")

    elif opt == 8:
        disponibles = False
        
        for n in range(len(titulos)):
            if ejemplares[n] > 0:
                print(f"{titulos[n]}: {ejemplares[n]} copias")
                disponibles = True
        if not disponibles:
            print("No hay libros disponibles actualmente")

    elif opt == 9:
        print("Has salido del menu")
        flag = False

    else:
        print("Error: opcion invalida, ingrese un numero entre 1 y 9")
