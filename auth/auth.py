from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from services.usuarios_service import autenticar_usuario
from auth.jwt_handler import crear_token
from schemas.user import UserIn

router = APIRouter()

@router.post("/login")
async def login(user: UserIn):
    usuario = autenticar_usuario(user.email, user.password)
    if not usuario:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    
    print(usuario)
    token = crear_token({"sub": str(usuario.get("id")), "rol" : usuario.get("rol")})
    return {"access_token": token, "token_type": "bearer"}
