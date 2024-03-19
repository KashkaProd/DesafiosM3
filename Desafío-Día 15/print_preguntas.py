def print_pregunta(enunciado, alternativas):
    # Imprimir enunciado
    print(enunciado[0])
    print()  # Salto de línea
    
    # Imprimir alternativas con la letra asociada
    for i, alt in enumerate(alternativas):
        print(f'{chr(65 + i)}. {alt[0]}')

if __name__ == '__main__':
    # No es necesario verificar el resultado aquí ya que este script se utiliza como un módulo.
    pass
   