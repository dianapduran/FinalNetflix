from fastapi import APIRouter, Depends
from typing import List
from schemas.user import UserCreate, UserResponse
from services.usuarios_service import obtener_usuarios, crear_usuario, obtener_usuario_por_id
from auth.deps import get_current_user, rol_requerido

router = APIRouter()

@router.get("/usuarios", response_model=List[UserResponse])
async def listar_usuarios(skip: int = 0, limit: int = 100, _ =Depends(rol_requerido("admin"))):
    return obtener_usuarios(skip=skip, limit=limit)

@router.post("/usuarios", response_model=UserResponse, status_code=201)
async def crear(usuario: UserCreate):
    return crear_usuario(usuario)

@router.get("/usuarios/{id}", response_model=UserResponse)
async def get_usuario(id:int):
    return obtener_usuario_por_id(id)


"""@router.get("/usuarios/{id}", response_model=UserResponse)
async def get_usuario(id: int, usuario_actual: UserResponse = Depends(obtener_usuario_actual)):
    return obtener_usuario_por_id(id)"""