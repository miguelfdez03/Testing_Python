"""
string_functions.py

Módulo con funciones para análisis de cadenas de texto.

Autor: Miguel Angel Fernandez Muñoz
"""

import unicodedata


# Verifica si una cadena es palíndroma.
# Ignora espacios, puntuación, tildes y mayúsculas/minúsculas.
# Args: cadena (str) - Cadena de texto a verificar
# Returns: bool - True si es palíndroma, False en caso contrario
# Raises: TypeError si el parámetro no es string, ValueError si no contiene caracteres alfanuméricos
def isPalindrome(cadena):
    if not isinstance(cadena, str):
        raise TypeError("El parámetro debe ser una cadena de texto (str)")
    
    # Normalizar para eliminar tildes (NFD descompone caracteres acentuados)
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    
    # Filtrar alfanuméricos y convertir a minúsculas (ignorar marcas diacríticas)
    cadena_limpia = ''.join(
        char.lower() 
        for char in cadena_normalizada 
        if char.isalnum() and not unicodedata.category(char) == 'Mn'
    )
    
    if not cadena_limpia:
        raise ValueError("La cadena no contiene caracteres alfanuméricos válidos")
    
    return cadena_limpia == cadena_limpia[::-1]
