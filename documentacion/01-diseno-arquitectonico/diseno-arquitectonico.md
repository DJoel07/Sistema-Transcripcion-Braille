# 📐 Diseño Arquitectónico de Alto Nivel - Sistema de Transcripción Braille

## 📋 Tabla de Contenidos
1. [Detalles y Requerimientos del Proyecto](#detalles-y-requerimientos)
2. [Especificación de Requisitos (SRS)](#especificación-de-requisitos)
3. [Arquitectura del Sistema](#arquitectura-del-sistema)
4. [Casos de Uso](#casos-de-uso)
5. [Historias de Usuario](#historias-de-usuario)

---

## 1. Detalles y Requerimientos del Proyecto {#detalles-y-requerimientos}

### I. Objetivo, Producto y Alcance

* **Objetivo General:** Desarrollar un producto de software que genere textos en el sistema de lectoescritura Braille.
* **Producto:** Un software que permite transcribir textos a Braille y viceversa.
* **Finalidad:** Que personas sin discapacidad puedan producir a bajo costo señalética o rotulación Braille para mejorar la accesibilidad.
* **Alcance (Bimestre 1):** Transcribir textos de español a Braille, incluyendo números, abecedario, vocales acentuadas y signos básicos.

### II. Requisitos Funcionales Detallados (Bimestre 1)

#### 1. Mapeo de Alfabeto y Acentuadas

El sistema debe implementar la lógica del Símbolo Generador (Cuadratín) de seis puntos.

* **Primera Serie (a a j):** Mapeo de la primera serie matriz.
    * *Ejemplos:* a (1), b (12), j (245).
* **Segunda Serie (k a t):** Resulta de añadir el punto 3 a la Primera Serie.
    * *Ejemplos:* k (13), o (135).
* **Tercera Serie (u, v, x, y, z):** Resulta de añadir los puntos 3 y 6 a la Primera Serie.
    * *Ejemplos:* u (136), z (1356).
* **Letras Adicionales:** Implementar mapeo de ñ y w.
* **Vocales Acentuadas:** Implementar mapeo de á, é, í, ó, ú, ü.

#### 2. Mapeo de Números

* Los dígitos (1-0) se obtienen anteponiendo el **Signo de Número** al patrón de la Primera Serie (a-j).
* El Signo de Número se coloca solamente al principio para cantidades de dos o más cifras.
* Los números se deben separar con espacios en blanco.

#### 3. Mapeo de Signos Básicos

* El sistema debe soportar la transcripción de signos como la coma, punto, punto y coma, dos puntos, signos de interrogación (¿?, ¡!) y paréntesis (()).

#### 4. Generación de Señalética (Output)

* El software debe generar una representación de la señalética Braille a partir de textos.
* **Implementación:** Utilizar librerías de Python (ReportLab para PDF) para generar un archivo de diseño vectorial de alta calidad, apto para impresión, que represente los puntos Braille en relieve junto al texto en tinta.

---

## 2. Especificación de Requisitos de Software (SRS) {#especificación-de-requisitos}

### 2.1 Requisitos Funcionales (RF)

| ID | Nombre del Requisito | Descripción Detallada | Fuentes del Sistema |
| :--- | :--- | :--- | :--- |
| **RF-001** | Transcribir Texto a Braille | El sistema debe tomar una cadena de texto en español y convertirla a su representación Braille, respetando los mapeos de las tres series del alfabeto, acentuadas y letras adicionales. | Texto de entrada |
| **RF-002** | Manejar Números | El sistema debe transcribir dígitos del 0 al 9. Debe anteponer el **Signo de Número** al primer dígito de una cantidad y separarlos con espacios. | Texto de entrada |
| **RF-003** | Manejar Signos Básicos | El sistema debe incluir la transcripción de signos básicos, como puntos, comas, y otros signos del Braille Español. | Texto de entrada |
| **RF-004** | Generar Señalética | El sistema debe generar una salida visualmente representable y apta para impresión (PDF) del texto transcrito en formato Braille para la creación de señalética. | Texto Braille |
| **RF-005** | Visualizar Cuadratín | El sistema debe mostrar el Símbolo Generador (Cuadratín) para ilustrar la posición de los seis puntos (1-6). | Interfaz de usuario |

### 2.2 Requisitos No Funcionales (RNF)

| ID | Categoría | Descripción Detallada |
| :--- | :--- | :--- |
| **RNF-001** | Usabilidad | La interfaz de usuario debe ser **intuitiva** y **fácil de usar** para personas sin discapacidad que buscan producir rotulación Braille. |
| **RNF-002** | Rendimiento | El tiempo de respuesta para la transcripción de un párrafo corto no debe exceder 2 segundos. |
| **RNF-003** | Escalabilidad | La arquitectura (Python/Flask) debe permitir futuras ampliaciones (Bimestre 2), como la transcripción inversa (Braille a texto). |
| **RNF-004** | Mantenibilidad | El código fuente debe ser modular, organizado y documentado con *docstrings* (documentación técnica) para permitir su fácil mantenimiento y evolución. |
| **RNF-005** | Documentación | El proyecto debe cumplir estrictamente con los requisitos de documentación en la rama `documentacion` de GitHub. |

---

## 3. Arquitectura del Sistema {#arquitectura-del-sistema}

### 3.1 Arquitectura de Tres Capas (3-Tier Architecture)

Arquitectura ideal para aplicaciones web robustas que mantiene la separación de responsabilidades (*Separation of Concerns*).

| Capa | Componente Principal | Tecnologías | Responsabilidad |
| :--- | :--- | :--- | :--- |
| **1. Capa de Presentación (Frontend)** | Interfaz de Usuario (UI) | HTML, CSS, JavaScript | Maneja la entrada del usuario (texto a transcribir) y presenta los resultados de la transcripción y las opciones de descarga de señalética. |
| **2. Capa de Lógica de Negocio (Backend/Flask Core)** | Servidor de Aplicaciones (Flask) | Python, Flask | Contiene la lógica central del proyecto: **la transcripción de español a Braille y la lógica de generación de archivos de señalética**. |
| **3. Capa de Datos (Data/Persistencia)** | Almacenamiento de Mapeos | Archivos de Configuración (`.json`, `.py`) o Bases de Datos (SQLite/PostgreSQL) | Almacena de manera estructurada los mapeos Braille (abecedario, números, signos), permitiendo una fácil actualización y consulta. |

### 3.2 Diagrama Conceptual de Flujo

```
┌──────────────────────────────────────────────────────────────┐
│                    USUARIO                                    │
└────────────────────┬─────────────────────────────────────────┘
                     │ Introduce texto
                     ▼
┌──────────────────────────────────────────────────────────────┐
│         CAPA DE PRESENTACIÓN (Frontend)                      │
│  - Formulario de entrada                                     │
│  - Visualización de resultados                               │
│  - Botón de descarga PDF                                     │
└────────────────────┬─────────────────────────────────────────┘
                     │ HTTP Request
                     ▼
┌──────────────────────────────────────────────────────────────┐
│    CAPA DE LÓGICA DE NEGOCIO (Flask Backend)                │
│  ┌────────────────────────────────────────────────┐         │
│  │  1. Recibe texto del usuario                   │         │
│  │  2. Valida entrada                             │         │
│  │  3. Consulta mapeos Braille ────────┐          │         │
│  │  4. Aplica reglas de transcripción  │          │         │
│  │  5. Genera PDF (si se solicita)     │          │         │
│  │  6. Retorna resultado               │          │         │
│  └────────────────────────────────────┬┘          │         │
└───────────────────────────────────────┼───────────┘         │
                                        │                      │
                                        ▼                      │
┌──────────────────────────────────────────────────────────────┐
│           CAPA DE DATOS (Persistencia)                       │
│  - Mapeos del alfabeto Braille (a-z, ñ, w)                  │
│  - Mapeos de vocales acentuadas (á, é, í, ó, ú, ü)         │
│  - Mapeos de números (0-9 + signo de número)                │
│  - Mapeos de signos de puntuación                           │
│  - Configuración del sistema                                 │
└──────────────────────────────────────────────────────────────┘
```

### 3.3 Estructura de Módulos del Proyecto

```
src/
├── core/                      # Lógica de negocio principal
│   ├── transcription_engine.py   # Motor de transcripción
│   └── braille_mappings.py       # Mapeos Braille
│
├── services/                  # Servicios de aplicación
│   ├── transcription_service.py  # Servicio de transcripción
│   └── pdf_generator.py          # Generador de PDF
│
├── web/                       # Capa de presentación
│   ├── routes.py                 # Rutas Flask
│   ├── templates/                # Plantillas HTML
│   │   └── index.html
│   └── static/                   # CSS, JS, imágenes
│       ├── css/
│       ├── js/
│       └── img/
│
└── utils/                     # Utilidades
    └── validators.py             # Validadores
```

### 3.4 Flujo de Datos Detallado

1. El **Usuario** introduce un texto y presiona "Transcribir" en la **Capa de Presentación**.
2. La **Capa de Lógica de Negocio (Flask)** recibe el texto vía HTTP POST.
3. El sistema **valida** el texto (longitud, caracteres soportados).
4. La **Capa de Lógica de Negocio** consulta la **Capa de Datos** para obtener las reglas de mapeo Braille.
5. El **Motor de Transcripción** aplica las reglas:
   - Normaliza el texto (minúsculas, espacios)
   - Procesa letra por letra aplicando mapeos
   - Maneja números con signo de número
   - Procesa signos de puntuación
6. Si se solicita **Señalética**, el **Generador de PDF** crea el documento usando ReportLab.
7. La **Capa de Lógica de Negocio** devuelve:
   - Texto Braille transcrito (para visualización web)
   - Archivo PDF (para descarga)
8. La **Capa de Presentación** muestra el resultado al usuario.

---

## 4. Casos de Uso {#casos-de-uso}

### 4.1 Diagrama de Casos de Uso

```
┌─────────────────────────────────────────────────────────┐
│                                                          │
│                  Sistema de Transcripción                │
│                        Braille                           │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │  CU-001: Transcribir Texto Simple              │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │  CU-002: Transcribir Texto con Números         │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │  CU-003: Generar Archivo de Señalética         │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │  CU-004: Gestión de Errores                    │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
                        ▲
                        │
                   ┌────┴────┐
                   │ Usuario │
                   └─────────┘
```

### 4.2 Especificación de Casos de Uso

#### CU-001: Transcribir Texto Simple

| Atributo | Descripción |
|----------|-------------|
| **ID** | CU-001 |
| **Nombre** | Transcribir Texto Simple |
| **Actores** | Usuario |
| **Descripción** | El Usuario ingresa texto sin números ni signos. El sistema aplica las reglas del alfabeto Braille y muestra el resultado. |
| **Precondiciones** | - El sistema está activo<br>- El usuario accede a la interfaz web |
| **Flujo Principal** | 1. El usuario introduce texto en el campo de entrada<br>2. El usuario presiona el botón "Transcribir"<br>3. El sistema valida que el texto contiene solo letras<br>4. El sistema aplica las reglas de mapeo Braille<br>5. El sistema muestra el resultado transcrito |
| **Postcondiciones** | - El texto Braille se muestra en pantalla<br>- El usuario puede copiar o generar PDF |
| **Flujos Alternativos** | 3a. Si el texto está vacío, el sistema muestra un mensaje de error |

#### CU-002: Transcribir Texto con Números

| Atributo | Descripción |
|----------|-------------|
| **ID** | CU-002 |
| **Nombre** | Transcribir Texto con Números |
| **Actores** | Usuario |
| **Descripción** | El Usuario ingresa una cadena que contiene números (ej. "Piso 5"). El sistema aplica la regla del Signo de Número. |
| **Precondiciones** | - El sistema está activo<br>- El usuario accede a la interfaz web |
| **Flujo Principal** | 1. El usuario introduce texto con números<br>2. El usuario presiona "Transcribir"<br>3. El sistema detecta números en el texto<br>4. El sistema antepone el Signo de Número<br>5. El sistema aplica mapeo numérico<br>6. El sistema muestra el resultado |
| **Postcondiciones** | - El texto Braille incluye números correctamente formateados |
| **Flujos Alternativos** | - |

#### CU-003: Generar Archivo de Señalética

| Atributo | Descripción |
|----------|-------------|
| **ID** | CU-003 |
| **Nombre** | Generar Archivo de Señalética |
| **Actores** | Usuario |
| **Descripción** | El Usuario revisa la transcripción y selecciona la opción para generar el documento imprimible. El sistema crea y ofrece la descarga del archivo vectorial (PDF). |
| **Precondiciones** | - El texto ha sido transcrito exitosamente |
| **Flujo Principal** | 1. El usuario revisa la transcripción en pantalla<br>2. El usuario hace clic en "Generar PDF"<br>3. El sistema crea el PDF con ReportLab<br>4. El sistema ofrece la descarga del archivo<br>5. El usuario descarga el archivo |
| **Postcondiciones** | - El archivo PDF se descarga en el dispositivo del usuario<br>- El PDF contiene texto Braille y texto original |
| **Flujos Alternativos** | 3a. Si hay error al generar PDF, mostrar mensaje de error |

#### CU-004: Gestión de Errores

| Atributo | Descripción |
|----------|-------------|
| **ID** | CU-004 |
| **Nombre** | Gestión de Errores |
| **Actores** | Usuario, Sistema |
| **Descripción** | El Usuario introduce caracteres no soportados o no definidos para el alcance del Bimestre 1. El sistema informa al usuario que el carácter no puede ser transcrito. |
| **Precondiciones** | - El sistema está activo |
| **Flujo Principal** | 1. El usuario introduce texto con caracteres no soportados<br>2. El usuario presiona "Transcribir"<br>3. El sistema valida el texto<br>4. El sistema detecta caracteres no soportados<br>5. El sistema muestra mensaje de error descriptivo<br>6. El sistema indica qué caracteres no son soportados |
| **Postcondiciones** | - El usuario es informado del problema<br>- No se realiza la transcripción |
| **Flujos Alternativos** | - |

---

## 5. Historias de Usuario {#historias-de-usuario}

### 5.1 Especificación de Historias de Usuario

#### HU-001: Transcripción Completa del Alfabeto

| Atributo | Detalle |
|----------|---------|
| **ID** | HU-001 |
| **Como** | Usuario Proponente |
| **Quiero** | Introducir un texto en español |
| **Para** | Que el sistema me devuelva la transcripción completa en Braille |
| **Criterios de Aceptación** | ✅ El sistema transcribe correctamente **todas las letras** (a-z, ñ, w, acentuadas) según las reglas de las series.<br>✅ La transcripción respeta el mapeo de las tres series<br>✅ Las vocales acentuadas (á, é, í, ó, ú, ü) se transcriben correctamente<br>✅ El resultado se muestra inmediatamente |
| **Prioridad** | 🔴 Alta |
| **Estimación** | 5 puntos |

#### HU-002: Transcripción de Números

| Atributo | Detalle |
|----------|---------|
| **ID** | HU-002 |
| **Como** | Usuario Proponente |
| **Quiero** | Transcribir números |
| **Para** | Poder producir señalética de conteo (ej. ascensores) |
| **Criterios de Aceptación** | ✅ El sistema coloca el **Signo de Número** correctamente<br>✅ Respeta el mapeo numérico de la primera serie<br>✅ Para cantidades de 2+ cifras, solo un signo al inicio<br>✅ Los números se separan con espacios |
| **Prioridad** | 🔴 Alta |
| **Estimación** | 3 puntos |

#### HU-003: Transcripción de Signos de Puntuación

| Atributo | Detalle |
|----------|---------|
| **ID** | HU-003 |
| **Como** | Usuario Proponente |
| **Quiero** | Que se incluyan los signos de puntuación básicos |
| **Para** | Que la señalética sea gramaticalmente correcta |
| **Criterios de Aceptación** | ✅ Los signos de puntuación (coma, punto, punto y coma, dos puntos) se transcriben correctamente<br>✅ Los signos de interrogación y exclamación (¿?, ¡!) se transcriben correctamente<br>✅ Los paréntesis se transcriben correctamente<br>✅ Sigue las reglas del Braille Español |
| **Prioridad** | 🟡 Media |
| **Estimación** | 3 puntos |

#### HU-004: Generación de Archivo Imprimible

| Atributo | Detalle |
|----------|---------|
| **ID** | HU-004 |
| **Como** | Usuario Proponente |
| **Quiero** | Generar un archivo listo para imprimir (PDF) |
| **Para** | Producir la señalética con el texto Braille y el texto en tinta |
| **Criterios de Aceptación** | ✅ Al hacer clic en "Generar PDF", se descarga un archivo<br>✅ El archivo es de alta calidad (vectorial)<br>✅ Contiene la transcripción Braille<br>✅ Contiene el texto original en tinta<br>✅ El formato es apto para impresión |
| **Prioridad** | 🔴 Alta |
| **Estimación** | 5 puntos |

### 5.2 Backlog Priorizado

| Prioridad | Historia | Estimación | Sprint |
|-----------|----------|------------|--------|
| 🔴 Alta | HU-001: Transcripción alfabeto | 5 puntos | Sprint 1 |
| 🔴 Alta | HU-002: Transcripción números | 3 puntos | Sprint 1 |
| 🔴 Alta | HU-004: Generación de PDF | 5 puntos | Sprint 2 |
| 🟡 Media | HU-003: Signos de puntuación | 3 puntos | Sprint 2 |

---

## 📚 Referencias y Documentación Adicional

- **Diagramas PlantUML**: Ver [diagramas/DiseñoAN.plantuml](diagramas/DiseñoAN.plantuml)
- **Código Fuente**: Rama `develop` del repositorio
- **Pruebas**: [Documentación de casos de prueba](../04-casos-prueba/)
- **Manual de Usuario**: [Guía de usuario](../06-manual-usuario/)

---

**Última actualización**: 2025-11-25  
**Versión del documento**: 2.0  
**Responsable**: Equipo de Desarrollo
