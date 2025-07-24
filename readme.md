# 🎬 Curso: Desarrollo de Backend Netflix con FastAPI

## 📌 Descripción

Este curso práctico de **16 horas** te enseñará a construir un backend completo para una plataforma de streaming tipo **Netflix** utilizando **FastAPI** y **SQL Server**. Aprenderás desde los fundamentos hasta técnicas avanzadas de desarrollo de APIs, trabajando directamente con **SQL** y siguiendo **buenas prácticas** de la industria.

---

## 📚 Estructura del Curso

### Clase 1: Introducción y Fundamentos
- Presentación del proyecto y arquitectura tipo Netflix
- Configuración del entorno de desarrollo
- Introducción a FastAPI y sus ventajas
- Primera API "Hola Mundo"
- Documentación automática con Swagger/OpenAPI

### Clase 2: Conexión a SQL SERVER
- Revisión y diseño de la base de datos
- Conexión directa a SQL Server
- Uso de `pyodbc` / `asyncpg` para consultas
- Queries SQL básicas desde FastAPI
- Manejo de conexiones y pool

### Clase 3: Endpoints de Usuarios
- Creación de endpoints (CRUD parcial)
- Validación con Pydantic
- Manejo de errores en SQL
- Pruebas desde Swagger UI

### Clase 4: Endpoints de Contenido
- CRUD para películas y series
- Consultas relacionales y Joins

### Clase 5: Autenticación y Seguridad
- Registro y login de usuarios
- Implementación de JWT
- Protección de rutas
- Roles y permisos básicos
- Mejores prácticas en seguridad API

### Clase 6: Funcionalidades Avanzadas - Parte 1
- Sistema de visualizaciones por usuario
- Recomendaciones básicas con SQL
- Búsqueda, filtrado y paginación

### Clase 7: Funcionalidades Avanzadas - Parte 2
- Subida y servicio de imágenes (posters)
- Caché básico para rendimiento
- Logging y monitoreo
- Pruebas de endpoints
- Documentación extendida

### Clase 8: Frontend Básico y Despliegue
- Introducción a HTML/JS para consumir la API
- Conexión desde el frontend a FastAPI
- Preparación para producción
- Despliegue en Railway o plataforma similar
- Proyecto final y cierre

---

## 🧠 Metodología

Cada clase de 2 horas incluye:

- **45 minutos** de teoría con ejemplos reales
- **75 minutos** de práctica guiada
- Uso intensivo de **SQL directo**, explicado paso a paso
- Construcción incremental del proyecto
- Enfoque en **consultas eficientes** y **buenas prácticas**

---

## 💻 Requisitos Técnicos

- Python 3.7 o superior
- VS Code (con extensiones sugeridas)
- SQL Server (local o remoto)
- Conocimientos básicos de Python y SQL
- Familiaridad básica con APIs REST (opcional)

---

## ✅ Resultado Final

Al finalizar, contarás con:

- Una **API REST funcional estilo Netflix**
- Integración directa con **SQL Server**
- Endpoints seguros y bien documentados
- Frontend básico conectado a la API
- Proyecto desplegado en la nube (ej. Railway)
- Habilidades sólidas en FastAPI y SQL nativo

---

## ⚙️ Instalación y Configuración

```bash
# 1. Clonar el repositorio
git clone https://github.com/cmestradap/curso_fast_api
cd curso_fast_api

# 2. Crear entorno virtual
python -m venv fast_api_venv

# 3. Activar entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Configurar variables de entorno
# Crear un archivo .env con el siguiente contenido:
# DATABASE_URL=SQL Server://usuario:password@localhost/netflix_db
# SECRET_KEY=tu_clave_secreta
# DEBUG=True

# 6. Ejecutar la aplicación
uvicorn app.main:app --reload
