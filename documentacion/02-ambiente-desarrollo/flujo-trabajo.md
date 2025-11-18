# Flujo de Trabajo del Equipo

## 👥 Roles y Responsabilidades

### Desarrollador Backend
- **Responsabilidades**:
  - Implementar lógica de transcripción Braille
  - Desarrollar generador de PDF
  - Crear servicios y controladores Flask
  - Escribir pruebas unitarias
- **Branches principales**: `develop`, `feature/*`

### Desarrollador Frontend
- **Responsabilidades**:
  - Diseñar interfaz de usuario
  - Implementar interacción con API
  - Garantizar responsive design
  - Validación de formularios del lado del cliente
- **Branches principales**: `develop`, `feature/*`

### Responsable de Documentación
- **Responsabilidades**:
  - Mantener documentación actualizada
  - Escribir manuales de usuario e instalación
  - Documentar casos de prueba
  - Generar diagramas arquitectónicos
- **Branches principales**: `documentacion`

### Responsable de QA/Testing
- **Responsabilidades**:
  - Diseñar plan de pruebas
  - Ejecutar casos de prueba
  - Reportar bugs encontrados
  - Validar correcciones
- **Branches principales**: `develop`, `bugfix/*`

## 🔄 Ciclo de Desarrollo Completo

### Fase 1: Planificación (Sprint Planning)

**Duración**: 1-2 horas al inicio de cada iteración

```
1. Reunión del equipo
2. Revisar requisitos pendientes
3. Seleccionar funcionalidades para la iteración
4. Dividir en tareas (issues en GitHub)
5. Asignar responsables
6. Estimar esfuerzo
```

**Resultado**: Lista de features a implementar con owners asignados

### Fase 2: Desarrollo

**Duración**: Variable según complejidad

#### Para cada Feature:

```bash
# 1. Desarrollador: Crear feature branch
git checkout develop
git pull origin develop
git checkout -b feature/nombre-funcionalidad

# 2. Implementar funcionalidad
# - Escribir código
# - Escribir docstrings
# - Añadir pruebas unitarias

# 3. Commits frecuentes (cada 1-2 horas de trabajo)
git add .
git commit -m "feat: descripción específica del cambio"

# 4. Mantener actualizado con develop
git fetch origin
git merge origin/develop

# 5. Push cuando esté listo para revisión
git push origin feature/nombre-funcionalidad
```

### Fase 3: Code Review

**Duración**: 1-2 días máximo

```
1. Desarrollador: Crear Pull Request en GitHub
   - Base branch: develop
   - Compare branch: feature/nombre-funcionalidad
   - Título descriptivo
   - Descripción completa de cambios
   - Screenshots si aplica

2. Asignar reviewers (al menos 1)

3. Reviewer: Revisar código
   - ✅ Verifica que sigue convenciones
   - ✅ Verifica que tiene pruebas
   - ✅ Verifica que las pruebas pasan
   - ✅ Verifica que está documentado
   - 💬 Dejar comentarios constructivos

4. Desarrollador: Atender feedback
   - Hacer cambios solicitados
   - Responder comentarios
   - Push de actualizaciones

5. Reviewer: Aprobar PR cuando esté listo
```

### Fase 4: Integración

```bash
# 1. Merge del PR (por GitHub)
# - Squash commits si son muchos
# - Merge commit si se quiere preservar historial

# 2. Actualizar local
git checkout develop
git pull origin develop

# 3. Eliminar feature branch
git branch -d feature/nombre-funcionalidad
git push origin --delete feature/nombre-funcionalidad
```

### Fase 5: Testing

**Responsable**: QA/Testing

```bash
# 1. Actualizar ambiente de testing
git checkout develop
git pull origin develop

# 2. Ejecutar suite de pruebas
python -m unittest discover tests/

# 3. Pruebas manuales de integración
python app.py
# - Probar en navegador
# - Verificar todas las funcionalidades

# 4. Documentar resultados
# - Si pasa: marcar como ✅ en casos de prueba
# - Si falla: crear issue con bug
```

### Fase 6: Release (cuando develop esté estable)

```bash
# 1. Verificar que todo está probado
# 2. Actualizar versión en archivos relevantes
# 3. Crear PR: develop → main
# 4. Después de merge, crear tag
git tag -a v1.0.0 -m "Release Bimestre 1"
git push origin v1.0.0
```

## 📅 Ritmo de Trabajo Recomendado

### Daily Standup (Opcional para equipos pequeños)
- **Cuándo**: Inicio del día (10-15 minutos)
- **Formato**:
  - ¿Qué hice ayer?
  - ¿Qué haré hoy?
  - ¿Tengo algún bloqueador?

### Sprint Review (Cada 1-2 semanas)
- **Cuándo**: Final de iteración
- **Agenda**:
  - Demostrar funcionalidades completadas
  - Revisar lo que no se completó
  - Retrospectiva: ¿qué mejorar?

## 🐛 Manejo de Bugs

### Flujo para Reportar Bug

```
1. QA encuentra bug
2. Crear issue en GitHub
   - Título descriptivo
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Screenshots/logs si aplica
   - Label: "bug"
   - Asignar prioridad

3. Equipo decide:
   - Urgente → hotfix
   - Normal → bugfix branch

4. Desarrollador:
   git checkout -b bugfix/descripcion-bug
   # Corregir
   # Añadir test que reproduzca el bug
   # Verificar que el test pasa
   git push origin bugfix/descripcion-bug
   
5. PR → develop
6. QA verifica corrección
7. Cerrar issue
```

### Priorización de Bugs

| Prioridad | Descripción | Tiempo de Respuesta |
|-----------|-------------|---------------------|
| 🔴 Crítico | Sistema no funciona | Inmediato (hotfix) |
| 🟠 Alto | Funcionalidad principal afectada | < 24 horas |
| 🟡 Medio | Funcionalidad secundaria afectada | < 3 días |
| 🟢 Bajo | Problema cosmético | Próximo sprint |

## 📋 Template de Pull Request

```markdown
## Descripción
Breve descripción de los cambios

## Tipo de cambio
- [ ] Bug fix (cambio no-breaking que corrige un issue)
- [ ] Nueva funcionalidad (cambio no-breaking que añade funcionalidad)
- [ ] Breaking change (fix o feature que causa cambios en funcionalidad existente)
- [ ] Documentación

## ¿Cómo se ha probado?
Describe las pruebas realizadas

## Checklist
- [ ] Mi código sigue las convenciones del proyecto
- [ ] He realizado self-review de mi código
- [ ] He comentado mi código, especialmente en áreas complejas
- [ ] He actualizado la documentación correspondiente
- [ ] Mis cambios no generan nuevas advertencias
- [ ] He añadido pruebas que demuestran que mi fix funciona o que mi feature funciona
- [ ] Pruebas unitarias nuevas y existentes pasan localmente
- [ ] He actualizado requirements.txt si añadí dependencias

## Screenshots (si aplica)
```

## 🔧 Herramientas de Comunicación

### Para el Proyecto
- **GitHub Issues**: Tracking de tareas y bugs
- **GitHub Projects**: Board Kanban para visualizar progreso
- **Pull Requests**: Code review y discusión técnica

### Para el Equipo (Recomendado)
- **Discord/Slack**: Comunicación rápida diaria
- **Google Meet/Zoom**: Reuniones de planificación
- **Google Drive**: Documentos compartidos

## 📊 Métricas de Éxito

### Indicadores de Calidad
- ✅ Cobertura de tests > 80%
- ✅ 0 bugs críticos en main
- ✅ Todos los PRs revisados antes de merge
- ✅ Documentación actualizada

### Indicadores de Productividad
- ✅ Tiempo de review < 48 horas
- ✅ Tiempo de vida de feature branch < 7 días
- ✅ Commits diarios en features activas

## 🎯 Mejores Prácticas del Equipo

### Comunicación
- ✅ Comunicar bloqueos temprano
- ✅ Ser específico en descripciones (issues, PRs, commits)
- ✅ Dar feedback constructivo en code reviews
- ✅ Actualizar issues con progreso

### Código
- ✅ Escribir código auto-documentado
- ✅ Probar localmente antes de push
- ✅ Seguir principios SOLID
- ✅ No comentar código muerto (eliminarlo)

### Git
- ✅ Pull antes de empezar a trabajar
- ✅ Push al final del día
- ✅ Commits atómicos (un cambio lógico)
- ✅ Mantener historial limpio

---

**Última actualización**: 2025-11-17  
**Revisión**: Cada inicio de iteración
