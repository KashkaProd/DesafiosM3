def primeros_auxilios():
    print("que hacer en caso de emergencia?")

    responde_estimulos = input("¿Responde a estímulos? (Sí/No): ").lower()
    if responde_estimulos == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
        print("Programa finalizado.")
        return  # Termina el programa automáticamente
    elif responde_estimulos == "no":
        print("Abrir la vía Aérea.")

        respira = input("¿Respira? (Sí/No): ").lower()
        if respira == "si":
            print("Permitirle posición de suficiente ventilación.")
            print("Esperar ambulancia.")
            print("Programa finalizado.")
            return  # Termina el programa automáticamente
            
        elif respira == "no":
            print("Administrar 5 ventilaciones y llamar a Ambulancia.") 
            
            signos_vida = input("¿Signos de vida? (Sí/No): ").lower()
            if signos_vida == "si":
                print("Reevaluar a la espera de la Ambulancia.")
            elif signos_vida == "no":
                print("Administrar Compresiones Torácicas hasta que llegue la ambulancia.")    
            else:
                print("Respuesta no válida. Reinicie el programa.")
        else:
            print("Respuesta no válida. Reinicie el programa.")
    else:
        print("Respuesta no válida. Reinicie el programa.")

    llego_ambulancia = input("¿Llegó la Ambulancia? (Sí/No): ").lower()
    if llego_ambulancia == "si":
        print("Programa finalizado.")
      
    else:
        print("Seguir esperando ambulancia, programa finalizado")

if __name__ == "__main__":
    primeros_auxilios()
