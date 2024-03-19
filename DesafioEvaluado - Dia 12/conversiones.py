import sys

def convertir_pesos(tasa_soles, tasa_pesos_arg, tasa_dolar, valor_pesos):
    soles = valor_pesos * tasa_soles
    pesos_argentinos = valor_pesos * tasa_pesos_arg
    dolares = valor_pesos * tasa_dolar

    return soles, pesos_argentinos, dolares

if __name__ == "__main__":
    if len(sys.argv) == 5:
        tasa_soles = float(sys.argv[1])
        tasa_pesos_arg = float(sys.argv[2])
        tasa_dolar = float(sys.argv[3])
        valor_pesos = float(sys.argv[4])

        resultados = convertir_pesos(tasa_soles, tasa_pesos_arg, tasa_dolar, valor_pesos)

        print(f"Los {valor_pesos} pesos equivalen a:")
        print(f"{resultados[0]} Soles")
        print(f"{resultados[1]} Pesos Argentinos")
        print(f"{resultados[2]} Dólares")
    else:
        print("Formato incorrecto. Debe ingresar las tasas y el valor en pesos. Ejemplo:")
        print("python conversiones.py 0.0046 0.093 0.0013 10000")

