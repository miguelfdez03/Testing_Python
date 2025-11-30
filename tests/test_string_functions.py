"""
test_string_functions.py

Módulo de testing para la función isPalindrome.

Autor: Miguel Angel Fernandez Muñoz
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.string_functions import isPalindrome


class TestIsPalindrome(unittest.TestCase):
    """Pruebas unitarias para la función isPalindrome."""
    
    def setUp(self):
        """Inicializa casos de prueba."""
        self.palindromos_validos = [
            ("anita lava la tina", True),
            ("Anita lava la tina", True),
            ("ANITA LAVA LA TINA", True),
            ("A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá", True),
            ("Dábale arroz a la zorra el abad", True),
            ("Amo la pacífica paloma", True),
            ("Yo hago yoga hoy", True),
            ("Ana", True),
            ("Reconocer", True),
            ("Oso", True),
            ("A ti no, bonita", True),
            ("Sé verlas al revés", True),
            ("Somos o no somos", True),
            ("Isaac no ronca así", True),
        ]
        
        self.no_palindromos = [
            ("Hola mundo", False),
            ("Python es genial", False),
            ("Esta no es palindroma", False),
            ("Testing unitario", False),
            ("Miguel Fernandez", False),
            ("Programación en Python", False),
        ]
        
        self.casos_limite_validos = [
            ("A", True),
            ("1", True),
            ("121", True),
            ("12321", True),
            ("a b a", True),
            ("¡Anita lava la tina!", True),
            ("Dábale arroz a la zorra el abad", True),
            ("Será o no será", False),
            ("A Santa at Nasa", True),
            ("¿Acaso hubo búhos acá?", True),
        ]
    
    def test_palindromos_validos(self):
        """Verifica que los palíndromos válidos son identificados correctamente."""
        for cadena, esperado in self.palindromos_validos:
            with self.subTest(cadena=cadena):
                resultado = isPalindrome(cadena)
                self.assertEqual(resultado, esperado, f"La cadena '{cadena}' debería ser palíndroma")
    
    def test_no_palindromos(self):
        """Verifica que las cadenas NO palíndromas son identificadas correctamente."""
        for cadena, esperado in self.no_palindromos:
            with self.subTest(cadena=cadena):
                resultado = isPalindrome(cadena)
                self.assertEqual(resultado, esperado, f"La cadena '{cadena}' NO debería ser palíndroma")
    
    def test_casos_limite(self):
        """Prueba casos límite."""
        for cadena, esperado in self.casos_limite_validos:
            with self.subTest(cadena=cadena):
                resultado = isPalindrome(cadena)
                self.assertEqual(resultado, esperado, f"Resultado incorrecto para '{cadena}'")
    
    def test_tipo_incorrecto_numero(self):
        """Verifica TypeError con números."""
        with self.assertRaises(TypeError) as context:
            isPalindrome(12321)
        self.assertIn("cadena de texto", str(context.exception).lower())
    
    def test_tipo_incorrecto_lista(self):
        """Verifica TypeError con listas."""
        with self.assertRaises(TypeError):
            isPalindrome(["a", "n", "a"])
    
    def test_tipo_incorrecto_none(self):
        """Verifica TypeError con None."""
        with self.assertRaises(TypeError):
            isPalindrome(None)
    
    def test_tipo_incorrecto_diccionario(self):
        """Verifica TypeError con diccionarios."""
        with self.assertRaises(TypeError):
            isPalindrome({"cadena": "ana"})
    
    def test_cadena_solo_espacios(self):
        """Verifica ValueError con solo espacios."""
        with self.assertRaises(ValueError) as context:
            isPalindrome("     ")
        self.assertIn("alfanuméricos", str(context.exception).lower())
    
    def test_cadena_solo_puntuacion(self):
        """Verifica ValueError con solo puntuación."""
        with self.assertRaises(ValueError):
            isPalindrome("!@#$%^&*()")
    
    def test_cadena_vacia_con_simbolos(self):
        """Verifica ValueError con cadenas vacías o solo símbolos."""
        casos_invalidos = ["", "   ", "!!!", "???", "...", "---"]
        for cadena in casos_invalidos:
            with self.subTest(cadena=cadena):
                with self.assertRaises(ValueError):
                    isPalindrome(cadena)
    
    def test_palindromos_con_tildes(self):
        """Verifica manejo correcto de tildes."""
        casos_con_tildes = [
            ("Sé verlas al revés", True),
            ("Amo la pacífica paloma", True),
            ("Dábale arroz a la zorra el abad", True),
        ]
        for cadena, esperado in casos_con_tildes:
            with self.subTest(cadena=cadena):
                resultado = isPalindrome(cadena)
                self.assertEqual(resultado, esperado)
    
    def test_palindromos_numericos(self):
        """Verifica palíndromos numéricos."""
        casos_numericos = [
            ("12321", True),
            ("123321", True),
            ("12345", False),
            ("11211", True),
            ("1", True),
        ]
        for cadena, esperado in casos_numericos:
            with self.subTest(cadena=cadena):
                resultado = isPalindrome(cadena)
                self.assertEqual(resultado, esperado)
    
    def test_palindromos_mixtos(self):
        """Verifica palíndromos alfanuméricos mixtos."""
        casos_mixtos = [
            ("A1B2B1A", True),
            ("1A2B2A1", True),
            ("ABC123", False),
        ]
        for cadena, esperado in casos_mixtos:
            with self.subTest(cadena=cadena):
                resultado = isPalindrome(cadena)
                self.assertEqual(resultado, esperado)
    
    def test_frase_ejemplo_actividad(self):
        """Verifica frase de ejemplo de la actividad."""
        frase_valida = "Anita lava la tina"
        self.assertTrue(isPalindrome(frase_valida), f"La frase '{frase_valida}' debe ser palíndroma")
        
        frase_invalida = "Esta frase no es palindroma"
        self.assertFalse(isPalindrome(frase_invalida), f"La frase '{frase_invalida}' NO debe ser palíndroma")


class TestIsPalindromeParametrizado(unittest.TestCase):
    """Pruebas parametrizadas para isPalindrome."""
    
    def test_casos_parametrizados(self):
        """Prueba parametrizada con estructura de datos flexible."""
        casos_de_prueba = {
            "palindromos_simples": [
                ("ana", True),
                ("oso", True),
                ("radar", True),
            ],
            "palindromos_frases": [
                ("anita lava la tina", True),
                ("amo la pacifica paloma", True),
            ],
            "no_palindromos": [
                ("hola", False),
                ("python", False),
                ("testing", False),
            ],
        }
        
        for categoria, casos in casos_de_prueba.items():
            for cadena, esperado in casos:
                with self.subTest(categoria=categoria, cadena=cadena):
                    resultado = isPalindrome(cadena)
                    self.assertEqual(resultado, esperado, f"[{categoria}] Fallo en '{cadena}'")


def suite():
    """Crea suite de pruebas personalizada."""
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTests(loader.loadTestsFromTestCase(TestIsPalindrome))
    test_suite.addTests(loader.loadTestsFromTestCase(TestIsPalindromeParametrizado))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    
    print("=" * 70)
    print("EJECUTANDO PRUEBAS UNITARIAS PARA isPalindrome")
    print("=" * 70)
    print()
    
    result = runner.run(suite())
    print()
    print("=" * 70)
    print("RESUMEN DE RESULTADOS")
    print("=" * 70)
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Tests exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Fallos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    print("=" * 70)
