# Calculadora de propinas en un restaurante

cuenta = float(input("Ingrese el monto de la cuenta: "))

propina_10 = cuenta * 0.10
propina_15 = cuenta * 0.15

total_10 = cuenta + propina_10
total_15 = cuenta + propina_15

print(f"Propina sugerida (10%): {propina_10}")
print(f"Total a pagar (10%): {total_10}")
print(f"Propina sugerida (15%): {propina_15}")
print(f"Total a pagar (15%): {total_15}")
