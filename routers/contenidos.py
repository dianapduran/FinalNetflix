from fastapi import APIRouter
from typing import List
from schemas.contenido import ContenidoOut
from services.contenidos_service import obtener_contenidos

router = APIRouter()

@router.get("/contenidos", response_model=List[ContenidoOut])
def listar_contenidos():
    return obtener_contenidos()