def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva + (cantidad_sin_iva * (porcentaje_iva / 100))
    return total

cantidad_sin_iva = float(input("Ingrse la cantidad sin IVA: "))
total = calcular_total_factura(cantidad_sin_iva)
print(total)

total_con_iva_personalizado = calcular_total_factura(cantidad_sin_iva, float(input("Ingrese la cantidad de IVA: ")))
print(total_con_iva_personalizado)