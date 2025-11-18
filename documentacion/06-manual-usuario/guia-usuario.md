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
- Usar mayúsculas solo al inicio (se normalizan automáticamente)
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

**P: ¿Por qué mis mayúsculas se convierten a minúsculas?**  
R: En Braille español básico, las mayúsculas y minúsculas no se diferencian en este nivel. Para mayúsculas se usaría un signo especial (no implementado en v1.0).

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

**Última actualización**: 2025-11-17  
**Versión**: 1.0  
**Autor**: Equipo de Desarrollo  
**Proyecto**: Sistema de Transcripción Braille

---

¡Gracias por usar nuestro sistema! Tu contribución a la accesibilidad es invaluable. 🌟
