-- 1. Agregar la columna 'rol' a la tabla
ALTER TABLE Profe.dbo.usuarios
ADD rol VARCHAR(50) DEFAULT 'usuario';

-- 2. Actualizar todos los registros existentes con el rol 'usuario'
UPDATE Profe.dbo.usuarios
SET rol = 'usuario';
