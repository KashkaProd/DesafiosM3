from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# Valores iniciales
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

# Limpiar pantalla
os.system(op_sys)

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')

opcion = validate(['0', '1'], opcion)

# Definir el comportamiento de salir
if opcion == '0':
    print("Nos vemos pronto!")
    time.sleep(2)
    os.system(op_sys)
    exit()

# Funcionamiento de las preguntas
while correcto and n_pregunta < 3 * p_level:
    if n_pregunta == 0:
        p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
        # Validar el número de preguntas por nivel
        while p_level not in ['1', '2', '3']:
            print("Por favor, ingrese un número válido de preguntas por nivel.")
            p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
        p_level = int(p_level)

    if continuar == 'y':
        n_pregunta += 1
        # Escoger el nivel de la pregunta
        nivel = choose_level(n_pregunta, p_level)
        print(f'Pregunta {n_pregunta}:')
        # Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        enunciado, alternativas = choose_q(nivel)
        if enunciado is None or alternativas is None:
            print("Lo siento, no hay preguntas disponibles para este nivel.")
            time.sleep(3)
            continue
        # Imprimir el enunciado y sus alternativas en pantalla
        print_pregunta(enunciado, alternativas)
        
        respuesta = input('Escoja la alternativa correcta:\n> ').lower()
        # Validar la respuesta entregada
        respuesta = validate(['a', 'b', 'c', 'd'], respuesta)
        # Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas, respuesta)
        
        if correcto and n_pregunta < 3 * p_level:
            print('Muy bien, sigue así!')
            continuar = input('¿Desea continuar? [y/n]: ').lower()
            # Validar si es que se responde 'y' o 'n'
            continuar = validate(['y', 'n'], continuar)
            os.system(op_sys)
        elif correcto and n_pregunta == 3 * p_level:
            print(f'¡Felicitaciones! Has respondido {3 * p_level} preguntas correctas.\nHas ganado la Trivia.\nGracias por Jugar, ¡hasta luego!')
            time.sleep(3)
            os.system(op_sys)
            exit()
        else:
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas.\n¡Sigue participando!')
            time.sleep(3)
            exit()
    else:
        print('Nos vemos la próxima vez, sigue practicando.')
        time.sleep(3)
        exit()
