# preguntas.py
# Preguntas básicas sobre producción musical
preguntas_basicas = {
    'pregunta_1': {'enunciado': ['¿Qué es un compresor en producción musical?'],
                   'alternativas': [['Un dispositivo de hardware para grabar audio', 0],
                                    ['Un efecto que ajusta la dinámica de una señal de audio', 1],
                                    ['Un software para editar pistas de audio', 0],
                                    ['Un módulo para generar sonidos de percusión', 0]]},

    'pregunta_2': {'enunciado': ['¿Qué es una mezcla en producción musical?'],
                   'alternativas': [['Un proceso para combinar diferentes pistas de audio', 1],
                                    ['Un efecto que simula la reverberación de un espacio', 0],
                                    ['Un instrumento musical utilizado en bandas de jazz', 0],
                                    ['Un tipo de ecualización para realzar frecuencias graves', 0]]},

    'pregunta_3': {'enunciado': ['¿Qué es un sintetizador en producción musical?'],
                   'alternativas': [['Un efecto para simular la distorsión de un amplificador', 0],
                                    ['Un instrumento electrónico que genera sonidos', 1],
                                    ['Un software para componer partituras musicales', 0],
                                    ['Un dispositivo para grabar audio en el campo', 0]]}
}

# Preguntas intermedias sobre producción musical
preguntas_intermedias = {
    'pregunta_1': {'enunciado': ['¿Qué es un ecualizador paramétrico en producción musical?'],
                   'alternativas': [['Un dispositivo de hardware para conectar micrófonos', 0],
                                    ['Un tipo de ecualizador que permite ajustar frecuencia, ganancia y ancho de banda', 1],
                                    ['Un software para crear efectos de delay en audio', 0],
                                    ['Un módulo para simular efectos de distorsión en guitarras', 0]]},

    'pregunta_2': {'enunciado': ['¿Qué es una estación de trabajo de audio digital (DAW)?'],
                   'alternativas': [['Un estudio de grabación analógico', 0],
                                    ['Un software para grabar, editar y producir música', 1],
                                    ['Un dispositivo para sincronizar pistas de audio en tiempo real', 0],
                                    ['Un tipo de compresor utilizado en masterización de audio', 0]]},

    'pregunta_3': {'enunciado': ['¿Qué es el MIDI en producción musical?'],
                   'alternativas': [['Un formato de archivo de audio sin pérdida de calidad', 0],
                                    ['Un protocolo estándar para comunicación entre dispositivos musicales', 1],
                                    ['Un tipo de efecto utilizado en mezcla y masterización de audio', 0],
                                    ['Un módulo de síntesis de audio utilizado en producción electrónica', 0]]}
}

# Preguntas avanzadas sobre producción musical
preguntas_avanzadas = {
    'pregunta_1': {'enunciado': ['¿Qué es la síntesis FM en producción musical?'],
                   'alternativas': [['Una técnica para mezclar frecuencias de audio', 0],
                                    ['Una técnica para modular frecuencias utilizando osciladores', 1],
                                    ['Una técnica para filtrar sonidos de alta frecuencia', 0],
                                    ['Una técnica para simular sonidos de instrumentos de viento', 0]]},

    'pregunta_2': {'enunciado': ['¿Qué es un plugin de audio en producción musical?'],
                   'alternativas': [['Un dispositivo de hardware para grabar audio', 0],
                                    ['Un software que se integra con una estación de trabajo de audio digital', 1],
                                    ['Un efecto que modifica la velocidad de reproducción de un audio', 0],
                                    ['Un módulo de ecualización para mezclar pistas de audio', 0]]},

    'pregunta_3': {'enunciado': ['¿Qué es la automatización en producción musical?'],
                   'alternativas': [['Un proceso para ajustar el volumen de una pista de audio', 0],
                                    ['Una técnica para controlar parámetros de efectos a lo largo del tiempo', 1],
                                    ['Una técnica para grabar audio en tiempo real', 0],
                                    ['Un efecto que simula la modulación de frecuencia', 0]]}
}

# Combinar todas las preguntas en un diccionario principal
pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}
