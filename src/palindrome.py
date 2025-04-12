def is_palindrome(word):

    #Limpieza de caracteres especiales, espacios, mayúsculas y minúsculas
    # Caracteres especiales y espacios
    special_chars = [' ', '.', ',', '!', '?', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}', "'", '"']
    word = word.lower() # Para no diferenciar entre mayúsculas y minúsculas
    
    # Eliminar caracteres especiales y espacios
    for char in special_chars:
        word = word.replace(char, '')

    return word == word[::-1]
    