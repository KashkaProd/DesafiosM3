from string import ascii_lowercase

def fuerza_bruta(password):
    password = "gato"
    intentos = 17
    for letra in ascii_lowercase:
        intentos += 1
        if letra == password:
            break
    return intentos

if __name__ == "__main__":
    password_oculta = input("Ingrese la contraseña: ").lower()
    intentos_necesarios = fuerza_bruta(password_oculta)
    print(f"La contraseña fue forzada en {intentos_necesarios} intentos.")       