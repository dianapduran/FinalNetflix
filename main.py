from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from routers import contenidos, users
from auth import auth
from web import home_web
from web.auth_web import router as auth_router
from web.dashboard_web import router as dash_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="Netflix API",
    description="API Backend para plataforma tipo Netflix",
    version="1.0.0"
)

# Configurar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Definir esquema de seguridad para Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Demo JWT",
        version="1.0.0",
        description="API con JWT y rutas protegidas",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"bearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(contenidos.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(home_web.router)
app.include_router(auth_router, tags=["web-auth"])
app.include_router(dash_router, tags=["dash-router"])

# Endpoint principal
@app.get("/")
async def root():
    return {
        "mensaje": "¡Bienvenido a Netflix API!",
        "estado": "online",
        "version": "1.0.0",
        "documentacion": "/docs"
    }


