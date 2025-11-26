# 📚 Documentación del Proyecto - Sistema de Transcripción Braille

## Índice de Documentación

Esta rama contiene toda la documentación técnica y de usuario del proyecto, organizada según los requisitos del curso.

### 📂 Estructura de la Documentación

#### [1. Diseño Arquitectónico de Alto Nivel](01-diseno-arquitectonico/)
- **Descripción**: Arquitectura del sistema, requisitos, casos de uso y decisiones de diseño
- **Archivos**:
  - [diseno-arquitectonico.md](01-diseno-arquitectonico/diseno-arquitectonico.md) - Documento consolidado con:
    - Detalles y requerimientos del proyecto
    - Especificación de requisitos (SRS)
    - Arquitectura de 3 capas
    - Casos de uso detallados
    - Historias de usuario
  - [diagramas/DiseñoAN.plantuml](01-diseno-arquitectonico/diagramas/DiseñoAN.plantuml) - Diagrama PlantUML

#### [2. Ambiente de Desarrollo](02-ambiente-desarrollo/)
- **Descripción**: Herramientas, flujo de trabajo, estrategia de ramificación y dockerización
- **Archivos**:
  - [herramientas-seleccionadas.md](02-ambiente-desarrollo/herramientas-seleccionadas.md) - Stack tecnológico
  - [estrategia-ramificacion.md](02-ambiente-desarrollo/estrategia-ramificacion.md) - GitFlow y branching
  - [flujo-trabajo.md](02-ambiente-desarrollo/flujo-trabajo.md) - Workflow del equipo
  - [dockerizacion.md](02-ambiente-desarrollo/dockerizacion.md) - Guía de Docker completa

#### [3. Documentación Técnica](03-documentacion-tecnica/)
- **Descripción**: Documentación tipo JavaDoc del código fuente
- **Archivos**:
  - [link.md](03-documentacion-tecnica/link.md) - Enlaces a documentación técnica

#### [4. Casos de Prueba](04-casos-prueba/)
- **Descripción**: Plan de pruebas, técnicas, casos de prueba y resultados de ejecución
- **Archivos**:
  - [plan-pruebas.md](04-casos-prueba/plan-pruebas.md) - Plan maestro de pruebas
  - [tecnicas-prueba.md](04-casos-prueba/tecnicas-prueba.md) - Técnicas aplicadas (Partición de Equivalencias, Valores Límite, Robustez)
  - [casos-prueba/](04-casos-prueba/casos-prueba/) - Casos de prueba detallados (CP-001, etc.)
  - [resultados-ejecucion/](04-casos-prueba/resultados-ejecucion/) - Resultados y análisis
    - [reporte-validacion.md](04-casos-prueba/resultados-ejecucion/reporte-validacion.md) - 61/61 tests pasando

#### [5. Manual de Instalación](05-manual-instalacion/)
- **Descripción**: Guías paso a paso para instalar y configurar el sistema
- **Archivos**:
  - [instalacion-local.md](05-manual-instalacion/instalacion-local.md) - Instalación en entorno local

#### [6. Manual de Usuario](06-manual-usuario/)
- **Descripción**: Guía de uso del sistema para usuarios finales
- **Archivos**:
  - [guia-usuario.md](06-manual-usuario/guia-usuario.md) - Manual completo de usuario
  - [capturas/](06-manual-usuario/capturas/) - Capturas de pantalla

---

## 🔄 Actualización de la Documentación

Para contribuir a la documentación:

```bash
# Cambiar a la rama de documentación
git checkout documentacion

# Hacer cambios en los archivos

# Commitear cambios
git add .
git commit -m "docs: descripción de los cambios"

# Push a GitHub
git push origin documentacion
```

## 📋 Estado de Completitud

| Sección | Estado | Última Actualización |
|---------|--------|---------------------|
| 1. Diseño Arquitectónico | ✅ Completo | 2025-11-25 |
| 2. Ambiente de Desarrollo | ✅ Completo | 2025-11-25 |
| 3. Documentación Técnica | 🔄 En progreso | 2025-11-17 |
| 4. Casos de Prueba | ✅ Completo | 2025-11-25 |
| 5. Manual de Instalación | 🔄 En progreso | 2025-11-17 |
| 6. Manual de Usuario | 🔄 En progreso | 2025-11-17 |

---

## 🎯 Cambios Recientes (v2.0 - 2025-11-25)

### ✅ Consolidación de Documentos
- ✅ Consolidados 5 archivos .txt en `01-diseno-arquitectonico/diseno-arquitectonico.md`
- ✅ Convertido Dockerizacion.txt a dockerizacion.md con formato mejorado
- ✅ Movido Tecnicas_Test.md a `04-casos-prueba/tecnicas-prueba.md`
- ✅ Movido Validaciones.md a `04-casos-prueba/resultados-ejecucion/reporte-validacion.md`

### 📝 Documentos Eliminados (Redundantes)
- ❌ DetallesProyecto.txt
- ❌ Documentacion.txt
- ❌ SRS.txt
- ❌ UseCases.txt
- ❌ UserHistory.txt
- ❌ Dockerizacion.txt

### 🎉 Mejoras Implementadas
- ✅ Estructura más clara y organizada
- ✅ Todo en formato Markdown para mejor legibilidad
- ✅ Navegación mejorada con tabla de contenidos
- ✅ Referencias cruzadas entre documentos
- ✅ Eliminadas redundancias

---

**Proyecto**: Sistema de Transcripción Braille  
**Curso**: Construcción de Software  
**Semestre**: 2025B
