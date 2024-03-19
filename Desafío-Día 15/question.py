import preguntas as p
import random
from shuffle import shuffle_alt

def choose_q(dificultad):
    preguntas_nivel = p.pool_preguntas.get(dificultad)  # Obtener preguntas para la dificultad dada
    
    if preguntas_nivel:  # Verificar si hay preguntas disponibles para esta dificultad
        # Escoger una pregunta aleatoria si hay preguntas disponibles
        pregunta_key = random.choice(list(preguntas_nivel.keys()))
        pregunta = preguntas_nivel.pop(pregunta_key)
        
        # Obtener enunciado y alternativas mezcladas
        enunciado = pregunta.get('enunciado')
        alternativas = shuffle_alt(pregunta)
        
        return enunciado, alternativas
    else:
        # Devolver None si no hay preguntas disponibles para esta dificultad
        return None, None

if __name__ == '__main__':
    # Verificar el resultado
    enunciado, alternativas = choose_q('basicas')
    print(f'El enunciado es: {enunciado}')
    print(f'Las alternativas son: {alternativas}')
