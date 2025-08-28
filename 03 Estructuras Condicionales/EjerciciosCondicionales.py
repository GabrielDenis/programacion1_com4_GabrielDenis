# ---------------- Ejercicio 1 — Sistema de becas estudiantiles ----------------
nombre_apellido = input("Ingrese nombre y apellido: ")
edad = int(input("Ingrese edad: "))
promedio = float(input("Ingrese promedio general (0-10): "))
ingresos_familiares = float(input("Ingrese ingresos familiares mensuales: "))

print(nombre_apellido, ",", edad, "años")
print("Promedio:", promedio)
print("Ingresos: $", int(ingresos_familiares))

if promedio < 6:
    print("Resultado: Rechazado")
else:
    if ingresos_familiares < 300000:
        print("Resultado: Beca completa")
    elif ingresos_familiares <= 600000:
        print("Resultado: Media beca")
    else:
        print("Resultado: Rechazado")


# ---------------- Ejercicio 2 — Gestión de turnos hospitalarios ----------------
nombre_completo = input("Ingrese nombre completo: ")
dni = input("Ingrese DNI: ")
edad_paciente = int(input("Ingrese edad: "))
obra_social = input("¿Tiene obra social? (si/no): ").lower()
prioridad = int(input("Ingrese prioridad médica (1=emergencia, 2=urgente, 3=control): "))

print("Paciente:", nombre_completo)
print("DNI:", dni)
print("Edad:", edad_paciente)
print("Prioridad:", prioridad)

if prioridad == 1:
    print("Turno asignado: Inmediato en guardia")
elif prioridad == 2:
    if obra_social == "si":
        print("Turno asignado: En menos de 24 hs")
    else:
        print("Turno asignado: En 48 hs")
elif prioridad == 3:
    if edad_paciente > 65:
        print("Turno asignado: Preferencial en 72 hs")
    else:
        print("Turno asignado: Normal en 7 días")


# ---------------- Ejercicio 3 — Evaluación de crédito bancario ----------------
cliente_nombre = input("Ingrese nombre y apellido: ")
cuit = input("Ingrese CUIT: ")
ingresos_mensuales = float(input("Ingrese ingresos mensuales: "))
antiguedad = int(input("Ingrese antigüedad laboral (en años): "))
historial = input("Ingrese historial crediticio (bueno/regular/malo): ").lower()

print("Cliente:", cliente_nombre)
print("CUIT:", cuit)
print("Ingresos: $", int(ingresos_mensuales))
print("Antigüedad:", antiguedad, "años")
print("Historial:", historial)

if historial == "malo":
    print("Monto aprobado: Rechazado")
elif ingresos_mensuales < 200000:
    print("Monto aprobado: Rechazado")
else:
    if antiguedad < 2:
        print("Monto aprobado: $500000")
    else:
        if historial == "regular":
            print("Monto aprobado: $1000000")
        elif historial == "bueno":
            print("Monto aprobado: $3000000")


# ---------------- Ejercicio 1 — Clasificación de impuestos ----------------
nombre_persona = input("Ingrese nombre completo: ")
edad_impuestos = int(input("Ingrese edad: "))
ingresos_anuales = float(input("Ingrese ingresos anuales: "))

print("Nombre: ", nombre_persona)
print("Edad:", edad_impuestos)
print("Ingresos anuales: $", int(ingresos_anuales))

if ingresos_anuales < 500000:
    impuesto = 0
elif ingresos_anuales < 2000000:
    impuesto = ingresos_anuales * 0.10
elif ingresos_anuales < 5000000:
    impuesto = ingresos_anuales * 0.20
else:
    impuesto = ingresos_anuales * 0.35

if edad_impuestos > 65:
    impuesto = impuesto / 2

print("Impuesto a pagar: $", int(impuesto))


# ---------------- Ejercicio 2 — Sistema de calificaciones con promoción ----------------
nombre_alumno = input("Ingrese nombre del alumno: ")
legajo = input("Ingrese número de legajo: ")
nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2: "))
nota3 = int(input("Ingrese nota 3: "))

promedio_notas = (nota1 + nota2 + nota3) / 3

print("Alumno:", nombre_alumno)
print("Legajo:", legajo)
print("Notas:", nota1, nota2, nota3)
print("Promedio:", promedio_notas)

if nota1 < 4 or nota2 < 4 or nota3 < 4:
    print("Estado académico: Desaprobado directo")
elif promedio_notas < 6:
    print("Estado académico: Desaprobado")
elif promedio_notas < 8:
    print("Estado académico: Aprobado con final")
else:
    print("Estado académico: Promocionado")


# ---------------- Ejercicio 3 — Simulador de cajero automático ----------------
usuario_nombre = input("Ingrese nombre del usuario: ")
pin_ingresado = input("Ingrese PIN: ")
pin_correcto = "1234"
saldo = 50000

if pin_ingresado == pin_correcto:
    monto_retiro = input("Ingrese monto a retirar o escriba 'cancelar': ")
    if monto_retiro != "cancelar":
        monto_retiro = int(monto_retiro)
        if monto_retiro % 1000 == 0 and monto_retiro <= saldo:
            if monto_retiro > 20000:
                comision = monto_retiro * 0.02
                saldo = saldo - monto_retiro - comision
            else:
                saldo = saldo - monto_retiro
            print("Retiro exitoso. Saldo actualizado: $", int(saldo))
        else:
            print("Operación no válida")
    else:
        print("Operación cancelada")
else:
    print("PIN incorrecto")


# ---------------- Ejercicio 4 — Categoría de conductores ----------------
nombre_conductor = input("Ingrese nombre del conductor: ")
edad_conductor = int(input("Ingrese edad: "))
experiencia = int(input("Ingrese años de experiencia conduciendo: "))

print("Conductor:", nombre_conductor)

if edad_conductor < 18:
    print("Categoría: No puede conducir")
elif edad_conductor >= 18 and experiencia < 1:
    print("Categoría: Principiante")
elif edad_conductor >= 21 and experiencia >= 1 and experiencia <= 5:
    print("Categoría: Conductor intermedio")
elif edad_conductor >= 30 and experiencia > 10:
    print("Categoría: Conductor profesional")
else:
    print("Categoría: Conductor estándar")


# ---------------- Ejercicio 5 — Simulador de carrito de compras ----------------
nombre_cliente = input("Ingrese nombre del cliente: ")
cantidad_productos = int(input("Ingrese cantidad de productos: "))
monto_total = float(input("Ingrese monto total de la compra: "))
medio_pago = input("Ingrese medio de pago (efectivo, debito, credito, mercado_pago): ").lower()

print("Cliente:", nombre_cliente)
print("Productos:", cantidad_productos)
print("Monto total: $", monto_total)
print("Medio de pago:", medio_pago)

if medio_pago == "efectivo":
    monto_total = monto_total * 0.85
elif medio_pago == "debito":
    monto_total = monto_total * 0.90
elif medio_pago == "credito":
    monto_total = monto_total * 1.05
elif medio_pago == "mercado_pago":
    if monto_total > 10000:
        monto_total = monto_total * 0.80

if cantidad_productos > 10:
    monto_total = monto_total * 0.95

print("Importe final a pagar: $", monto_total)
