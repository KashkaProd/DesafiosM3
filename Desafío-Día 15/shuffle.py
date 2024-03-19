import preguntas as p
import random

def shuffle_alt(pregunta):
    #Mezclar alternativas
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    #Verificar el resultado
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))
    #Ejemplo de resultado esperando: [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
