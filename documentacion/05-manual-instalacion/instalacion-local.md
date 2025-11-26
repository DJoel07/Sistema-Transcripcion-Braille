# Manual de Instalación - Sistema de Transcripción Braille

## 📋 Tabla de Contenido

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Opción 1: Instalación Local](#opción-1-instalación-local)
3. [Opción 2: Instalación con Docker](#opción-2-instalación-con-docker)
4. [Verificación de la Instalación](#verificación-de-la-instalación)
5. [Solución de Problemas](#solución-de-problemas)

---

## 🖥️ Requisitos del Sistema

### Requisitos Mínimos

| Componente | Especificación |
|------------|----------------|
| **Sistema Operativo** | Windows 10/11, Ubuntu 20.04+, macOS 11+ |
| **Procesador** | Intel Core i3 o equivalente |
| **RAM** | 4 GB |
| **Espacio en Disco** | 500 MB libres |
| **Navegador Web** | Chrome 90+, Firefox 88+, Edge 90+ |

### Requisitos Recomendados

| Componente | Especificación |
|------------|----------------|
| **Sistema Operativo** | Windows 11, Ubuntu 22.04, macOS 12+ |
| **Procesador** | Intel Core i5 o equivalente |
| **RAM** | 8 GB |
| **Espacio en Disco** | 1 GB libres |

### Software Requerido

#### Para Instalación Local
- **Python** 3.11 o superior
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)

#### Para Instalación con Docker
- **Docker Desktop** 4.0+
- **Git** (para clonar el repositorio)

---

## 🔧 Opción 1: Instalación Local

### Paso 1: Instalar Python

#### Windows

1. Descargar Python desde [python.org](https://www.python.org/downloads/)
2. Ejecutar el instalador
3. ✅ **IMPORTANTE**: Marcar "Add Python to PATH"
4. Hacer clic en "Install Now"

```powershell
# Verificar instalación
python --version
# Salida esperada: Python 3.11.x o superior
```

#### Linux (Ubuntu/Debian)

```bash
# Actualizar repositorios
sudo apt update

# Instalar Python 3.11
sudo apt install python3.11 python3.11-venv python3-pip

# Verificar instalación
python3.11 --version
```

#### macOS

```bash
# Con Homebrew
brew install python@3.11

# Verificar instalación
python3 --version
```

### Paso 2: Instalar Git

#### Windows
1. Descargar desde [git-scm.com](https://git-scm.com/download/win)
2. Ejecutar el instalador con opciones por defecto

#### Linux
```bash
sudo apt install git
```

#### macOS
```bash
brew install git
```

### Paso 3: Clonar el Repositorio

```bash
# Navegar al directorio donde quieres instalar
cd C:\Users\TU_USUARIO\Documentos  # Windows
cd ~/Documents                      # Linux/Mac

# Clonar repositorio
git clone https://github.com/DJoel07/Sistema-Transcripcion-Braille.git

# Entrar al directorio
cd Sistema-Transcripcion-Braille

# Cambiar a rama main (código estable)
git checkout main
```

### Paso 4: Crear Entorno Virtual

#### Windows (PowerShell)

```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Si hay error de política de ejecución:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Linux/macOS

```bash
# Crear entorno virtual
python3.11 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

**Indicador de Éxito**: Debe aparecer `(venv)` al inicio de tu línea de comandos.

### Paso 5: Instalar Dependencias

```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt
```

**Salida Esperada**:
```
Successfully installed Flask-3.0.0 reportlab-4.0.7 Werkzeug-3.0.1 python-dotenv-1.0.0 ...
```

### Paso 6: Configurar Variables de Entorno (Opcional)

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tu editor favorito
# notepad .env      # Windows
# nano .env         # Linux
# vim .env          # Linux/Mac
```

**Contenido del `.env` (opcional, usa valores por defecto si no lo editas)**:
```ini
FLASK_APP=app.py
FLASK_ENV=development
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
SECRET_KEY=tu-clave-secreta-aqui
```

### Paso 7: Ejecutar la Aplicación

```bash
# Asegurarse de que el entorno virtual está activo
# (debe aparecer (venv) al inicio de la línea)

# Iniciar servidor
python app.py
```

**Salida Esperada**:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
Press CTRL+C to quit
```

### Paso 8: Acceder a la Aplicación

1. Abrir navegador web
2. Navegar a: `http://localhost:5000`
3. Deberías ver la interfaz del Sistema de Transcripción Braille

✅ **¡Instalación Completada!**

---

## 🐳 Opción 2: Instalación con Docker

### Paso 1: Instalar Docker Desktop

#### Windows
1. Descargar desde [docker.com](https://www.docker.com/products/docker-desktop)
2. Ejecutar instalador
3. Reiniciar PC si es necesario
4. Abrir Docker Desktop y esperar que inicie

#### Linux
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Cerrar y reabrir sesión
```

#### macOS
1. Descargar desde [docker.com](https://www.docker.com/products/docker-desktop)
2. Arrastrar a carpeta Aplicaciones
3. Abrir Docker Desktop

```bash
# Verificar instalación
docker --version
# Salida esperada: Docker version 24.x.x
```

### Paso 2: Clonar el Repositorio

```bash
# Navegar al directorio deseado
cd ~/Documents  # o C:\Users\TU_USUARIO\Documentos en Windows

# Clonar repositorio
git clone https://github.com/DJoel07/Sistema-Transcripcion-Braille.git

# Entrar al directorio
cd Sistema-Transcripcion-Braille

# Cambiar a rama main
git checkout main
```

### Paso 3: Construir la Imagen Docker

```bash
# Construir imagen (esto puede tardar 2-3 minutos)
docker build -t braille-transcriptor .
```

**Salida Esperada**:
```
[+] Building 45.2s (12/12) FINISHED
Successfully built abc123def456
Successfully tagged braille-transcriptor:latest
```

### Paso 4: Ejecutar el Contenedor

```bash
# Opción 1: Ejecución en primer plano
docker run -p 5000:5000 braille-transcriptor

# Opción 2: Ejecución en segundo plano (recomendado)
docker run -d -p 5000:5000 --name braille-app braille-transcriptor
```

**Verificar que el contenedor está corriendo**:
```bash
docker ps

# Salida esperada:
# CONTAINER ID   IMAGE                  STATUS         PORTS
# abc123def456   braille-transcriptor   Up 5 seconds   0.0.0.0:5000->5000/tcp
```

### Paso 5: Acceder a la Aplicación

1. Abrir navegador
2. Navegar a: `http://localhost:5000`

✅ **¡Instalación con Docker Completada!**

### Comandos Útiles de Docker

```bash
# Ver contenedores en ejecución
docker ps

# Ver logs del contenedor
docker logs braille-app

# Detener contenedor
docker stop braille-app

# Reiniciar contenedor
docker start braille-app

# Eliminar contenedor
docker rm braille-app

# Ver imágenes
docker images

# Eliminar imagen
docker rmi braille-transcriptor
```

---

## ✅ Verificación de la Instalación

### Checklist de Verificación

#### 1. Verificar que el servidor está corriendo

```bash
# En terminal (método local)
# Debe mostrar: Running on http://127.0.0.1:5000

# O para Docker
docker logs braille-app
# Debe mostrar logs del servidor Flask
```

#### 2. Verificar acceso web

1. Abrir `http://localhost:5000`
2. ✅ La página debe cargar sin errores
3. ✅ Debe mostrar el título "Transcriptor Braille"
4. ✅ Debe haber un área de texto y botones

#### 3. Verificar funcionalidad básica

1. En el campo de texto, escribir: `hola`
2. Hacer clic en "Transcribir a Braille"
3. ✅ Debe mostrar resultado: `⠓⠕⠇⠁`
4. ✅ Debe aparecer mensaje de éxito

#### 4. Verificar generación de PDF

1. Después de transcribir
2. Hacer clic en "Generar Señalética PDF"
3. ✅ Debe descargarse archivo `senaletica_braille.pdf`
4. ✅ El PDF debe abrir correctamente

#### 5. Ejecutar Pruebas Unitarias (Solo Instalación Local)

```bash
# Activar entorno virtual
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# Ejecutar pruebas
python -m unittest discover tests/

# Salida esperada: todas las pruebas pasan
# Ran X tests in Y.ZZZs
# OK
```

---

## 🔧 Solución de Problemas

### Problema 1: "Python no se reconoce como comando"

**Causa**: Python no está en el PATH del sistema

**Solución Windows**:
```powershell
# Encontrar ubicación de Python
where python

# Agregar manualmente al PATH:
# 1. Buscar "Variables de entorno" en Windows
# 2. Editar "Path" en Variables del sistema
# 3. Agregar: C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python311
```

**Solución Linux/Mac**:
```bash
# Usar python3 en lugar de python
python3 --version

# O crear alias
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc
```

### Problema 2: "ModuleNotFoundError: No module named 'flask'"

**Causa**: Entorno virtual no está activado o dependencias no instaladas

**Solución**:
```bash
# 1. Verificar que entorno virtual está activo
# Debe aparecer (venv) al inicio de la línea

# Si no está activo:
# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate

# 2. Reinstalar dependencias
pip install -r requirements.txt
```

### Problema 3: Error de política de ejecución (Windows PowerShell)

**Error**: "no se puede cargar el archivo ... porque la ejecución de scripts está deshabilitada"

**Solución**:
```powershell
# Ejecutar PowerShell como Administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Luego volver a activar entorno virtual
.\venv\Scripts\Activate.ps1
```

### Problema 4: Puerto 5000 ya en uso

**Error**: "Address already in use" o "OSError: [Errno 48]"

**Solución Opción 1**: Cambiar puerto
```bash
# Editar .env
FLASK_PORT=5001

# Reiniciar aplicación
python app.py
# Acceder a http://localhost:5001
```

**Solución Opción 2**: Detener proceso en puerto 5000

**Windows**:
```powershell
# Encontrar proceso
netstat -ano | findstr :5000

# Terminar proceso (reemplazar PID)
taskkill /PID NUMERO_PID /F
```

**Linux/Mac**:
```bash
# Encontrar y terminar proceso
lsof -ti:5000 | xargs kill -9
```

### Problema 5: Docker no inicia el contenedor

**Solución**:
```bash
# Ver logs de error
docker logs braille-app

# Verificar que Docker Desktop está corriendo
docker info

# Reconstruir imagen
docker rmi braille-transcriptor
docker build -t braille-transcriptor .
```

### Problema 6: Página web no carga estilos

**Causa**: Archivos estáticos no se encuentran

**Solución**:
```bash
# Verificar estructura de carpetas
ls src/static/css/
ls src/static/js/

# Si faltan archivos, verificar rama correcta
git checkout main
git pull origin main
```

### Problema 7: Error al generar PDF

**Error**: "Error al generar señalética"

**Solución**:
```bash
# Verificar instalación de reportlab
pip show reportlab

# Si no está instalado
pip install reportlab==4.0.7

# Verificar permisos de escritura
# En Windows: deshabilitar antivirus temporalmente
```

---

## 📞 Soporte Adicional

Si después de seguir esta guía aún tienes problemas:

1. **Revisar Issues en GitHub**:
   - [Repositorio del Proyecto](https://github.com/DJoel07/Sistema-Transcripcion-Braille/issues)

2. **Crear un Nuevo Issue**:
   - Incluir: SO, versión de Python, logs de error, pasos para reproducir

3. **Documentación Adicional**:
   - [Manual de Usuario](../06-manual-usuario/guia-usuario.md)
   - [Casos de Prueba](../04-casos-prueba/)

---

## 📝 Notas Finales

- Para entornos de producción, considerar usar un servidor WSGI (gunicorn, uWSGI)
- Cambiar `SECRET_KEY` en `.env` para producción
- Configurar HTTPS para despliegues públicos
- La carpeta `venv/` no debe subirse a Git (ya está en `.gitignore`)

## 🔐 Consideraciones de Seguridad

### Para Entornos de Producción

Si planeas desplegar la aplicación en un entorno público, considera:

#### 1. Variables de Entorno Seguras

```bash
# Generar SECRET_KEY segura
python -c "import secrets; print(secrets.token_hex(32))"

# Agregar al .env
SECRET_KEY=tu_clave_generada_aqui_64_caracteres
```

#### 2. HTTPS

Para producción, usa HTTPS. Opciones:

**Opción A: Usar servidor proxy reverso (Recomendado)**
```bash
# Nginx con Let's Encrypt
sudo apt install nginx certbot python3-certbot-nginx
sudo certbot --nginx -d tudominio.com
```

**Opción B: Usar servicio en la nube**
- Azure App Service (HTTPS automático)
- AWS Elastic Beanstalk
- Google Cloud Run
- Heroku

#### 3. Firewall y Puertos

```bash
# Permitir solo puertos necesarios
# UFW (Linux)
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

#### 4. Actualizar Dependencias

```bash
# Revisar vulnerabilidades
pip list --outdated

# Actualizar paquetes
pip install --upgrade Flask reportlab

# Revisar con safety
pip install safety
safety check
```

---

## 🌐 Despliegue en Producción

### Opción 1: Usando Gunicorn (Recomendado)

Gunicorn es un servidor WSGI de producción para aplicaciones Flask.

#### Instalación

```bash
# Agregar a requirements.txt
echo "gunicorn==21.2.0" >> requirements.txt

# Instalar
pip install gunicorn
```

#### Ejecución

```bash
# Desarrollo (1 worker)
gunicorn -w 1 -b 0.0.0.0:5000 app:app

# Producción (4 workers)
gunicorn -w 4 -b 0.0.0.0:5000 --timeout 120 app:app

# Con reload automático (desarrollo)
gunicorn -w 1 -b 0.0.0.0:5000 --reload app:app
```

#### Crear Servicio Systemd (Linux)

```bash
# Crear archivo de servicio
sudo nano /etc/systemd/system/braille-app.service
```

**Contenido**:
```ini
[Unit]
Description=Braille Transcription Service
After=network.target

[Service]
User=tuusuario
WorkingDirectory=/ruta/a/Sistema-Transcripcion-Braille
Environment="PATH=/ruta/a/Sistema-Transcripcion-Braille/venv/bin"
ExecStart=/ruta/a/Sistema-Transcripcion-Braille/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Habilitar y arrancar servicio
sudo systemctl enable braille-app
sudo systemctl start braille-app
sudo systemctl status braille-app
```

### Opción 2: Azure App Service

#### Paso 1: Preparar Aplicación

```bash
# Crear requirements.txt actualizado
pip freeze > requirements.txt

# Crear archivo .deployment (opcional)
echo "[config]" > .deployment
echo "SCM_DO_BUILD_DURING_DEPLOYMENT=true" >> .deployment
```

#### Paso 2: Deploy con Azure CLI

```bash
# Instalar Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login
az login

# Crear grupo de recursos
az group create --name braille-rg --location eastus

# Crear App Service Plan
az appservice plan create --name braille-plan --resource-group braille-rg --sku B1 --is-linux

# Crear Web App
az webapp create --resource-group braille-rg --plan braille-plan --name mi-app-braille --runtime "PYTHON:3.11"

# Deploy desde Git local
az webapp deployment source config-local-git --name mi-app-braille --resource-group braille-rg

# Push código
git remote add azure <url-proporcionada>
git push azure main:master
```

### Opción 3: Docker en Producción

#### Docker Compose para Producción

Crear `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  braille-app:
    build: .
    container_name: braille-prod
    ports:
      - "80:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=${SECRET_KEY}
    restart: unless-stopped
    volumes:
      - ./logs:/usr/src/app/logs
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

#### Ejecutar

```bash
# Construir y ejecutar
docker-compose -f docker-compose.prod.yml up -d

# Ver logs
docker-compose -f docker-compose.prod.yml logs -f

# Detener
docker-compose -f docker-compose.prod.yml down
```

---

## 📊 Monitoreo y Logs

### Configurar Logging

Editar `app.py`:

```python
import logging
from logging.handlers import RotatingFileHandler

# Configurar logging
if not app.debug:
    file_handler = RotatingFileHandler('logs/braille.log', maxBytes=10240000, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Braille Transcriptor startup')
```

### Ver Logs

```bash
# Instalación local
tail -f logs/braille.log

# Docker
docker logs -f braille-app

# Systemd
sudo journalctl -u braille-app -f
```

---

## 🔄 Actualización de la Aplicación

### Actualizar Instalación Local

```bash
# 1. Hacer backup (opcional pero recomendado)
cp -r Sistema-Transcripcion-Braille Sistema-Transcripcion-Braille-backup

# 2. Navegar al directorio
cd Sistema-Transcripcion-Braille

# 3. Guardar cambios locales (si hay)
git stash

# 4. Obtener última versión
git pull origin main

# 5. Activar entorno virtual
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\Activate.ps1  # Windows

# 6. Actualizar dependencias
pip install -r requirements.txt --upgrade

# 7. Reiniciar aplicación
# Si usas systemd:
sudo systemctl restart braille-app

# Si ejecutas manualmente:
# Ctrl+C para detener y luego:
python app.py
```

### Actualizar Docker

```bash
# 1. Detener contenedor actual
docker stop braille-app
docker rm braille-app

# 2. Obtener última versión del código
git pull origin main

# 3. Reconstruir imagen
docker build -t braille-transcriptor:latest .

# 4. Ejecutar nuevo contenedor
docker run -d -p 5000:5000 --name braille-app braille-transcriptor:latest

# O con docker-compose:
docker-compose down
docker-compose build
docker-compose up -d
```

---

## 🧪 Ejecutar Pruebas

### Pruebas Unitarias

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\Activate.ps1  # Windows

# Ejecutar todas las pruebas
python -m unittest discover tests/ -v

# Ejecutar prueba específica
python -m unittest tests.test_comprehensive.TestParticionEquivalencias -v

# Con cobertura
pip install coverage
coverage run -m unittest discover tests/
coverage report
coverage html  # Genera reporte HTML en htmlcov/
```

### Pruebas de Integración

```bash
# Prueba de endpoint
curl http://localhost:5000/

# Prueba de transcripción (requiere jq)
curl -X POST http://localhost:5000/api/transcribe \
  -H "Content-Type: application/json" \
  -d '{"text": "hola"}' | jq

# Prueba de salud (si implementada)
curl http://localhost:5000/health
```

---

## 📱 Acceso Remoto

### Acceso desde Otros Dispositivos en Red Local

#### Configuración

```python
# En app.py, asegurar:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

#### Obtener IP Local

**Windows**:
```powershell
ipconfig
# Buscar "Dirección IPv4"
```

**Linux/Mac**:
```bash
ifconfig | grep "inet "
# o
ip addr show
```

#### Acceder desde Otro Dispositivo

```
http://<IP_DE_TU_PC>:5000

Ejemplo:
http://192.168.1.100:5000
```

#### Firewall

**Windows**: Permitir puerto 5000 en Windows Defender Firewall

**Linux**:
```bash
sudo ufw allow 5000/tcp
```

**macOS**: System Preferences → Security & Privacy → Firewall Options

---

## 🔧 Configuración Avanzada

### Variables de Entorno Completas

Crear archivo `.env` en raíz del proyecto:

```ini
# Flask
FLASK_APP=app.py
FLASK_ENV=production
FLASK_DEBUG=0

# Server
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Security
SECRET_KEY=tu-clave-secreta-muy-larga-y-segura-aqui

# PDF Generation
PDF_MAX_SIZE=10485760  # 10MB
PDF_TIMEOUT=30  # segundos

# Transcription
MAX_TEXT_LENGTH=500
ALLOW_SPECIAL_CHARS=false

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/braille.log
LOG_MAX_BYTES=10485760
LOG_BACKUP_COUNT=10
```

### Cargar Variables de Entorno

```python
# En app.py
from dotenv import load_dotenv
import os

load_dotenv()

# Usar variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-default')
MAX_TEXT_LENGTH = int(os.getenv('MAX_TEXT_LENGTH', 500))
```

---

## 📦 Backup y Restauración

### Backup Manual

```bash
# Backup completo
tar -czf braille-backup-$(date +%Y%m%d).tar.gz Sistema-Transcripcion-Braille/

# Solo código y configuración (excluir venv)
tar -czf braille-backup-$(date +%Y%m%d).tar.gz \
  --exclude='venv' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  Sistema-Transcripcion-Braille/
```

### Backup Automatizado (Linux)

```bash
# Crear script de backup
nano /home/usuario/backup-braille.sh
```

```bash
#!/bin/bash
BACKUP_DIR="/home/usuario/backups"
APP_DIR="/home/usuario/Sistema-Transcripcion-Braille"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR
cd $APP_DIR/..
tar -czf $BACKUP_DIR/braille-$DATE.tar.gz \
  --exclude='venv' \
  --exclude='__pycache__' \
  Sistema-Transcripcion-Braille/

# Mantener solo últimos 7 backups
cd $BACKUP_DIR
ls -t | tail -n +8 | xargs -r rm

echo "Backup completed: braille-$DATE.tar.gz"
```

```bash
# Hacer ejecutable
chmod +x /home/usuario/backup-braille.sh

# Agregar a cron (diario a las 2 AM)
crontab -e
# Agregar línea:
0 2 * * * /home/usuario/backup-braille.sh
```

### Restauración

```bash
# Detener servicio
sudo systemctl stop braille-app  # si usas systemd
# o detener manualmente

# Extraer backup
tar -xzf braille-backup-20251125.tar.gz

# Restaurar ubicación
mv Sistema-Transcripcion-Braille /ruta/original/

# Reinstalar dependencias
cd Sistema-Transcripcion-Braille
source venv/bin/activate
pip install -r requirements.txt

# Reiniciar servicio
sudo systemctl start braille-app
```

---

## 🎓 Recursos Adicionales

### Documentación Relacionada

- [Manual de Usuario](../06-manual-usuario/guia-usuario.md) - Para usuarios finales
- [Documentación de Dockerización](../02-ambiente-desarrollo/dockerizacion.md) - Guía completa de Docker
- [Plan de Pruebas](../04-casos-prueba/plan-pruebas.md) - Casos de prueba documentados
- [Diseño Arquitectónico](../01-diseno-arquitectonico/diseno-arquitectonico.md) - Arquitectura del sistema

### Comunidad y Soporte

- **GitHub**: [DJoel07/Sistema-Transcripcion-Braille](https://github.com/DJoel07/Sistema-Transcripcion-Braille)
- **Issues**: Reportar bugs y solicitar features
- **Discussions**: Preguntas y discusiones

### Aprender Más

- **Flask**: https://flask.palletsprojects.com/
- **Docker**: https://docs.docker.com/
- **Python**: https://docs.python.org/3/
- **ReportLab**: https://www.reportlab.com/docs/reportlab-userguide.pdf

---

**Última actualización**: 2025-11-25  
**Versión del documento**: 2.0  
**Mantenedor**: Equipo de Desarrollo
