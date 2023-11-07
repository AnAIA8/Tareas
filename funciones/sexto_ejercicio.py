def calcular_media(muestra):
    if len(muestra) == 0:
        return None
    suma = sum(muestra)
    media = suma / len(muestra)
    return media

numeros = [int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese otro número: "))]
media = calcular_media(numeros)
print(f"La media de la muestra de números es: {media}")