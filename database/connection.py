import os
import pyodbc

from config import settings

class ConnectionFactory:
    @staticmethod
    def create_connection():
        try:
            if settings.db_auth_mode == "sql":
                conn_str = f'''
                    DRIVER={settings.driver};
                    SERVER={settings.server};
                    DATABASE={settings.database};
                    UID={settings.username};
                    PWD={settings.password};
                '''
            elif settings.db_auth_mode == "windows":
                conn_str = f'''
                    DRIVER={settings.driver};
                    SERVER={settings.server};
                    DATABASE={settings.database};
                    Trusted_Connection=yes;
                '''
            else:
                raise ValueError(f"Modo de autenticación inválido: {settings.db_auth_mode}")

            return pyodbc.connect(conn_str)

        except pyodbc.Error as e:
            print("❌ Error al conectar a la base de datos:")
            print(e)
            raise