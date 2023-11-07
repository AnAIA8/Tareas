def decimal_a_binario(decimal):
    binario = bin(decimal)
    return binario

def binario_a_decimal(binario):
        decimal = int(binario, 2)
        return decimal
    
numero_decimal = int(input("Ingrese el número decimal: "))
numero_binario = input("Ingrese el número binario: ")

binario_resultado = decimal_a_binario(numero_decimal)
decimal_resultado = binario_a_decimal(numero_binario)

print(f"Decimal {numero_decimal} en binario: {binario_resultado}")
print(f"Binario {numero_binario} en decimal: {decimal_resultado}")