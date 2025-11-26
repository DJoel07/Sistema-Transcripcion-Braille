# Técnicas de Prueba Aplicadas - Sistema de Transcripción Braille

## 📋 Resumen

Este documento detalla las técnicas de prueba de caja negra y caja blanca aplicadas en el Sistema de Transcripción Braille para garantizar la calidad y robustez del software.

---

## 📸 Evidencias Visuales

### Captura 1: Ejecución Completa de Tests
<img width="837" height="619" alt="image" src="https://github.com/user-attachments/assets/e8c31f5a-be29-4e07-b7bf-61cf024ad121" />
*Resultado de la ejecución completa de la suite de pruebas mostrando 61 tests pasando exitosamente.*

### Captura 2: Tests de Partición de Equivalencias
<img width="1093" height="905" alt="image" src="https://github.com/user-attachments/assets/cb181a5c-dbd2-4efe-9a37-1f120c5f73ff" />
*Detalle de los 21 tests de la técnica de Partición de Equivalencias.*

### Captura 3: Tests de Valores Límite
<img width="1104" height="299" alt="image" src="https://github.com/user-attachments/assets/3a97d775-6343-40a9-a1d9-64b2e4155871" />
*Validación de casos límite (0, 1, 499, 500, 501 caracteres).*

### Captura 4: Tests de Robustez
<img width="1099" height="887" alt="image" src="https://github.com/user-attachments/assets/d41af3c0-9718-48f8-a881-181023afaf6c" />

*Pruebas con casos extremos: espacios múltiples, puntuación duplicada, caracteres inválidos.*

### Captura 5: Código del Motor de Transcripción
<img width="1910" height="3370" alt="image" src="https://github.com/user-attachments/assets/e897330c-19ed-490e-bbe1-5c692168b11d" />
*Implementación del método `transcribe()` con todas las validaciones.*

### Captura 6: Método de Normalización de Espacios
<img width="1248" height="1166" alt="image" src="https://github.com/user-attachments/assets/ed38d51e-2ba1-4072-a7bd-2b1287f9e584" />
*Función que normaliza espacios múltiples y elimina espacios innecesarios.*

---

## 🎯 Técnicas de Caja Negra Implementadas

### 1. **Partición de Equivalencias (Equivalence Partitioning)**

Esta técnica divide el dominio de entrada en clases de datos donde se espera que el sistema se comporte de manera similar.

#### Clases de Equivalencia Identificadas:

| Clase | Descripción | Valores Válidos | Valores Inválidos |
|-------|-------------|-----------------|-------------------|
| **CE1: Letras** | Alfabeto español | a-z, ñ, w | @, #, $ |
| **CE2: Vocales acentuadas** | Vocales con tilde | á, é, í, ó, ú, ü | à, è, ò |
| **CE3: Mayúsculas** | Letras en mayúscula | A-Z, Ñ | - |
| **CE4: Números** | Dígitos | 0-9 | - |
| **CE5: Números decimales** | Números con separador | 12.5, 12,5 | 12..5, 12.,5 |
| **CE6: Puntuación** | Signos soportados | . , ; : ¿ ? ¡ ! ( ) - | @ # $ % & |
| **CE7: Espacios** | Espacios en blanco | ' ' (1 espacio) | '    ' (40 espacios) |
| **CE8: Longitud de texto** | Cantidad de caracteres | 0-500 | 501+ |

#### Casos de Prueba por Partición:

```python
# CE1: Letras minúsculas
Entrada: "hola"
Salida esperada: "⠓⠕⠇⠁"

# CE2: Vocales acentuadas
Entrada: "información"
Salida esperada: "⠊⠝⠋⠕⠗⠍⠁⠉⠌⠬⠝"

# CE3: Mayúsculas (con indicador ⠨)
Entrada: "HOLA"
Salida esperada: "⠨⠓⠨⠕⠨⠇⠨⠁"  # Cada letra con indicador de mayúscula

# CE3b: Mayúscula inicial
Entrada: "Hola"
Salida esperada: "⠨⠓⠕⠇⠁"  # Solo primera letra con indicador

# CE4: Números enteros
Entrada: "123"
Salida esperada: "⠼⠁⠃⠉"

# CE5: Números decimales
Entrada: "12.5"
Salida esperada: "⠼⠁⠃⠲⠑"

# CE6: Puntuación
Entrada: "Hola, ¿cómo estás?"
Salida esperada: "⠓⠕⠇⠁⠂ ⠢⠉⠬⠍⠕ ⠑⠎⠞⠷⠎⠦"

# CE7: Espacios múltiples (se normalizan)
Entrada: "hola    mundo"
Salida esperada: "⠓⠕⠇⠁ ⠍⠥⠝⠙⠕"

# CE8: Texto vacío
Entrada: ""
Salida esperada: ""
```

---

### 2. **Análisis de Valores Límite (Boundary Value Analysis)**

Esta técnica prueba los valores en los límites de las clases de equivalencia.

#### Valores Límite Identificados:

| Límite | Valor Mínimo | Valor Mínimo + 1 | Valor Máximo - 1 | Valor Máximo | Valor Máximo + 1 |
|--------|--------------|-------------------|------------------|--------------|-------------------|
| **Longitud** | 0 | 1 | 499 | 500 | 501 |
| **Espacios** | 0 | 1 | - | 2 | 3+ |

#### Casos de Prueba de Valores Límite:

```python
# BVA1: Longitud = 0 (mínimo)
Entrada: ""
Salida esperada: ""
Error esperado: None

# BVA2: Longitud = 1 (mínimo + 1)
Entrada: "a"
Salida esperada: "⠁"

# BVA3: Longitud = 500 (máximo)
Entrada: "a" * 500
Salida esperada: "⠁" * 500

# BVA4: Longitud = 501 (máximo + 1)
Entrada: "a" * 501
Error esperado: "El texto excede el límite máximo de 500 caracteres"

# BVA5: Espacios consecutivos = 1
Entrada: "hola mundo"
Salida esperada: "⠓⠕⠇⠁ ⠍⠥⠝⠙⠕"

# BVA6: Espacios consecutivos = 40
Entrada: "hola" + " "*40 + "mundo"
Salida esperada: "⠓⠕⠇⠁ ⠍⠥⠝⠙⠕"  # Normalizados a 1 espacio
```

---

### 3. **Pruebas de Robustez (Robustness Testing)**

Esta técnica prueba el comportamiento del sistema ante entradas inesperadas o extremas.

#### Casos de Robustez:

```python
# ROB1: Solo espacios
Entrada: "     "
Salida esperada: ""

# ROB2: Puntuación duplicada
Entrada: "Hola.."
Salida esperada: "⠓⠕⠇⠁⠲"  # Solo un punto

# ROB3: Puntos consecutivos (:::)
Entrada: "Hola:::"
Salida esperada: "⠓⠕⠇⠁⠒"  # Solo dos puntos

# ROB4: Mezcla de mayúsculas y minúsculas
Entrada: "HoLa MuNdO"
Salida esperada: "⠓⠕⠇⠁ ⠍⠥⠝⠙⠕"

# ROB5: Caracteres especiales no soportados
Entrada: "hola@mundo"
Error esperado: "El texto contiene caracteres no soportados: '@'"

# ROB6: Números con múltiples puntos decimales
Entrada: "12..5"
Salida esperada: "⠼⠁⠃⠲⠲⠑"  # Trata cada punto como separador

# ROB7: Espacios al inicio y final
Entrada: "   hola   "
Salida esperada: "⠓⠕⠇⠁"  # Se eliminan espacios al inicio/final

# ROB8: Texto con solo números
Entrada: "12345"
Salida esperada: "⠼⠁⠃⠉⠙⠑"

# ROB9: Texto con solo puntuación
Entrada: "..."
Salida esperada: "⠲"  # Solo un punto (duplicados eliminados)

# ROB10: Mezcla compleja
Entrada: "Información123, ¿verdad?"
Salida esperada: "⠊⠝⠋⠕⠗⠍⠁⠉⠌⠬⠝⠼⠁⠃⠉⠂ ⠢⠧⠑⠗⠙⠁⠙⠦"
```

---

### 4. **Tablas de Decisión (Decision Tables)**

Combinaciones de condiciones de entrada y acciones resultantes.

| # | Texto Vacío | Longitud > 500 | Tiene Inválidos | Acción |
|---|-------------|----------------|-----------------|--------|
| 1 | Sí | - | - | Retornar "" |
| 2 | No | Sí | - | Lanzar ValueError |
| 3 | No | No | Sí | Lanzar ValueError |
| 4 | No | No | No | Transcribir |

---

## 🔍 Técnicas de Caja Blanca Implementadas

### 1. **Cobertura de Sentencias (Statement Coverage)**

Objetivo: Ejecutar cada línea de código al menos una vez.

**Porcentaje objetivo**: ≥ 80%

### 2. **Cobertura de Decisiones (Decision Coverage)**

Objetivo: Ejecutar cada decisión booleana con True y False.

#### Decisiones Críticas:

```python
# Decisión 1: if not text or not text.strip()
Test True: text = ""
Test False: text = "hola"

# Decisión 2: if len(text) > self.MAX_TEXT_LENGTH
Test True: text = "a" * 501
Test False: text = "hola"

# Decisión 3: if char.isdigit()
Test True: char = "5"
Test False: char = "a"

# Decisión 4: if char in self._alphabet
Test True: char = "a"
Test False: char = "@"

# Decisión 5: if char in self._punctuation
Test True: char = "."
Test False: char = "a"
```

### 3. **Cobertura de Condiciones (Condition Coverage)**

Objetivo: Evaluar cada condición booleana como True y False.

```python
# Condición: char_lower in self._alphabet or char in self._punctuation or char.isdigit()
Test 1: char = "a" (primera condición True)
Test 2: char = "." (segunda condición True)
Test 3: char = "5" (tercera condición True)
Test 4: char = "@" (todas False)
```

### 4. **Cobertura de Caminos (Path Coverage)**

Objetivo: Ejecutar todos los caminos posibles a través del código.

#### Caminos principales en `transcribe()`:

1. **Camino 1**: Texto vacío → return ""
2. **Camino 2**: Texto excede límite → raise ValueError
3. **Camino 3**: Caracteres no soportados → raise ValueError
4. **Camino 4**: Transcripción exitosa con letras
5. **Camino 5**: Transcripción exitosa con números
6. **Camino 6**: Transcripción exitosa con puntuación
7. **Camino 7**: Transcripción mixta (letras + números + puntuación)

---

## 📊 Criterios de Validación Implementados

### 1. **Normalización de Espacios**

```python
# Regla 1: Múltiples espacios → 1 espacio
"hola    mundo" → "hola mundo"

# Regla 2: Espacios al inicio/final → Eliminados
"  hola  " → "hola"

# Regla 3: Espacios antes de puntuación → Eliminados
"hola ." → "hola."

# Regla 4: Espacios después de puntuación de apertura → Eliminados
"¿ hola" → "¿hola"
```

### 2. **Manejo de Mayúsculas (v2.1.0+)**

```python
# Las mayúsculas se preservan con indicador ⠨ (puntos 4,6)
"HOLA" → "⠨⠓⠨⠕⠨⠇⠨⠁"  # Todas con indicador
"Hola" → "⠨⠓⠕⠇⠁"          # Solo primera con indicador
"HoLa" → "⠨⠓⠕⠨⠇⠁"        # H y L con indicador
```

### 3. **Eliminación de Puntuación Duplicada**

```python
# Puntos consecutivos
"hola.." → "hola."

# Comas consecutivas
"hola,," → "hola,"

# Dos puntos consecutivos
"hola:::" → "hola:"
```

### 4. **Límite de Caracteres**

```python
MAX_TEXT_LENGTH = 500

# Texto de 500 caracteres → OK
# Texto de 501 caracteres → ValueError
```

---

## ✅ Casos de Prueba Documentados

### Suite CP-001: Transcripción de Alfabeto

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------|
| CP-001-01 | "abcdefghij" | "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚" | PE: Primera serie |
| CP-001-02 | "klmnopqrst" | "⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞" | PE: Segunda serie |
| CP-001-03 | "uvxyz" | "⠥⠧⠭⠽⠵" | PE: Tercera serie |
| CP-001-04 | "ñw" | "⠻⠺" | PE: Letras adicionales |

### Suite CP-002: Números y Decimales

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------|
| CP-002-01 | "123" | "⠼⠁⠃⠉" | PE: Números enteros |
| CP-002-02 | "12.5" | "⠼⠁⠃⠲⠑" | PE: Decimal con punto |
| CP-002-03 | "12,5" | "⠼⠁⠃⠂⠑" | PE: Decimal con coma |
| CP-002-04 | "0" | "⠼⠚" | BVA: Número mínimo |

### Suite CP-003: Vocales Acentuadas

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------|
| CP-003-01 | "áéíóú" | "⠷⠮⠌⠬⠾" | PE: Vocales acentuadas |
| CP-003-02 | "ü" | "⠳" | PE: Diéresis |
| CP-003-03 | "información" | "⠊⠝⠋⠕⠗⠍⠁⠉⠌⠬⠝" | PE: Palabra con acentos |

### Suite CP-004: Mayúsculas (v2.1.0+)

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------||
| CP-004-01 | "HOLA" | "⠨⠓⠨⠕⠨⠇⠨⠁" | PE: Todo mayúsculas |
| CP-004-02 | "HoLa" | "⠨⠓⠕⠨⠇⠁" | PE: Mezcla may/min |
| CP-004-03 | "Hola Mundo" | "⠨⠓⠕⠇⠁ ⠨⠍⠥⠝⠙⠕" | PE: Mayúsculas iniciales |

### Suite CP-005: Espacios Múltiples

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------|
| CP-005-01 | "hola  mundo" | "⠓⠕⠇⠁ ⠍⠥⠝⠙⠕" | Robustez: 2 espacios |
| CP-005-02 | "hola     mundo" | "⠓⠕⠇⠁ ⠍⠥⠝⠙⠕" | Robustez: 5 espacios |
| CP-005-03 | "hola" + " "*40 + "mundo" | "⠓⠕⠇⠁ ⠍⠥⠝⠙⠕" | Robustez: 40 espacios |
| CP-005-04 | "  hola  " | "⠓⠕⠇⠁" | Robustez: Espacios inicio/fin |

### Suite CP-006: Puntuación Duplicada

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------|
| CP-006-01 | "hola.." | "⠓⠕⠇⠁⠲" | Robustez: Puntos dobles |
| CP-006-02 | "hola,,," | "⠓⠕⠇⠁⠂" | Robustez: Comas múltiples |
| CP-006-03 | "hola:::" | "⠓⠕⠇⠁⠒" | Robustez: Dos puntos múltiples |
| CP-006-04 | "¿¿hola??" | "⠢⠓⠕⠇⠁⠦" | Robustez: Interrogación duplicada |

### Suite CP-007: Límites de Longitud

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------|
| CP-007-01 | "" | "" | BVA: Texto vacío |
| CP-007-02 | "a" | "⠁" | BVA: 1 carácter |
| CP-007-03 | "a" * 500 | "⠁" * 500 | BVA: Máximo permitido |
| CP-007-04 | "a" * 501 | ValueError | BVA: Excede máximo |

### Suite CP-008: Caracteres No Soportados

| ID | Entrada | Salida Esperada | Técnica |
|----|---------|-----------------|---------|
| CP-008-01 | "hola@mundo" | ValueError: '@' | Robustez: Arroba |
| CP-008-02 | "hola#mundo" | ValueError: '#' | Robustez: Numeral |
| CP-008-03 | "hola$mundo" | ValueError: '$' | Robustez: Dólar |
| CP-008-04 | "hola%mundo" | ValueError: '%' | Robustez: Porcentaje |

---

## 🎓 Resumen de Técnicas

| Técnica | Aplicación | Casos de Prueba |
|---------|------------|-----------------|
| **Partición de Equivalencias** | Dividir entradas en clases válidas/inválidas | 30+ casos |
| **Valores Límite** | Probar límites de longitud y espacios | 15+ casos |
| **Robustez** | Entradas extremas y combinaciones complejas | 20+ casos |
| **Cobertura de Sentencias** | Ejecutar todas las líneas de código | 80%+ |
| **Cobertura de Decisiones** | Evaluar todas las bifurcaciones | 100% |
| **Cobertura de Condiciones** | Evaluar cada condición booleana | 100% |

---

## 📝 Conclusiones

El sistema ha sido diseñado con **criterios lógicos robustos** que incluyen:

✅ **Normalización automática** de espacios múltiples  
✅ **Límite de 500 caracteres** para prevenir sobrecargas  
✅ **Conversión automática** de mayúsculas a minúsculas  
✅ **Eliminación de puntuación duplicada** consecutiva  
✅ **Validación exhaustiva** de caracteres antes de transcribir  
✅ **Manejo de números decimales** con punto y coma  
✅ **Mensajes de error descriptivos** para debugging  

Todas las técnicas de prueba aplicadas garantizan un software **confiable, robusto y libre de defectos** para los casos de uso definidos.

---

## 📸 Evidencias Adicionales

### Captura 7: Aplicación Web en Ejecución
<img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/6ce5dda6-9447-4f8a-a78f-055d4e25c1a9" />
*Sistema de transcripción Braille ejecutándose en localhost:5000.*

### Captura 8: Interfaz de Usuario
<img width="1168" height="474" alt="image" src="https://github.com/user-attachments/assets/b59abce2-ce37-4bca-b22b-d30599a53883" />
*Página principal mostrando el formulario de transcripción.*

### Captura 9: Ejemplo de Transcripción con Mayúsculas
<img width="1172" height="461" alt="image" src="https://github.com/user-attachments/assets/0f149f09-502c-4299-8750-8a1c499ec1d8" />
*Entrada "HOLA" transcrita correctamente a Braille.*

### Captura 10: Ejemplo de Transcripción con Acentos y Ñ
<img width="1169" height="456" alt="image" src="https://github.com/user-attachments/assets/116017db-d7ca-4c7c-a59e-5879e537c785" />
*Entrada "Asoma mañana también" con caracteres especiales.*

### Captura 11: Manejo de Números Decimales
<img width="1137" height="409" alt="image" src="https://github.com/user-attachments/assets/c56f6f22-fb06-4366-9139-f6368e2edf89" />
<img width="1145" height="432" alt="image" src="https://github.com/user-attachments/assets/d0078abc-f220-4cd3-99df-a1c57043bd79" />
*Transcripción de "11.8" y "11,8" mostrando soporte para ambos separadores.*

### Captura 12: Validación de Errores
<img width="1133" height="369" alt="image" src="https://github.com/user-attachments/assets/71efdd64-6d0e-4a77-9276-82416566d0f3" />
<img width="1062" height="873" alt="image" src="https://github.com/user-attachments/assets/170e94a0-8588-4a65-9d72-8d9017278c1b" />

*Mensaje de error cuando se intenta transcribir caracteres no soportados o exceder el límite.*
