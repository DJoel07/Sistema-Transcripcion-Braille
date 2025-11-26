# Manual de Usuario - Sistema de Transcripción Braille

## 📖 Introducción

### ¿Qué es el Sistema de Transcripción Braille?

El Sistema de Transcripción Braille es una aplicación web diseñada para convertir texto en español a su representación en sistema Braille y generar señalética imprimible de alta calidad. La aplicación permite a personas sin discapacidad visual producir etiquetas y señales Braille de forma económica y accesible.

### ¿Para quién es esta aplicación?

- **Instituciones educativas** que necesitan crear señalética Braille
- **Negocios y oficinas** que desean mejorar la accesibilidad
- **Diseñadores** que trabajan en proyectos inclusivos
- **Familias** con miembros con discapacidad visual
- **Estudiantes** aprendiendo sobre accesibilidad

### Características Principales

✅ Transcripción instantánea de texto español a Braille  
✅ Soporte completo del alfabeto español (incluyendo ñ, w)  
✅ Manejo de vocales acentuadas (á, é, í, ó, ú, ü)  
✅ Transcripción de números con formato Braille correcto  
✅ Signos de puntuación básicos  
✅ Generación de PDF listo para imprimir  
✅ Interfaz intuitiva y fácil de usar  
✅ Diseño responsive (funciona en computadora, tablet y móvil)

---

## 🚀 Inicio Rápido (5 minutos)

### Paso 1: Acceder a la Aplicación

1. Abrir navegador web (Chrome, Firefox, Edge)
2. Navegar a: `http://localhost:5000`
   - O la dirección proporcionada por tu administrador

### Paso 2: Transcribir tu Primer Texto

1. En el campo de texto grande, escribir: **"Baño"**
2. Hacer clic en el botón azul **"Transcribir a Braille"**
3. ¡Listo! Verás el resultado: **⠃⠁⠻⠕**

### Paso 3: Generar PDF

1. Después de la transcripción, hacer clic en **"Generar Señalética PDF"**
2. El archivo se descargará automáticamente
3. Abrir el PDF y ¡está listo para imprimir!

---

## 🎯 Guía Detallada de Uso

### Pantalla Principal

Cuando abres la aplicación, verás:

```
┌─────────────────────────────────────────┐
│   🔤 Transcriptor Braille               │
│   Sistema de Generación de Señalética   │
├─────────────────────────────────────────┤
│                                         │
│  [  Área de Texto                  ]   │
│  [  para escribir tu texto         ]   │
│  [                                  ]   │
│                                         │
│  0 / 500 caracteres                    │
│                                         │
│  [Transcribir a Braille] [Limpiar]     │
│                                         │
└─────────────────────────────────────────┘
```

### Componentes de la Interfaz

#### 1. **Área de Texto (Campo de Entrada)**
- **Ubicación**: Parte superior central
- **Función**: Aquí escribes o pegas el texto a transcribir
- **Límite**: 500 caracteres
- **Contador**: Muestra cuántos caracteres has usado

**Ejemplo**:
```
Escribe aquí: "Salida de Emergencia Piso 3"
```

#### 2. **Botón "Transcribir a Braille"**
- **Apariencia**: Botón azul grande
- **Función**: Inicia el proceso de transcripción
- **Estado**: Se deshabilita mientras procesa (mostrará "Transcribiendo...")

#### 3. **Botón "Limpiar"**
- **Apariencia**: Botón gris
- **Función**: Borra el texto ingresado y oculta resultados
- **Uso**: Para empezar una nueva transcripción desde cero

#### 4. **Sección de Resultados** (aparece después de transcribir)
- Muestra tu texto original
- Muestra el texto en Braille
- Ofrece opciones para generar PDF o copiar

---

## 📝 Casos de Uso Comunes

### Caso 1: Señalética de Baños

**Objetivo**: Crear señal para puerta de baño

**Pasos**:
1. Escribir en el campo de texto:
   ```
   Baño
   ```

2. Clic en "Transcribir a Braille"

3. **Resultado mostrado**:
   ```
   Texto Original: Baño
   Texto en Braille: ⠃⠁⠻⠕
   ```

4. Clic en "Generar Señalética PDF"

5. Imprimir el PDF en papel adhesivo o cartón

**💡 Consejo**: Para mayor durabilidad, laminar la señal después de imprimir.

---

### Caso 2: Números de Piso en Ascensor

**Objetivo**: Crear señales numéricas para pisos

**Pasos**:
1. Escribir:
   ```
   Piso 1
   Piso 2
   Piso 3
   ```

2. Transcribir **cada uno por separado** (hacer 3 transcripciones)

3. **Resultados**:
   ```
   Piso 1 → ⠏⠊⠎⠕ ⠼⠁
   Piso 2 → ⠏⠊⠎⠕ ⠼⠃
   Piso 3 → ⠏⠊⠎⠕ ⠼⠉
   ```

4. Generar PDF para cada uno

**⚠️ Importante**: Los números en Braille llevan un símbolo especial (⠼) antes del número.

---

### Caso 3: Señalética con Acentos

**Objetivo**: Crear señal que incluye vocales acentuadas

**Pasos**:
1. Escribir:
   ```
   Información
   ```

2. Transcribir

3. **Resultado**:
   ```
   Texto Original: Información
   Texto en Braille: ⠊⠝⠋⠕⠗⠍⠁⠉⠌⠬⠝
                                     ↑   ↑
                            (í = ⠌) (ó = ⠬)
   ```

**✅ Ventaja**: El sistema maneja automáticamente todas las vocales acentuadas.

---

### Caso 4: Frases Completas con Puntuación

**Objetivo**: Crear señal con oración completa

**Pasos**:
1. Escribir:
   ```
   Salida de emergencia.
   ```

2. Transcribir

3. **Resultado**:
   ```
   Salida de emergencia. → ⠎⠁⠇⠊⠙⠁ ⠙⠑ ⠑⠍⠑⠗⠛⠑⠝⠉⠊⠁⠲
                                                              ↑
                                                       (punto = ⠲)
   ```

**📌 Signos soportados**: 
- Punto (.)
- Coma (,)
- Punto y coma (;)
- Dos puntos (:)
- Signos de interrogación (¿?)
- Signos de exclamación (¡!)
- Paréntesis (())

---

## 🎨 Generación de Señalética PDF

### ¿Qué incluye el PDF?

Cuando generas un PDF, obtienes:

1. **Texto en tinta** (texto original legible)
2. **Puntos Braille visuales** (círculos que representan los puntos)
3. **Formato profesional** listo para imprimir
4. **Alta calidad** (vectorial, no se pixela al ampliar)

### Proceso de Generación de PDF

```
1. Transcribir texto
   ↓
2. Clic en "Generar Señalética PDF"
   ↓
3. El navegador descarga automáticamente: senaletica_braille.pdf
   ↓
4. Abrir PDF con Adobe Reader, Foxit, o visor por defecto
   ↓
5. Imprimir en impresora común
```

### Recomendaciones de Impresión

#### Para Señalética Interior
- **Material**: Papel adhesivo mate 80-100g
- **Color**: Impresión en negro sobre fondo blanco/crema
- **Tamaño**: A4 o según necesidad
- **Acabado**: Laminado mate para mayor durabilidad

#### Para Señalética Exterior
- **Material**: Vinyl adhesivo o plástico rígido
- **Impresión**: En centro de impresión profesional
- **Protección**: UV-resistant coating

#### Para Práctica/Pruebas
- **Material**: Papel común 75g
- **Impresión**: Impresora de oficina estándar

---

## ⌨️ Funciones Adicionales

### Copiar Braille al Portapapeles

**Uso**: Para pegar el texto Braille en otro documento

**Pasos**:
1. Después de transcribir, localizar botón "📋 Copiar Braille"
2. Hacer clic
3. Aparecerá mensaje: "¡Texto Braille copiado!"
4. Pegar (Ctrl+V / Cmd+V) en cualquier aplicación

**Ejemplo de uso**: Copiar a documento de Word, email, etc.

---

### Validación de Caracteres

El sistema te avisa si intentas usar caracteres no soportados.

**Ejemplo**:

Si escribes:
```
info@empresa.com
```

Recibirás mensaje de error:
```
❌ Caracteres no soportados: @
```

**Solución**: Reescribir sin caracteres especiales:
```
info empresa.com
```

---

## 📊 Límites y Restricciones

| Aspecto | Límite | Notas |
|---------|--------|-------|
| **Caracteres por transcripción** | 500 | Para textos más largos, dividir en partes |
| **Tiempo de respuesta** | < 2 segundos | Generalmente instantáneo |
| **Tamaño de PDF** | ~500 KB | Depende de la longitud del texto |
| **Caracteres soportados** | Ver tabla abajo | Solo caracteres del español básico |

### Caracteres Soportados

#### ✅ Soportados
- **Letras**: a-z, ñ, w (minúsculas y mayúsculas)
- **Acentuadas**: á, é, í, ó, ú, ü
- **Números**: 0-9
- **Puntuación**: . , ; : ¿ ? ¡ ! ( ) -
- **Espacios**: Espacio en blanco normal

#### ❌ NO Soportados (actualmente)
- Símbolos: @ # $ % & * + = / \ | ~ ` ^ < >
- Emojis: 😊 🎉 ❤️
- Caracteres especiales de otros idiomas

---

## 💡 Consejos y Mejores Prácticas

### Para Obtener Mejores Resultados

✅ **SÍ HACER**:
- Usar texto claro y conciso
- Revisar ortografía antes de transcribir
- Las mayúsculas se preservan con el indicador ⠨ (v2.1.0+)
- Dividir textos largos en múltiples transcripciones
- Probar la transcripción antes de imprimir en masa

❌ **NO HACER**:
- No usar caracteres especiales no soportados
- No exceder 500 caracteres
- No confiar solo en el resultado visual (verificar con experto Braille si es para uso oficial)

### Revisión de Calidad

Antes de imprimir señalética oficial:

1. ✅ Revisar ortografía del texto original
2. ✅ Verificar que todos los caracteres se transcribieron
3. ✅ Imprimir una prueba en papel común
4. ✅ Si es posible, validar con persona que lee Braille
5. ✅ Verificar que el PDF se ve correcto

---

## 🎓 Entendiendo el Sistema Braille

### El Cuadratín Braille

El sistema Braille usa un "cuadratín" de 6 puntos:

```
1 • • 4
2 • • 5
3 • • 6
```

Cada letra es una combinación única de estos puntos.

### Ejemplo: La letra "A"

```
• •
2 • • 5
3 • • 6

La letra "a" solo usa el punto 1 → ⠁
```

### Las Tres Series del Alfabeto

#### Primera Serie (a-j)
Usa puntos: 1, 2, 4, 5
```
a=⠁  b=⠃  c=⠉  d=⠙  e=⠑  f=⠋  g=⠛  h=⠓  i=⠊  j=⠚
```

#### Segunda Serie (k-t)
Primera serie + punto 3
```
k=⠅  l=⠇  m=⠍  n=⠝  o=⠕  p=⠏  q=⠟  r=⠗  s=⠎  t=⠞
```

#### Tercera Serie (u-z)
Primera serie + puntos 3 y 6
```
u=⠥  v=⠧  x=⠭  y=⠽  z=⠵
```

### Números en Braille

Los números se forman con el **Signo de Número** (⠼) seguido de las letras a-j:

```
1 = ⠼⠁  (signo + a)
2 = ⠼⠃  (signo + b)
3 = ⠼⠉  (signo + c)
...
0 = ⠼⠚  (signo + j)
```

**Importante**: El signo de número solo se pone **una vez** al principio:
```
123 = ⠼⠁⠃⠉  (NO: ⠼⠁⠼⠃⠼⠉)
```

---

## ❓ Preguntas Frecuentes (FAQ)

### General

**P: ¿Es gratuita la aplicación?**  
R: Sí, es un proyecto de código abierto completamente gratuito.

**P: ¿Funciona sin conexión a internet?**  
R: Si la instalaste localmente, sí. Si accedes vía web, necesitas internet.

**P: ¿Puedo usarla en mi teléfono móvil?**  
R: Sí, la interfaz es responsive y funciona en móviles.

### Sobre la Transcripción

**P: ¿Cómo se representan las mayúsculas en Braille?**  
R: Desde la versión 2.1.0, el sistema implementa el indicador de mayúsculas (⠨ - puntos 4,6) según las reglas oficiales del Braille español. Cada letra mayúscula va precedida por este indicador. Por ejemplo: "Hola" → "⠨⠓⠕⠇⠁" y "HOLA" → "⠨⠓⠨⠕⠨⠇⠨⠁".

**P: ¿Puedo transcribir texto en inglés?**  
R: Algunos caracteres funcionarán, pero el sistema está optimizado para español. Caracteres exclusivos del inglés (como la 'w' en ciertas posiciones) pueden no transcribirse correctamente según el contexto.

**P: ¿Por qué aparece un símbolo antes de los números?**  
R: Es el "Signo de Número" (⠼) requerido por el sistema Braille para diferenciar números de letras.

### Sobre el PDF

**P: ¿El PDF es de alta calidad?**  
R: Sí, es formato vectorial (no se pixela) apto para impresión profesional.

**P: ¿Puedo editar el PDF generado?**  
R: Puedes abrirlo en editores de PDF, pero es más práctico re-generar si necesitas cambios.

**P: ¿El PDF incluye puntos en relieve?**  
R: No, incluye representación visual de los puntos. Para relieve, necesitarás una impresora Braille especializada o crear las marcas manualmente.

### Problemas Técnicos

**P: El botón "Transcribir" no funciona**  
R: 
1. Verifica que hay texto en el campo
2. Recarga la página (F5)
3. Verifica tu conexión a internet
4. Consulta la [sección de solución de problemas](#-solución-de-problemas-comunes)

**P: El PDF no se descarga**  
R:
1. Verifica configuración del navegador (permitir descargas)
2. Verifica espacio en disco
3. Intenta con otro navegador
4. Revisa el bloqueador de pop-ups

**P: Aparece un error al transcribir**  
R: Verifica que no estés usando caracteres no soportados (como @, #, $, etc.). El sistema te indicará qué caracteres causan problema.

---

## 🐛 Solución de Problemas Comunes

### Problema 1: "Caracteres no soportados"

**Síntoma**: Mensaje de error al transcribir

**Causa**: Usaste símbolos no soportados (@, #, $, etc.)

**Solución**:
1. Leer el mensaje de error (indica qué caracteres son)
2. Eliminar o reemplazar esos caracteres
3. Intentar nuevamente

**Ejemplo**:
```
❌ Error: "info@correo.com"
✅ Correcto: "info correo.com"
```

---

### Problema 2: Página no carga

**Síntoma**: Navegador muestra error "No se puede acceder"

**Solución**:
1. Verificar que el servidor está corriendo
2. Verificar la URL (debe ser http://localhost:5000)
3. Intentar con otro navegador
4. Contactar administrador del sistema

---

### Problema 3: PDF no abre

**Síntoma**: Error al abrir archivo descargado

**Solución**:
1. Instalar Adobe Reader o visor de PDF
2. Verificar que la descarga se completó (revisar tamaño del archivo)
3. Re-descargar el PDF
4. Intentar en otra computadora

---

### Problema 4: Texto muy largo

**Síntoma**: No puedo escribir más de 500 caracteres

**Solución**:
1. Dividir el texto en partes
2. Transcribir cada parte por separado
3. Generar múltiples PDFs

**Ejemplo**:
```
Texto largo (800 caracteres)
    ↓
Parte 1 (400 caracteres) → Transcribir → PDF 1
Parte 2 (400 caracteres) → Transcribir → PDF 2
```

---

## 📞 Soporte y Ayuda

### Recursos Adicionales

- **Manual de Instalación**: Para administradores del sistema
- **Documentación Técnica**: Para desarrolladores
- **Casos de Prueba**: Para verificar funcionamiento

### Reportar Problemas

Si encuentras un error o tienes una sugerencia:

1. **GitHub Issues**:
   - Ve a: https://github.com/DJoel07/Sistema-Transcripcion-Braille/issues
   - Clic en "New Issue"
   - Describe el problema con detalle

2. **Información a incluir**:
   - ¿Qué estabas intentando hacer?
   - ¿Qué esperabas que pasara?
   - ¿Qué pasó en realidad?
   - Captura de pantalla (si aplica)
   - Navegador y sistema operativo

### Contribuir

Este es un proyecto de código abierto. Si quieres contribuir:
- Reporta errores
- Sugiere mejoras
- Comparte el proyecto

---

## 📚 Glosario

**Braille**: Sistema de lectoescritura táctil para personas con discapacidad visual.

**Cuadratín**: Celda de 6 puntos que forma la base del sistema Braille.

**Signo de Número**: Símbolo especial (⠼) que indica que lo siguiente son números.

**PDF Vectorial**: Archivo que mantiene calidad al ampliar, ideal para impresión.

**Transcripción**: Proceso de convertir texto normal a Braille.

**Señalética**: Conjunto de señales o símbolos que informan o guían.

---

## 📖 Anexos

### Anexo A: Tabla Completa de Caracteres Braille

#### Alfabeto Básico
```
a=⠁  b=⠃  c=⠉  d=⠙  e=⠑  f=⠋  g=⠛  h=⠓  i=⠊  j=⠚
k=⠅  l=⠇  m=⠍  n=⠝  o=⠕  p=⠏  q=⠟  r=⠗  s=⠎  t=⠞
u=⠥  v=⠧  x=⠭  y=⠽  z=⠵
```

#### Letras Adicionales
```
ñ=⠻  w=⠺
```

#### Vocales Acentuadas
```
á=⠷  é=⠮  í=⠌  ó=⠬  ú=⠾  ü=⠳
```

#### Números (con signo ⠼)
```
1=⠼⠁  2=⠼⠃  3=⠼⠉  4=⠼⠙  5=⠼⠑
6=⠼⠋  7=⠼⠛  8=⠼⠓  9=⠼⠊  0=⠼⠚
```

#### Puntuación
```
.=⠲  ,=⠂  ;=⠆  :=⠒  
¿=⠢  ?=⠦  ¡=⠖  !=⠖  
(=⠐⠣  )=⠐⠜  -=⠤
```

### Anexo B: Ejemplos de Señalética Común

| Texto Original | Transcripción Braille | Uso |
|----------------|----------------------|-----|
| Entrada | ⠑⠝⠞⠗⠁⠙⠁ | Puertas |
| Salida | ⠎⠁⠇⠊⠙⠁ | Puertas |
| Baño | ⠃⠁⠻⠕ | Sanitarios |
| Hombres | ⠓⠕⠍⠃⠗⠑⠎ | Sanitarios |
| Mujeres | ⠍⠥⠚⠑⠗⠑⠎ | Sanitarios |
| Piso 1 | ⠏⠊⠎⠕ ⠼⠁ | Ascensores |
| Emergencia | ⠑⠍⠑⠗⠛⠑⠝⠉⠊⠁ | Salidas |
| Información | ⠊⠝⠋⠕⠗⠍⠁⠉⠌⠬⠝ | Oficinas |

---

## 🎬 Tutorial en Video (Paso a Paso)

### Video 1: Tu Primera Transcripción (2 minutos)

**Minuto 0:00-0:30** - Acceder a la aplicación  
**Minuto 0:30-1:00** - Escribir texto simple  
**Minuto 1:00-1:30** - Transcribir a Braille  
**Minuto 1:30-2:00** - Generar y descargar PDF

*Nota: Los videos están disponibles en el repositorio GitHub en la carpeta `/docs/videos/`*

### Video 2: Casos de Uso Avanzados (5 minutos)

**Minuto 0:00-1:00** - Números y signos de puntuación  
**Minuto 1:00-2:00** - Vocales acentuadas  
**Minuto 2:00-3:00** - Frases completas con puntuación  
**Minuto 3:00-4:00** - Validación de caracteres  
**Minuto 4:00-5:00** - Tips de impresión

---

## 🖼️ Galería de Capturas de Pantalla

### Interfaz Principal

<img width="1902" height="915" alt="image" src="https://github.com/user-attachments/assets/0f56fcf7-a1ce-48d0-b770-f1afc0026093" />
*Figura 1: Vista principal de la aplicación con campo de entrada*

### Proceso de Transcripción

<img width="1115" height="896" alt="image" src="https://github.com/user-attachments/assets/c95c3dc4-b6b1-4fa2-8b5f-fbe8eda519be" />
*Figura 2: Aplicación procesando texto ingresado*

### Resultado de Transcripción

<img width="1127" height="443" alt="image" src="https://github.com/user-attachments/assets/eec39f48-e1a9-4740-9390-45f48ccbce2e" />
*Figura 3: Texto original y transcripción Braille mostrados*


### Ejemplos de Señalética Impresa

<img width="880" height="204" alt="image" src="https://github.com/user-attachments/assets/6b5921c8-a713-4fbb-8278-8943047bd7c0" />
*Figura 4: Ejemplos de señalética impresa y aplicada*

---

## 🎯 Casos de Uso Detallados

### Caso 5: Señalética para Ascensores (Completo)

**Escenario**: Edificio de oficinas de 5 pisos necesita señalética Braille en ascensores

**Materiales Necesarios**:
- Papel adhesivo mate
- Impresora láser o inkjet
- Laminadora (opcional)
- Tijeras o cutter
- Cinta métrica

**Proceso Completo**:

#### Paso 1: Planificación
```
Pisos a señalizar: P, 1, 2, 3, 4, 5
Textos requeridos:
- "Planta Baja"
- "Piso 1"
- "Piso 2"
- "Piso 3"
- "Piso 4"
- "Piso 5"
```

#### Paso 2: Transcripción

Transcribir cada texto:

| Texto Original | Braille | Notas |
|----------------|---------|-------|
| Planta Baja | ⠏⠇⠁⠝⠞⠁ ⠃⠁⠚⠁ | Sin número |
| Piso 1 | ⠏⠊⠎⠕ ⠼⠁ | Número con signo ⠼ |
| Piso 2 | ⠏⠊⠎⠕ ⠼⠃ | Número 2 = b |
| Piso 3 | ⠏⠊⠎⠕ ⠼⠉ | Número 3 = c |
| Piso 4 | ⠏⠊⠎⠕ ⠼⠙ | Número 4 = d |
| Piso 5 | ⠏⠊⠎⠕ ⠼⠑ | Número 5 = e |

#### Paso 3: Generación de PDFs

1. Para cada piso, hacer:
   - Transcribir texto
   - Generar PDF
   - Descargar y nombrar: `piso_1.pdf`, `piso_2.pdf`, etc.

#### Paso 4: Impresión

**Configuración de Impresora**:
```
Tamaño papel: A4
Orientación: Vertical
Calidad: Alta (1200 dpi mínimo)
Tipo papel: Adhesivo mate
Color: Negro sobre fondo blanco
```

#### Paso 5: Corte y Acabado

1. Imprimir todos los PDFs
2. Esperar 2 minutos (secar tinta)
3. Laminar cada etiqueta (opcional)
4. Cortar con margen de 5mm
5. Redondear esquinas (opcional)

#### Paso 6: Instalación

1. Limpiar superficie con alcohol
2. Medir y marcar posición (altura estándar: 1.20m)
3. Retirar papel protector del adhesivo
4. Aplicar de arriba hacia abajo evitando burbujas
5. Presionar firmemente con paño suave

**Tiempo Estimado Total**: 2-3 horas para 6 señales

---

### Caso 6: Menú de Restaurante Inclusivo

**Objetivo**: Crear secciones de menú con nombres en Braille

**Categorías a transcribir**:
```
1. Entradas → ⠑⠝⠞⠗⠁⠙⠁⠎
2. Platos Fuertes → ⠏⠇⠁⠞⠕⠎ ⠋⠥⠑⠗⠞⠑⠎
3. Postres → ⠏⠕⠎⠞⠗⠑⠎
4. Bebidas → ⠃⠑⠃⠊⠙⠁⠎
```

**Implementación**:

1. **Transcribir cada categoría** por separado
2. **Generar PDF** para cada una
3. **Imprimir en cartulina** (más resistente que papel)
4. **Ubicación sugerida**:
   - Inicio de cada sección del menú
   - Altura: 10cm del borde superior de la mesa
   - Esquina superior izquierda de cada página

**Beneficio**: Clientes con discapacidad visual pueden navegar el menú de forma independiente

---

### Caso 7: Etiquetas para Medicamentos

**Advertencia Legal**: Este ejemplo es informativo. Para uso médico oficial, consultar con especialistas certificados.

**Escenario**: Etiquetar frascos de medicamentos en casa

**Información a incluir**:
```
Ejemplo 1: "Ibuprofeno 600mg"
Transcripción: ⠊⠃⠥⠏⠗⠕⠋⠑⠝⠕ ⠼⠋⠚⠚⠍⠛

Ejemplo 2: "Tomar cada 8 horas"
Transcripción: ⠞⠕⠍⠁⠗ ⠉⠁⠙⠁ ⠼⠓ ⠓⠕⠗⠁⠎
```

**Proceso**:

1. Transcribir nombre del medicamento
2. Transcribir dosis en línea separada
3. Generar PDF
4. Imprimir en papel adhesivo resistente al agua
5. Aplicar en frasco limpio y seco

**Tips de Seguridad**:
- ✅ Incluir fecha de vencimiento
- ✅ Usar mayúsculas para medicamentos críticos
- ✅ Revisar transcripción dos veces
- ✅ Validar con farmacéutico si es posible

---

## 🔍 Análisis de Errores Comunes

### Error 1: Confusión entre Letras Similares

**Problema**: Letras que se parecen visualmente

| Par Confuso | Braille | Diferencia |
|-------------|---------|------------|
| d vs f | ⠙ vs ⠋ | d=1-4-5, f=1-2-4 |
| h vs j | ⠓ vs ⠚ | h=1-2-5, j=2-4-5 |
| e vs i | ⠑ vs ⠊ | e=1-5, i=2-4 |

**Solución**: Siempre revisar el resultado cuidadosamente, letra por letra.

---

### Error 2: Olvidar el Signo de Número

**Incorrecto**:
```
"Piso 3" → ⠏⠊⠎⠕ ⠉  ❌
```

**Correcto**:
```
"Piso 3" → ⠏⠊⠎⠕ ⠼⠉  ✅
           (signo de número antes del 3)
```

**Prevención**: El sistema agrega automáticamente el signo de número. Solo verifica visualmente que esté presente.

---

### Error 3: Espacios Incorrectos

**Incorrecto**:
```
"Piso   3" (3 espacios)
```

**Sistema corrige automáticamente**:
```
"Piso 3" (1 espacio)
```

**Nota**: El sistema normaliza múltiples espacios a uno solo automáticamente.

---

### Error 4: Uso de Mayúsculas

**Entrada correcta**:
```
"Salida de Emergencia"
```

**Resultado (v2.1.0+)**:
```
⠨⠎⠁⠇⠊⠙⠁ ⠙⠑ ⠨⠑⠍⠑⠗⠛⠑⠝⠉⠊⠁
```

**Nota**: Desde v2.1.0, el sistema preserva las mayúsculas usando el indicador ⠨ (puntos 4,6). Cada letra mayúscula va precedida por este símbolo según las reglas oficiales del Braille español.

---

## 📐 Especificaciones Técnicas de Impresión

### Dimensiones Recomendadas

#### Señalética Pequeña (Placas de Puerta)
```
Ancho: 10cm
Alto: 5cm
Margen: 0.5cm en todos los lados
Tamaño de fuente (tinta): 14pt
Tamaño de puntos Braille: 2mm diámetro
```

#### Señalética Mediana (Ascensores, Pasillos)
```
Ancho: 15cm
Alto: 8cm
Margen: 1cm en todos los lados
Tamaño de fuente (tinta): 18pt
Tamaño de puntos Braille: 2.5mm diámetro
```

#### Señalética Grande (Exteriores, Entradas)
```
Ancho: 20cm o más
Alto: 10cm o más
Margen: 1.5cm en todos los lados
Tamaño de fuente (tinta): 24pt
Tamaño de puntos Braille: 3mm diámetro
```

### Separación entre Celdas Braille

**Estándar Internacional**:
- Horizontal: 2.5mm entre centros
- Vertical: 2.5mm entre centros
- Entre palabras: Espacio de una celda vacía

### Materiales Recomendados por Uso

| Ubicación | Material | Vida Útil | Costo |
|-----------|----------|-----------|-------|
| **Interior (oficina)** | Papel adhesivo mate 80g | 1-2 años | Bajo |
| **Interior (tráfico alto)** | Vinyl autoadhesivo | 3-5 años | Medio |
| **Exterior protegido** | Aluminum adhesivo | 5-7 años | Alto |
| **Exterior expuesto** | Acero inoxidable grabado | 10+ años | Muy Alto |
| **Temporal** | Papel común con cinta | Días-semanas | Muy Bajo |

---

## 🎨 Personalización del PDF

### Modificar Colores (Para Desarrolladores)

Si tienes acceso al código fuente, puedes personalizar los colores del PDF editando `src/services/pdf_generator.py`:

```python
# Colores actuales (negro sobre blanco)
punto_color = colors.black
fondo_color = colors.white
texto_color = colors.black

# Cambiar a colores personalizados (ejemplo: azul)
punto_color = colors.Color(0, 0.2, 0.5)  # Azul oscuro
texto_color = colors.Color(0, 0.2, 0.5)
```

### Agregar Logo o Marca

Para agregar un logo corporativo al PDF:

```python
# En pdf_generator.py
from reportlab.lib.utils import ImageReader

# Agregar imagen
logo = ImageReader('ruta/a/logo.png')
c.drawImage(logo, x=450, y=750, width=50, height=50)
```

**Nota**: Estas modificaciones requieren conocimientos de programación en Python.

---

## 🌍 Cumplimiento de Normativas

### Estándares de Accesibilidad

La aplicación ayuda a cumplir con:

#### Normativa Internacional
- **ISO 24751**: Tecnología de información - Individualized adaptability
- **WCAG 2.1**: Web Content Accessibility Guidelines
- **ADA** (Americans with Disabilities Act): Señalética Braille requerida

#### Normativa España
- **UNE 41500**: Accesibilidad en la edificación
- **Real Decreto 1/2013**: Derechos de personas con discapacidad

#### Normativa México
- **NOM-034-SSA3-2013**: Accesibilidad de las personas con discapacidad

#### Normativa Argentina
- **Ley 26.653**: Accesibilidad de la información en páginas web

### Requisitos Específicos para Señalética

Según ADA y normativas similares:

1. **Altura de instalación**: 120-150cm del suelo
2. **Contraste**: Mínimo 70% entre fondo y texto
3. **Tamaño de puntos**: 2-3mm de diámetro
4. **Ubicación**: Al lado de la manija (lado de la bisagra)
5. **Acabado**: Superficie mate (no brillante)

---

## 🔒 Privacidad y Datos

### Política de Privacidad

**¿Qué datos recopila la aplicación?**

✅ **NINGUNO**

- No se almacena el texto que transcribes
- No se recopilan datos personales
- No se usan cookies de seguimiento
- No se envían datos a servidores externos

**Procesamiento Local**:
- Toda la transcripción ocurre en tu navegador o servidor local
- Los PDFs se generan en tu computadora
- No hay almacenamiento en la nube (a menos que tú lo configures)

### Seguridad

```
Tu Texto → Tu Navegador → Servidor Local → Tu PDF
          ↑                                  ↓
          └──────── Todo local ──────────────┘
```

---

## 📞 Soporte Técnico Avanzado

### Soporte por Niveles

#### Nivel 1: Auto-ayuda
- Revisar este manual
- Consultar FAQ
- Ver tutoriales en video

#### Nivel 2: Comunidad
- Buscar en GitHub Issues
- Preguntar en Discussions
- Revisar casos similares

#### Nivel 3: Soporte Directo
- Crear Issue en GitHub con etiqueta `bug` o `help wanted`
- Incluir información detallada:
  - Sistema operativo y versión
  - Navegador y versión
  - Pasos exactos para reproducir
  - Capturas de pantalla
  - Logs (si están disponibles)

### Template para Reportar Bug

```markdown
**Descripción del problema:**
[Describir qué salió mal]

**Pasos para reproducir:**
1. Ir a...
2. Hacer clic en...
3. Escribir...
4. Ver error

**Comportamiento esperado:**
[Qué debería haber pasado]

**Comportamiento actual:**
[Qué pasó en realidad]

**Capturas de pantalla:**
[Si aplica]

**Entorno:**
- SO: Windows 11 / Ubuntu 22.04 / macOS 13
- Navegador: Chrome 119 / Firefox 121 / Safari 17
- Versión de la app: [ver en pie de página]

**Información adicional:**
[Cualquier contexto relevante]
```

---

## 🎓 Recursos de Aprendizaje

### Aprender Más Sobre Braille

#### Libros Recomendados
- "El Sistema Braille: Historia y Desarrollo" - UNESCO
- "Manual de Braille Español" - ONCE

#### Cursos Online
- Coursera: "Accessible Design" (gratuito con certificado opcional)
- edX: "Introduction to Braille"

#### Videos Educativos
- Canal YouTube: ONCE Discapacidad Visual
- TED Talks sobre accesibilidad

### Proyectos Relacionados

- **Liblouis**: Motor de traducción Braille open source
- **NVDA**: Lector de pantalla gratuito
- **Braille ASCII**: Estándar para representar Braille en texto

### Contribuir al Proyecto

¿Quieres mejorar esta aplicación?

1. **Reportar bugs**: GitHub Issues
2. **Sugerir features**: GitHub Discussions
3. **Contribuir código**: Pull Requests
4. **Mejorar documentación**: Editar archivos .md
5. **Compartir casos de uso**: Inspira a otros usuarios

---

## 📱 Uso en Dispositivos Móviles

### Acceso desde Smartphone

La aplicación es completamente responsive y funciona en móviles.

**Navegadores Recomendados**:
- ✅ Chrome (Android)
- ✅ Safari (iOS)
- ✅ Firefox (Android)
- ✅ Edge (Android/iOS)

### Tips para Móviles

1. **Orientación**: Usar en vertical para mejor experiencia
2. **Teclado**: Usar teclado por defecto (no autocorrector)
3. **PDFs**: Se descargan a carpeta "Descargas"
4. **Compartir**: Usar botón "Compartir" del navegador

### Limitaciones Móviles

- Editar PDF más difícil (usar computadora)
- Impresión directa limitada (transferir a PC)
- Pantalla pequeña para visualizar resultados largos

---

## 🎁 Extras y Funciones Ocultas

### Atajos de Teclado

| Atajo | Acción |
|-------|--------|
| `Ctrl + Enter` | Transcribir texto |
| `Ctrl + L` | Limpiar campos |
| `Ctrl + S` | Descargar PDF |
| `Ctrl + C` | Copiar resultado |
| `Esc` | Cerrar mensajes |

### Funciones Beta

Funciones experimentales (pueden cambiar):

- **Modo oscuro**: Agregando próximamente
- **Historial de transcripciones**: En desarrollo
- **Export a múltiples formatos**: Planificado (SVG, PNG)
- **API REST**: Para integraciones (documentación próxima)

---

**Última actualización**: 2025-11-25  
**Versión**: 2.0  
**Autor**: Equipo de Desarrollo  
**Proyecto**: Sistema de Transcripción Braille
