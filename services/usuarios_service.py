from database.connection import ConnectionFactory
from schemas.user import UserResponse, UserCreate
from fastapi import HTTPException, status

def obtener_usuarios(skip: int = 0, limit: int = 100):
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
                    SELECT id, nombre, email
                    FROM usuarios
                    ORDER BY id
                    OFFSET ? ROWS
                    FETCH NEXT ? ROWS ONLY
                    """,
        (skip, limit),
    )
    rows = cursor.fetchall()
    return [
        UserResponse(
            id=row[0],
            nombre=row[1],
            email=row[2],
        )
        for row in rows
    ]


def crear_usuario(usuario: UserCreate) -> UserResponse:
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nombre, email, contrasena)
        OUTPUT INSERTED.id, INSERTED.nombre, INSERTED.email
        VALUES (?, ?, ?)
    """, (usuario.nombre, usuario.email, usuario.contrasena))

    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return UserResponse(
        id=row.id,
        nombre=row.nombre,
        email=row.email
    )

def obtener_usuario_por_id(user_id: int) -> UserResponse:
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT id, nombre, email
                   FROM usuarios
                   WHERE id = ?""", (user_id))
    
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con id {user_id} no encontrado"
        )
    
    return UserResponse(
        id=row.id,
        nombre=row.nombre,
        email=row.email

    )

def autenticar_usuario(email: str, password: str):
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()

    query = """
    SELECT id, nombre, email, rol
    FROM usuarios
    WHERE email = ? AND contrasena = ?
    """

    cursor.execute(query, (email, password))
    row = cursor.fetchone()
    conn.close()

    if row:
        print("Encuentro usuario")
        print(row.id)
        return {
            "id": row.id,
            "username": row.nombre,
            "email": row.email,
            "rol": row.rol
        }
    
    return None