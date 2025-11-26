# 🐳 Dockerización del Sistema de Transcripción Braille

## 📋 Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Archivos de Configuración](#archivos-de-configuración)
4. [Construcción y Ejecución](#construcción-y-ejecución)
5. [Comandos Útiles](#comandos-útiles)

---

## 1. Introducción {#introducción}

Para garantizar que el proyecto se ejecute de manera consistente en cualquier entorno (desarrollo, pruebas o producción), la aplicación es portable mediante la contenedorización con **Docker**.

### Beneficios de la Dockerización

✅ **Portabilidad**: Ejecuta la aplicación en cualquier sistema que soporte Docker  
✅ **Consistencia**: Mismo entorno en desarrollo, pruebas y producción  
✅ **Aislamiento**: Dependencias aisladas del sistema operativo host  
✅ **Facilidad de despliegue**: Simplifica el proceso de instalación  
✅ **Escalabilidad**: Facilita la creación de múltiples instancias  

---

## 2. Requisitos {#requisitos}

### Prerrequisitos

- **Docker**: Versión 20.10 o superior
- **Docker Compose** (opcional): Para orquestación multi-contenedor

### Verificar Instalación

```bash
# Verificar versión de Docker
docker --version

# Verificar que Docker está corriendo
docker ps
```

---

## 3. Archivos de Configuración {#archivos-de-configuración}

### 3.1 requirements.txt

Lista todas las dependencias exactas de Python que necesita el proyecto.

**Ubicación**: Raíz del proyecto

**Propósito**: Asegurar que el entorno de Python dentro del contenedor sea idéntico al entorno de desarrollo.

**Contenido**:
```
Flask==3.0.0
reportlab==4.0.7
Werkzeug==3.0.1
```

**Generación**:
```bash
# Activar entorno virtual
.\.venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# Generar requirements.txt
pip freeze > requirements.txt
```

### 3.2 Dockerfile

Contiene las instrucciones paso a paso que Docker usa para construir la imagen del contenedor.

**Ubicación**: Raíz del proyecto

**Contenido**:

```dockerfile
# Usar una imagen base oficial de Python (python:3.11-slim es eficiente)
FROM python:3.11-slim

# Información del mantenedor
LABEL maintainer="equipo@transcripcion-braille.com"
LABEL description="Sistema de Transcripción Braille - Flask Application"

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Copiar archivo de dependencias
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente
COPY . .

# Exponer el puerto de Flask
EXPOSE 5000

# Variable de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando de inicio: correr la aplicación en el host 0.0.0.0
CMD ["python", "app.py"]
```

### 3.3 .dockerignore

Archivo para excluir archivos innecesarios de la imagen Docker.

**Ubicación**: Raíz del proyecto

**Contenido**:
```
# Entorno virtual
.venv/
venv/
env/

# Archivos de Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Archivos de prueba
.pytest_cache/
.coverage
htmlcov/

# Archivos de Git
.git/
.gitignore

# Documentación
documentacion/
*.md

# Archivos de IDE
.vscode/
.idea/
*.swp
*.swo

# Archivos temporales
*.log
*.tmp
```

### 3.4 docker-compose.yml (Opcional)

Para facilitar la gestión del contenedor.

**Ubicación**: Raíz del proyecto

**Contenido**:
```yaml
version: '3.8'

services:
  braille-app:
    build: .
    container_name: braille-transcription
    ports:
      - "5000:5000"
    volumes:
      - ./src:/usr/src/app/src
      - ./static:/usr/src/app/static
      - ./templates:/usr/src/app/templates
    environment:
      - FLASK_ENV=development
      - FLASK_DEBUG=1
    restart: unless-stopped
```

---

## 4. Construcción y Ejecución {#construcción-y-ejecución}

### 4.1 Construcción de la Imagen

```bash
# Desde la raíz del proyecto
docker build -t braille-transcription:latest .

# Con un nombre de versión específico
docker build -t braille-transcription:1.0 .
```

**Opciones útiles**:
- `--no-cache`: Construir sin usar caché
- `-t <nombre>:<tag>`: Asignar nombre y etiqueta a la imagen

### 4.2 Ejecución del Contenedor

#### Método 1: Docker Run

```bash
# Ejecutar el contenedor
docker run -d -p 5000:5000 --name braille-app braille-transcription:latest

# Con montaje de volúmenes para desarrollo
docker run -d -p 5000:5000 --name braille-app \
  -v $(pwd)/src:/usr/src/app/src \
  braille-transcription:latest
```

**Parámetros**:
- `-d`: Modo detached (segundo plano)
- `-p 5000:5000`: Mapeo de puertos (host:contenedor)
- `--name`: Nombre del contenedor
- `-v`: Montaje de volúmenes

#### Método 2: Docker Compose

```bash
# Iniciar servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down
```

### 4.3 Verificar Ejecución

```bash
# Verificar que el contenedor está corriendo
docker ps

# Acceder a la aplicación
# Abrir navegador en: http://localhost:5000

# Ver logs del contenedor
docker logs braille-app

# Ver logs en tiempo real
docker logs -f braille-app
```

---

## 5. Comandos Útiles {#comandos-útiles}

### 5.1 Gestión de Contenedores

```bash
# Listar contenedores en ejecución
docker ps

# Listar todos los contenedores (incluidos detenidos)
docker ps -a

# Detener contenedor
docker stop braille-app

# Iniciar contenedor detenido
docker start braille-app

# Reiniciar contenedor
docker restart braille-app

# Eliminar contenedor
docker rm braille-app

# Eliminar contenedor en ejecución (forzar)
docker rm -f braille-app
```

### 5.2 Gestión de Imágenes

```bash
# Listar imágenes
docker images

# Eliminar imagen
docker rmi braille-transcription:latest

# Limpiar imágenes no utilizadas
docker image prune

# Limpiar todo (contenedores, imágenes, volúmenes)
docker system prune -a
```

### 5.3 Acceso al Contenedor

```bash
# Ejecutar comando dentro del contenedor
docker exec braille-app ls /usr/src/app

# Acceder a shell interactivo
docker exec -it braille-app /bin/bash

# Ver procesos del contenedor
docker top braille-app

# Inspeccionar contenedor
docker inspect braille-app
```

### 5.4 Debugging

```bash
# Ver logs con timestamps
docker logs --timestamps braille-app

# Ver últimas N líneas de logs
docker logs --tail 50 braille-app

# Monitorear estadísticas de recursos
docker stats braille-app

# Ver cambios en el filesystem
docker diff braille-app
```

---

## 📊 Configuración de Red y Puertos

### Configuración del Servidor Flask

El servidor Flask debe configurarse para ser accesible desde fuera del contenedor:

```python
# app.py
if __name__ == '__main__':
    # Host 0.0.0.0 permite acceso desde fuera del contenedor
    # Puerto 5000 es el predeterminado de Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**Importante**:
- ✅ **Host `0.0.0.0`**: Permite conexiones desde cualquier interfaz
- ❌ **Host `127.0.0.1`**: Solo permite conexiones locales dentro del contenedor

### Mapeo de Puertos

| Puerto Host | Puerto Contenedor | Descripción |
|-------------|-------------------|-------------|
| 5000 | 5000 | Puerto principal de Flask |
| 8000 | 5000 | Mapeo alternativo (opcional) |

Para usar puerto diferente en el host:
```bash
docker run -d -p 8000:5000 --name braille-app braille-transcription:latest
# Acceder en: http://localhost:8000
```

---

## 🔧 Troubleshooting

### Problema: Puerto ya en uso

```bash
# Error: Bind for 0.0.0.0:5000 failed: port is already allocated

# Solución 1: Usar puerto diferente
docker run -d -p 5001:5000 --name braille-app braille-transcription:latest

# Solución 2: Detener proceso que usa el puerto
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Problema: Cambios en código no se reflejan

```bash
# Solución: Reconstruir imagen sin caché
docker build --no-cache -t braille-transcription:latest .
docker stop braille-app
docker rm braille-app
docker run -d -p 5000:5000 --name braille-app braille-transcription:latest
```

### Problema: Contenedor se detiene inmediatamente

```bash
# Ver logs para identificar el error
docker logs braille-app

# Ejecutar en modo interactivo para debugging
docker run -it --rm -p 5000:5000 braille-transcription:latest
```

---

## 📚 Referencias

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Flask Deployment Options](https://flask.palletsprojects.com/en/3.0.x/deploying/)

---

**Última actualización**: 2025-11-25  
**Versión**: 2.0
