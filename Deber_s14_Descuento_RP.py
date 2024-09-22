def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje al monto total
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devuelve el monto del descuento
    return descuento

# Llamada con solo el monto total, usando el descuento predeterminado del 10%
descuento1 = calcular_descuento(1000)

# Llamada con el monto total y un descuento del 20%
descuento2 = calcular_descuento(1500, 20)

# Imprimir los resultados de la primera llamada
monto_final1 = 1000 - descuento1
print(f"El descuento es: ${descuento1:.2f}")
print(f"El monto final a pagar es: ${monto_final1:.2f}")

# Imprimir los resultados de la segunda llamada
monto_final2 = 1500 - descuento2
print(f"El descuento es: ${descuento2:.2f}")
print(f"El monto final a pagar es: ${monto_final2:.2f}")

