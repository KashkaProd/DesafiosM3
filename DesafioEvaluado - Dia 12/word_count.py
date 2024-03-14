import sys

def contar_caracteres_palabras(texto):
    caracteres_distintos = set(texto)
    palabras_distintas = set(texto.split())

    return caracteres_distintos, palabras_distintas

if __name__ == "__main__":
    if len(sys.argv) == 2:
        archivo_texto = sys.argv[1]

        with open(archivo_texto, "r") as file:
            texto = file.read()

        resultado = contar_caracteres_palabras(texto)

        print(f"El número de caracteres distintos es: {len(resultado[0])}")
        print(f"El número de palabras distintas es: {len(resultado[1])}")
    else:
        print("Formato incorrecto. Debe ingresar el archivo de texto. Ejemplo:")
        print("python word_count.py lorem_ipsum.txt")
