def filtrar_productos(precios, umbral, operacion='mayor'):
    if operacion == 'menor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    elif operacion == 'mayor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    else:
        return "Lo sentimos, no es una operación válida"

    return productos_filtrados

if __name__ == "__main__":
    import sys

    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        resultado = filtrar_productos(precios, umbral)
        print(f"Los productos mayores al umbral son: {', '.join(resultado.keys())}")
    elif len(sys.argv) == 3 and sys.argv[2] in ['mayor', 'menor']:
        umbral = int(sys.argv[1])
        operacion = sys.argv[2]
        resultado = filtrar_productos(precios, umbral, operacion)
        print(f"Los productos {operacion} al umbral son: {', '.join(resultado.keys())}")
    else:
        print("Lo sentimos, no es una operación válida.")

