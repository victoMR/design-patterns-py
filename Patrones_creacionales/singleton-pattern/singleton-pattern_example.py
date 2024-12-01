import sqlite3
from sqlite3 import Connection
import os

# Obtener el directorio donde se encuentra este archivo
path = os.path.dirname(os.path.abspath(__file__))
print(f"Directorio del archivo actual: {path}")

class DatabaseSingleton:
    _instance = None  # Variable de clase para almacenar la única instancia de la clase
    _connection = None  # Variable de clase para almacenar la conexión a la base de datos

    def __new__(cls):
        """
        Método especial para controlar la creación de nuevas instancias.
        Si la instancia no existe, la crea y establece la conexión a la base de datos.
        """
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            # Usar el path inicial para la base de datos
            cls._connection = sqlite3.connect(os.path.join(path, 'database.db'))
        return cls._instance

    def get_connection(self) -> Connection:
        """
        Devuelve la conexión a la base de datos.
        """
        return self._connection

# Ejemplo de uso
if __name__ == "__main__":
    # Crear varias instancias de la clase DatabaseSingleton
    dataBaseInstances = [DatabaseSingleton() for _ in range(15)]
    
    # Comprobar que todas las instancias son la misma
    for i, db in enumerate(dataBaseInstances):
        print(f"Instancia {i}: {'Es la misma instancia' if db == dataBaseInstances[0] else 'No es la misma instancia'}")
        print(f"Conexión de instancia {i}: {db.get_connection()}")
    
    # Cerrar la conexión a la base de datos
    dataBaseInstances[0].get_connection().close()
    
    # Comprobar que la conexión se ha cerrado
    try:
        dataBaseInstances[0].get_connection().execute("SELECT 1")
    except sqlite3.ProgrammingError as e:
        print(f"Conexión cerrada correctamente: {e}")