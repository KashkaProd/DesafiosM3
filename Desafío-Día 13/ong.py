def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def calcular_productoria(lista):
    productoria = 1
    for elemento in lista:
        productoria *= elemento
    return productoria

def calcular(**kwargs):
    for key, value in kwargs.items():
        if 'fact' in key:
            print(f"El factorial de {value} es {calcular_factorial(value)}")
        elif 'prod' in key:
            print(f"La productoria de {value} es {calcular_productoria(value)}")

if __name__ == "__main__":
    calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)
