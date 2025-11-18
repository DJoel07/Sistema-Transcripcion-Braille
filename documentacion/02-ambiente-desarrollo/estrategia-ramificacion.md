# Estrategia de Ramificación: Feature Branch Workflow

## 🌿 Modelo de Ramificación

Este proyecto implementa el **Feature Branch Workflow**, una estrategia de ramificación que mantiene la rama principal limpia y permite desarrollo paralelo de funcionalidades.

## 📋 Estructura de Ramas

### Ramas Permanentes

#### `main`
- **Propósito**: Código de producción estable y listo para entregar
- **Protección**: ✅ Protegida - No se permite desarrollo directo
- **Actualización**: Solo mediante Pull Requests aprobados desde `develop`
- **Restricciones**:
  - No se permiten commits directos
  - Requiere al menos 1 revisión aprobada
  - Todos los tests deben pasar

#### `documentacion`
- **Propósito**: Documentación técnica y de usuario del proyecto
- **Contenido**: 
  - Diseño arquitectónico
  - Manuales de instalación y usuario
  - Casos de prueba y resultados
  - Documentación del código
- **Actualización**: Commits directos por el equipo de documentación
- **Independiente**: No se fusiona con `main` o `develop`

#### `develop`
- **Propósito**: Rama de integración para desarrollo activo
- **Contenido**: Últimas funcionalidades completadas y probadas
- **Actualización**: Merge de ramas `feature/*` completadas
- **Estabilidad**: Código funcional pero en desarrollo activo

### Ramas Temporales

#### `feature/*`
- **Propósito**: Desarrollo de nuevas funcionalidades
- **Nomenclatura**: `feature/nombre-descriptivo-en-kebab-case`
- **Ejemplos**:
  - `feature/transcripcion-alfabeto`
  - `feature/generador-pdf`
  - `feature/interfaz-usuario`
  - `feature/validacion-entrada`
- **Ciclo de vida**:
  1. Se crean desde `develop`
  2. Se desarrolla la funcionalidad
  3. Se prueban localmente
  4. Se fusionan de vuelta a `develop`
  5. Se eliminan después del merge

#### `hotfix/*`
- **Propósito**: Correcciones urgentes en producción
- **Nomenclatura**: `hotfix/descripcion-del-problema`
- **Ejemplos**:
  - `hotfix/error-transcripcion-numeros`
  - `hotfix/pdf-no-descarga`
- **Ciclo de vida**:
  1. Se crean desde `main`
  2. Se corrige el problema
  3. Se prueban exhaustivamente
  4. Se fusionan a `main` y `develop`
  5. Se eliminan después del merge

#### `bugfix/*` (Opcional)
- **Propósito**: Correcciones de bugs no urgentes
- **Nomenclatura**: `bugfix/descripcion-del-bug`
- **Ciclo de vida**: Similar a `feature/*` pero para correcciones

## 🔄 Flujo de Trabajo Completo

### 1. Desarrollo de Nueva Funcionalidad

```bash
# 1. Actualizar develop
git checkout develop
git pull origin develop

# 2. Crear feature branch
git checkout -b feature/mi-nueva-funcionalidad

# 3. Desarrollar (hacer commits frecuentes)
git add .
git commit -m "feat: implementa lógica de transcripción"
git commit -m "test: añade pruebas unitarias"
git commit -m "docs: actualiza docstrings"

# 4. Mantener branch actualizado con develop
git checkout develop
git pull origin develop
git checkout feature/mi-nueva-funcionalidad
git merge develop

# 5. Push de la feature branch
git push origin feature/mi-nueva-funcionalidad

# 6. Crear Pull Request en GitHub
# - Ir a GitHub
# - Base: develop ← Compare: feature/mi-nueva-funcionalidad
# - Añadir descripción
# - Asignar reviewers

# 7. Después de aprobación y merge, limpiar
git checkout develop
git pull origin develop
git branch -d feature/mi-nueva-funcionalidad
git push origin --delete feature/mi-nueva-funcionalidad
```

### 2. Preparar Release (Entrega)

```bash
# 1. Asegurar que develop está listo
git checkout develop
git pull origin develop

# 2. Ejecutar todas las pruebas
python -m unittest discover tests/

# 3. Crear Pull Request: develop → main
# En GitHub:
# - Base: main ← Compare: develop
# - Título: "Release v1.0: Bimestre 1"
# - Describir cambios incluidos

# 4. Después de aprobación y merge
git checkout main
git pull origin main

# 5. Crear tag de versión
git tag -a v1.0 -m "Release Bimestre 1: Transcripción básica completa"
git push origin v1.0
```

### 3. Hotfix Urgente

```bash
# 1. Crear hotfix desde main
git checkout main
git pull origin main
git checkout -b hotfix/error-critico

# 2. Corregir el problema
git add .
git commit -m "fix: corrige error en transcripción de números"

# 3. Probar exhaustivamente
python -m unittest discover tests/

# 4. Push del hotfix
git push origin hotfix/error-critico

# 5. Crear 2 Pull Requests:
# PR1: hotfix/error-critico → main
# PR2: hotfix/error-critico → develop

# 6. Después de merge, limpiar
git branch -d hotfix/error-critico
git push origin --delete hotfix/error-critico
```

## 📝 Convención de Commits

Seguimos la especificación **Conventional Commits**:

### Formato
```
<tipo>(<alcance opcional>): <descripción>

[cuerpo opcional]

[footer opcional]
```

### Tipos de Commits

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `feat` | Nueva funcionalidad | `feat: añade transcripción de números` |
| `fix` | Corrección de bug | `fix: corrige mapeo de letra ñ` |
| `docs` | Solo documentación | `docs: actualiza README con ejemplos` |
| `style` | Formato (no afecta código) | `style: formatea código con black` |
| `refactor` | Refactorización | `refactor: simplifica lógica de validación` |
| `test` | Añade/modifica tests | `test: añade tests para vocales acentuadas` |
| `chore` | Tareas de mantenimiento | `chore: actualiza dependencias` |

### Ejemplos de Buenos Commits

```bash
git commit -m "feat(core): implementa motor de transcripción Braille"
git commit -m "fix(pdf): corrige alineación de puntos en PDF"
git commit -m "docs: añade manual de instalación con Docker"
git commit -m "test(engine): añade casos de prueba para números"
git commit -m "refactor(services): extrae lógica a service layer"
```

## 🛡️ Protección de Ramas

### Configuración de `main` en GitHub

1. **Settings** → **Branches** → **Add rule**
2. **Branch name pattern**: `main`
3. **Configuración recomendada**:
   - ☑️ Require a pull request before merging
     - ☑️ Require approvals: 1
   - ☑️ Require status checks to pass before merging
     - ☑️ Require branches to be up to date
   - ☑️ Do not allow bypassing the above settings
   - ☑️ Restrict who can push to matching branches

### Configuración de `develop` en GitHub

1. **Settings** → **Branches** → **Add rule**
2. **Branch name pattern**: `develop`
3. **Configuración recomendada**:
   - ☑️ Require a pull request before merging
   - ☑️ Require status checks to pass before merging

## 📊 Diagrama de Flujo

```
                    ┌──────────────┐
                    │     main     │ ← Producción
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   hotfix/*   │ ← Solo emergencias
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   develop    │ ← Integración
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
         ┌────▼────┐  ┌───▼────┐  ┌───▼────┐
         │feature/ │  │feature/│  │feature/│
         │  alfa   │  │  beta  │  │  gamma │
         └─────────┘  └────────┘  └────────┘

         ┌─────────────────────────────────┐
         │      documentacion              │ ← Independiente
         └─────────────────────────────────┘
```

## 🎯 Mejores Prácticas

### ✅ Hacer
- Crear feature branch para cada funcionalidad
- Commits pequeños y frecuentes
- Mensajes de commit descriptivos
- Probar localmente antes de push
- Mantener branches actualizados con develop
- Eliminar branches después de merge
- Escribir buenos títulos en PRs
- Documentar decisiones importantes

### ❌ Evitar
- Commits directos a main
- Branches de larga duración (> 1 semana)
- Commits con mensajes vagos ("fix", "update")
- Push de código sin probar
- Mezclar múltiples funcionalidades en un branch
- Dejar branches obsoletos en el repositorio

## 📚 Recursos

- [Feature Branch Workflow - Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

---

**Última actualización**: 2025-11-17  
**Aplicado desde**: Inicio del proyecto
