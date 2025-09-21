letras = ["A", "A", "A"]
numeros = 0

incremento = int(input("Ingrese un número: "))

numeros += incremento

while numeros > 999:
    numeros -= 1000
    letras[2] = chr(ord(letras[2]) + 1)
    if letras[2] > "Z":
        letras[2] = "A"
        letras[1] = chr(ord(letras[1]) + 1)
        if letras[1] > "Z":
            letras[1] = "A"
            letras[0] = chr(ord(letras[0]) + 1)

# Armar la patente final
patente = "".join(letras) + f"{numeros:03d}"

print("La patente es:", patente)
