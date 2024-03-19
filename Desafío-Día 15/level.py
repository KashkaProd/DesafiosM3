def choose_level(n_pregunta, p_level):
    # Definir lógica para escoger el nivel
    if p_level == 1:
        if n_pregunta in [1]:
            return 'basicas'
        elif n_pregunta in [2]:
            return 'intermedias'
        elif n_pregunta in [3]:
            return 'avanzadas'
    elif p_level == 2:
        if n_pregunta in [1, 2]:
            return 'basicas'
        elif n_pregunta in [3, 4]:
            return 'intermedias'
        elif n_pregunta in [5, 6]:
            return 'avanzadas'
    elif p_level == 3:
        if n_pregunta in [1, 2, 3]:
            return 'basicas'
        elif n_pregunta in [4, 5, 6]:
            return 'intermedias'
        elif n_pregunta in [7, 8 , 9]:
            return 'avanzadas'  
    else:
        return None
     

if __name__ == '__main__':
    # Verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
