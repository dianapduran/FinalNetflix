from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from services.usuarios_service import autenticar_usuario, crear_usuario
from schemas.user import UserResponse, UserCreate
from auth.jwt_handler import crear_token

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
async def login_form(request: Request):
    return templates.TemplateResponse("auth/login.html", {
        "request": request,
        "title": "Iniciar Sesión"
    })

@router.post("/web/login")
async def login_submit(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    try:
        # Reutilizar tu servicio existente
        print(email)
        print(password)
        usuario = autenticar_usuario(email, password)
        
        
        if not usuario:
            return templates.TemplateResponse("auth/login.html", {
                "request": request,
                "title": "Iniciar Sesión",
                "error": "Credenciales inválidas",
                "email": email  # Mantener email en el form
            })
        
        # Crear token usando tu función existente
        token = crear_token({"sub": str(usuario.get("id")), "rol": usuario.get("rol")})
        
        # Redirigir al dashboard con cookie
        response = RedirectResponse(url="/dashboard", status_code=302)
        response.set_cookie(
            key="access_token", 
            value=f"Bearer {token}",
            httponly=True,
            max_age=1800  # 30 minutos
        )
        return response
        
    except Exception as e:
        return templates.TemplateResponse("auth/login.html", {
            "request": request,
            "title": "Iniciar Sesión",
            "error": "Error interno del servidor",
            "email": email
        })

@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=302)
    response.delete_cookie("access_token")
    return response

@router.get("/register")
async def login_form(request: Request):
    return templates.TemplateResponse("registrarse.html", {
        "request": request,
        "title": "Iniciar Sesión"
    })
    
@router.post("/register")
async def register_submit(
    request: Request,
    nombre: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    try:
        # Reutilizar tu servicio existente
        print(nombre)
        print(email)
        print(password)
        registrar_usuario: UserCreate
        
        
        registrar_usuario = UserCreate(nombre=nombre, email=email, contrasena=password) 
        print(registrar_usuario)
       
   
        usuario_creado=crear_usuario(registrar_usuario)
        
        return templates.TemplateResponse("auth/login.html", {
            "request": request,
            "title": "Iniciar Sesión"
        })
        
    except Exception as e:
        return templates.TemplateResponse("auth/login.html", {
            "request": request,
            "title": "Iniciar Sesión",
            "error": "Error interno del servidor",
            "email": email
        })
        
    #     if not usuario:
    #         return templates.TemplateResponse("auth/login.html", {
    #             "request": request,
    #             "title": "Iniciar Sesión",
    #             "error": "Credenciales inválidas",
    #             "email": email  # Mantener email en el form
    #         })
        
    #     # Crear token usando tu función existente
    #     token = crear_token({"sub": str(usuario.get("id")), "rol": usuario.get("rol")})
        
    #     # Redirigir al dashboard con cookie
    #     response = RedirectResponse(url="/dashboard", status_code=302)
    #     response.set_cookie(
    #         key="access_token", 
    #         value=f"Bearer {token}",
    #         httponly=True,
    #         max_age=1800  # 30 minutos
    #     )
    #     return response
        
    # except Exception as e:
    #     return templates.TemplateResponse("auth/login.html", {
    #         "request": request,
    #         "title": "Iniciar Sesión",
    #         "error": "Error interno del servidor",
    #         "email": email
    #     })