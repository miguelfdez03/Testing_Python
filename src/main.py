"""
main.py

Programa que verifica si cadenas son palíndromas.
Solicita frases al usuario hasta que escriba 'salir' o 'exit'.

Autor: Miguel Angel Fernandez Muñoz
"""

from utils.string_functions import isPalindrome


def main():
    """Ejecuta el bucle de interacción con el usuario."""
    print("=" * 60)
    print("VERIFICADOR DE PALÍNDROMOS")
    print("=" * 60)
    print("Este programa verifica si una frase es palíndroma.")
    print("Escribe 'salir' o 'exit' para terminar el programa.\n")
    
    while True:
        frase = input("Introduce una frase: ").strip()
        
        if frase.lower() == "salir" or frase.lower() == "exit":
            print("\n" + "=" * 60)
            print("Programa finalizado. ¡Hasta pronto!")
            print("=" * 60)
            break
        
        if not frase:
            print("⚠ Por favor, introduce una frase válida.\n")
            continue
        
        try:
            if isPalindrome(frase):
                print("✓ La frase ES palíndroma.\n")
            else:
                print("✗ La frase NO es palíndroma.\n")
        
        except ValueError as ve:
            print(f"⚠ Error: {ve}\n")
        
        except TypeError as te:
            print(f"⚠ Error: {te}\n")
        
        except Exception as e:
            print(f"⚠ Error inesperado: {e}\n")


if __name__ == "__main__":
    main()
