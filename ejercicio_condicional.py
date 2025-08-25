fecha = input("Ingrese la fecha en formato 'día, DD/MM': ")

partes = fecha.split(",")
if len(partes) != 2:
    print("Error en el formato")
else:
    dia = partes[0].strip().lower()
    fecha_num = partes[1].strip().split("/")
    if len(fecha_num) != 2:
        print("Error en el formato")
    else:
        dia_num = int(fecha_num[0])
        mes_num = int(fecha_num[1])

        if dia_num < 1 or dia_num > 31 or mes_num < 1 or mes_num > 12:
            print("Error en la fecha")
        elif dia not in ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"]:
            print("Error en el día")
        elif dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "miercoles":
            hubo_examen = input("¿Hubo examen? (si/no): ").lower()
            if hubo_examen == "si":
                aprobados = int(input("Ingrese la cantidad de aprobados: "))
                desaprobados = int(input("Ingrese la cantidad de desaprobados: "))
                total = aprobados + desaprobados
                if total > 0:
                    porcentaje = (aprobados * 100) / total
                    print("Porcentaje de aprobados:", porcentaje, "%")
                else:
                    print("No hubo alumnos para calcular")
            else:
                print("No hubo examen")
        elif dia == "jueves":
            asistencia = float(input("Ingrese el porcentaje de asistencia: "))
            if asistencia > 50:
                print("asistió la mayoría")
            else:
                print("no asistió la mayoría")
        elif dia == "viernes":
            if dia_num == 1 and (mes_num == 1 or mes_num == 7):
                print("Comienzo de nuevo ciclo")
                alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                arancel = float(input("Ingrese el arancel por alumno: "))
                ingreso_total = alumnos * arancel
                print("Ingreso total: $", ingreso_total)
            else:
                print("Clase normal de inglés para viajeros")
