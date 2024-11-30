# Singleton Pattern Example

Este proyecto demuestra el uso del patrón Singleton en Python utilizando una conexión a una base de datos SQLite.

## Descripción

El archivo `main.py` contiene una implementación del patrón Singleton para gestionar una única instancia de conexión a una base de datos SQLite. La clase `DatabaseSingleton` asegura que solo una instancia de la conexión a la base de datos sea creada y utilizada a lo largo de la aplicación.

## Estructura del Código

- **DatabaseSingleton**: Clase que implementa el patrón Singleton.
  - `__new__(cls)`: Método especial que controla la creación de nuevas instancias.
  - `get_connection()`: Método que devuelve la conexión a la base de datos.

## Uso

El script crea múltiples instancias de `DatabaseSingleton` y verifica que todas las instancias son la misma. También cierra la conexión a la base de datos y verifica que la conexión se ha cerrado correctamente.

## Ejecución

Para ejecutar el script, simplemente corre el archivo `main.py`:

```bash
python main.py
```

## Salida

A continuación, se muestra un ejemplo de la salida del script:
  
  ```bash
Instancia 0: Es la misma instancia
Conexión de instancia 0: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 1: Es la misma instancia
Conexión de instancia 1: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 2: Es la misma instancia
Conexión de instancia 2: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 3: Es la misma instancia
Conexión de instancia 3: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 4: Es la misma instancia
Conexión de instancia 4: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 5: Es la misma instancia
Conexión de instancia 5: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 6: Es la misma instancia
Conexión de instancia 6: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 7: Es la misma instancia
Conexión de instancia 7: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 8: Es la misma instancia
Conexión de instancia 8: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 9: Es la misma instancia
Conexión de instancia 9: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 10: Es la misma instancia
Conexión de instancia 10: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 11: Es la misma instancia
Conexión de instancia 11: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 12: Es la misma instancia
Conexión de instancia 12: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 13: Es la misma instancia
Conexión de instancia 13: <sqlite3.Connection object at 0x0000023C74294E50>
Instancia 14: Es la misma instancia
Conexión de instancia 14: <sqlite3.Connection object at 0x0000023C74294E50>
Conexión cerrada correctamente: Cannot operate on a closed database.

```
