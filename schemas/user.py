# app/models/user.py
from pydantic import BaseModel, EmailStr, Field


# Para crear un usuario
class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    contrasena: str

# Para devolver info de un usuario (sin contraseña)
class UserResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr

# Para loguear un usuario
class UserIn(BaseModel):
    email: str
    password: str