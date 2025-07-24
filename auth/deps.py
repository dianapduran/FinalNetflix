from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verificar_token
from services.usuarios_service import obtener_usuario_por_id
from schemas.user import UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    return payload


def rol_requerido(rol: str):
    def validador(usuario=Depends(get_current_user)):
        print("usuario desde rol")
        print(type(usuario))
        print(usuario)
        if usuario.get("rol") != rol:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos suficientes"
            )
        return usuario
    
    return validador