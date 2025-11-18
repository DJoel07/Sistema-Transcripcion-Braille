# Plan de Pruebas - Sistema de Transcripción Braille

## 📋 Información General del Plan

| Atributo | Valor |
|----------|-------|
| **Proyecto** | Sistema de Transcripción Braille |
| **Versión** | 1.0 - Bimestre 1 |
| **Fecha de creación** | 2025-11-17 |
| **Responsable de QA** | Equipo de Desarrollo |
| **Entorno de pruebas** | Python 3.11, Flask 3.0, Windows/Linux |

## 🎯 Objetivos del Plan de Pruebas

### Objetivo General
Verificar que el Sistema de Transcripción Braille cumple con todos los requisitos funcionales y no funcionales especificados para el Bimestre 1.

### Objetivos Específicos
1. Validar la correcta transcripción del alfabeto español completo
2. Verificar el manejo correcto de números con signo de número
3. Comprobar la transcripción de vocales acentuadas
4. Validar la transcripción de signos de puntuación básicos
5. Verificar la generación correcta de archivos PDF
6. Comprobar el manejo de errores para caracteres no soportados
7. Validar la interfaz de usuario y experiencia del usuario

## 📊 Alcance de las Pruebas

### Funcionalidades Incluidas
- ✅ Transcripción de alfabeto (a-z, ñ, w)
- ✅ Transcripción de vocales acentuadas (á, é, í, ó, ú, ü)
- ✅ Transcripción de números (0-9)
- ✅ Transcripción de signos de puntuación (. , ; : ¿ ? ¡ ! ( ) -)
- ✅ Generación de PDF con señalética
- ✅ Validación de entrada
- ✅ Interfaz web responsiva

### Funcionalidades Excluidas
- ❌ Transcripción de Braille a texto (Bimestre 2)
- ❌ Símbolos matemáticos avanzados
- ❌ Formato de texto (negritas, cursivas)
- ❌ Múltiples idiomas

## 🧪 Tipos de Pruebas

### 1. Pruebas Unitarias
- **Objetivo**: Verificar componentes individuales del sistema
- **Cobertura objetivo**: ≥ 80%
- **Herramienta**: unittest (Python)
- **Responsable**: Desarrolladores

### 2. Pruebas de Integración
- **Objetivo**: Verificar interacción entre módulos
- **Alcance**: API endpoints, servicios, generador PDF
- **Responsable**: Desarrolladores

### 3. Pruebas Funcionales
- **Objetivo**: Verificar que el sistema cumple requisitos funcionales
- **Método**: Manual y automatizado
- **Responsable**: QA

### 4. Pruebas de Interfaz de Usuario
- **Objetivo**: Verificar usabilidad y experiencia de usuario
- **Método**: Manual
- **Navegadores**: Chrome, Firefox, Edge

### 5. Pruebas de Regresión
- **Objetivo**: Asegurar que cambios no rompan funcionalidad existente
- **Frecuencia**: Antes de cada merge a main
- **Método**: Suite automatizada

## 📝 Casos de Prueba

### Casos de Prueba de Alta Prioridad

| ID | Descripción | Módulo | Prioridad | Estado |
|----|-------------|--------|-----------|--------|
| [CP-001](casos-prueba/CP-001-transcripcion-alfabeto.md) | Transcripción alfabeto básico | Motor | 🔴 Alta | ✅ Pasado |
| [CP-002](casos-prueba/CP-002-transcripcion-numeros.md) | Transcripción de números | Motor | 🔴 Alta | ✅ Pasado |
| [CP-003](casos-prueba/CP-003-vocales-acentuadas.md) | Transcripción vocales acentuadas | Motor | 🔴 Alta | ✅ Pasado |
| [CP-004](casos-prueba/CP-004-signos-puntuacion.md) | Transcripción signos puntuación | Motor | 🔴 Alta | ✅ Pasado |
| [CP-005](casos-prueba/CP-005-generacion-pdf.md) | Generación de PDF | Generador | 🔴 Alta | ✅ Pasado |

### Casos de Prueba de Prioridad Media

| ID | Descripción | Módulo | Prioridad | Estado |
|----|-------------|--------|-----------|--------|
| CP-006 | Caracteres no soportados | Motor | 🟡 Media | ✅ Pasado |
| CP-007 | Validación de entrada | Servicio | 🟡 Media | ✅ Pasado |
| CP-008 | Texto vacío | Motor | 🟡 Media | ✅ Pasado |
| CP-009 | Mayúsculas a minúsculas | Motor | 🟡 Media | ✅ Pasado |
| CP-010 | Límite de caracteres (500) | Frontend | 🟡 Media | ✅ Pasado |

### Casos de Prueba de Interfaz

| ID | Descripción | Componente | Prioridad | Estado |
|----|-------------|------------|-----------|--------|
| CP-UI-001 | Carga de página principal | Frontend | 🟡 Media | ✅ Pasado |
| CP-UI-002 | Botón transcribir | Frontend | 🟡 Media | ✅ Pasado |
| CP-UI-003 | Visualización de resultados | Frontend | 🟡 Media | ✅ Pasado |
| CP-UI-004 | Descarga de PDF | Frontend | 🔴 Alta | ✅ Pasado |
| CP-UI-005 | Copiar al portapapeles | Frontend | 🟢 Baja | ✅ Pasado |
| CP-UI-006 | Responsive design | Frontend | 🟡 Media | ✅ Pasado |

## 🔄 Proceso de Ejecución de Pruebas

### Fase 1: Preparación
```bash
# 1. Actualizar código
git checkout develop
git pull origin develop

# 2. Activar entorno virtual
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Verificar ambiente
python --version  # Verificar Python 3.11+
```

### Fase 2: Ejecución de Pruebas Unitarias
```bash
# Ejecutar todas las pruebas
python -m unittest discover tests/

# Ejecutar pruebas con cobertura
pip install coverage
coverage run -m unittest discover tests/
coverage report
coverage html  # Genera reporte HTML
```

### Fase 3: Ejecución de Pruebas Manuales
1. Iniciar aplicación: `python app.py`
2. Abrir navegador: `http://localhost:5000`
3. Ejecutar casos de prueba según documentación
4. Documentar resultados en formato especificado

### Fase 4: Registro de Resultados
- Actualizar tabla de estado de casos de prueba
- Documentar bugs encontrados como issues en GitHub
- Crear reporte de ejecución (ver [resultados-ejecucion/](resultados-ejecucion/))

## 🐛 Criterios de Fallo

Un caso de prueba falla si:
- ❌ El resultado obtenido difiere del resultado esperado
- ❌ El sistema lanza una excepción no manejada
- ❌ El tiempo de respuesta excede 2 segundos (requisito RNF-002)
- ❌ El PDF generado no es válido o no se descarga
- ❌ La interfaz no es responsive

## ✅ Criterios de Aceptación

### Para Casos de Prueba Individuales
- ✅ Resultado coincide con esperado
- ✅ No hay excepciones no manejadas
- ✅ Tiempo de respuesta aceptable
- ✅ Logs no muestran errores

### Para el Sistema Completo
- ✅ Todos los casos de prueba de prioridad Alta pasan
- ✅ Al menos 95% de casos de prioridad Media pasan
- ✅ Cobertura de código ≥ 80%
- ✅ 0 bugs críticos pendientes
- ✅ Documentación de resultados completa

## 📊 Métricas de Calidad

### Métricas a Reportar
| Métrica | Objetivo | Actual |
|---------|----------|--------|
| Casos de prueba pasados | 100% de Alta prioridad | - |
| Cobertura de código | ≥ 80% | - |
| Bugs críticos | 0 | - |
| Bugs altos | ≤ 2 | - |
| Tiempo promedio de respuesta | < 2 segundos | - |

### Reporte de Defectos
| Severidad | Descripción | Acción |
|-----------|-------------|--------|
| 🔴 Crítico | Sistema no funciona | Hotfix inmediato |
| 🟠 Alto | Funcionalidad principal falla | Fix en < 24h |
| 🟡 Medio | Funcionalidad secundaria falla | Fix en próximo sprint |
| 🟢 Bajo | Problema cosmético | Backlog |

## 🔄 Manejo de Casos de Prueba Fallidos

### Proceso Obligatorio para Casos Fallidos

1. **Documentar el Fallo**
   - Resultado esperado vs obtenido
   - Pasos exactos para reproducir
   - Screenshots/logs si aplica
   - Fecha y hora de ejecución
   - Ambiente (OS, navegador, versión)

2. **Análisis de Causa Raíz**
   - Identificar módulo afectado
   - Analizar código relacionado
   - Determinar causa del fallo
   - Documentar análisis en caso de prueba

3. **Implementar Solución**
   - Crear issue en GitHub
   - Desarrollar fix en branch apropiado
   - Añadir test que reproduzca el bug
   - Verificar que test pasa con el fix
   - Commit y PR

4. **Re-ejecutar Caso de Prueba**
   - Ejecutar caso de prueba original
   - Verificar que ahora pasa
   - Documentar resultado exitoso
   - Actualizar estado en plan de pruebas

5. **Documentación Final**
   - Actualizar caso de prueba con:
     - Análisis del fallo
     - Solución implementada
     - Resultado de re-ejecución
   - Ver ejemplo en [CP-001](casos-prueba/CP-001-transcripcion-alfabeto.md)

## 📅 Calendario de Pruebas

| Hito | Fecha | Actividad |
|------|-------|-----------|
| Sprint 1 | Semana 1-2 | Pruebas unitarias continuas |
| Sprint 2 | Semana 3-4 | Pruebas de integración |
| Pre-release | Semana 5 | Pruebas de regresión completas |
| Release | Semana 6 | Validación final y entrega |

## 🛠️ Ambiente de Pruebas

### Configuración Requerida
- **SO**: Windows 10/11, Ubuntu 20.04+, macOS 11+
- **Python**: 3.11 o superior
- **Navegadores**: Chrome 90+, Firefox 88+, Edge 90+
- **Resoluciones**: 1920x1080, 1366x768, 375x667 (móvil)

### Datos de Prueba
Ver [datos-prueba.md](datos-prueba.md) para conjunto completo de datos de prueba.

## 📚 Referencias
- [Casos de Prueba Detallados](casos-prueba/)
- [Resultados de Ejecución](resultados-ejecucion/)
- [SRS - Requisitos](../01-diseno-arquitectonico/SRS.txt)
- [Casos de Uso](../01-diseno-arquitectonico/UseCases.txt)

---

**Última actualización**: 2025-11-17  
**Próxima revisión**: Antes de cada release
