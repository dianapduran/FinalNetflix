from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from services.contenidos_service import obtener_contenidos

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/home")
async def home(request: Request):
    contenidos = obtener_contenidos()
    print("CONTENIDOS CARGADOS:", len(contenidos))  # ver en terminal
    return templates.TemplateResponse("home.html", {
        "request": request,
        "contenidos": contenidos  # 👈 MUY IMPORTANTE
    })
