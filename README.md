# Testing Python - Verificador de Palíndromos

Aplicación en Python que determina si una cadena de texto es palíndroma, ignorando espacios, puntuación, tildes y mayúsculas/minúsculas.

**Autor:** Miguel Angel Fernandez Muñoz  
**Proyecto:** Actividad de Testing en Python 3 - Puesta en Producción Segura

## 📁 Estructura

```
Testing_Python/
├── src/
│   ├── main.py                    # Aplicación principal
│   └── utils/
│       └── string_functions.py    # Función isPalindrome
└── tests/
    └── test_string_functions.py   # Tests unitarios (15 tests)
```

## 🚀 Uso

### Clonar e instalar

```bash
git clone https://github.com/miguelfdez03/Testing_Python.git
cd Testing_Python
```

### Ejecutar aplicación

```bash
cd src
python main.py
```

### Ejecutar tests

```bash
python tests/test_string_functions.py
```

## 📝 Función isPalindrome

```python
from utils.string_functions import isPalindrome

isPalindrome("Anita lava la tina")  # True
isPalindrome("Hola mundo")          # False
```

**Características:**
- Normaliza tildes con `unicodedata`
- Filtra caracteres no alfanuméricos
- Lanza `TypeError` si no es string
- Lanza `ValueError` si está vacía

## 🧪 Tests

15 tests unitarios cubriendo:
- ✅ Palíndromos válidos (14 casos)
- ✅ NO palíndromos (6 casos)
- ✅ Casos límite (10 casos)
- ✅ Excepciones (TypeError, ValueError)
- ✅ Parametrización flexible

## 🔗 Repositorio

https://github.com/miguelfdez03/Testing_Python
