import preguntas as p

def verificar(alternativas, eleccion):
    # Devuelve el índice de la elección dada
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)
    
    # Generar lógica para determinar respuestas correctas
    respueta_correcta = next(alt for alt in alternativas if alt[1] == 1)
    
    # Verificar si la elección es la respuesta correcta
    if eleccion == alternativas.index(respueta_correcta):
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False
    
if __name__ == '__main__':
    # Verificar la respuesta con una pregunta específica
    pregunta = p.pool_pregunntas['basicas']['pregunta_2']
    respuesta = input('Escoja la alterbativa correcta:\n> ').lower()    
    verificar(pregunta['alternativas'], respuesta)