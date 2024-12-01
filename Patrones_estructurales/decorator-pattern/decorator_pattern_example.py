
from abc import ABC, abstractmethod
from datetime import datetime
import json
from typing import Dict, Any

# -------------------- 1. Componentes Base del Patrón --------------------
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class BaseLogger(Logger):
    def log(self, message: str) -> None:
        print(message)

class LoggerDecorator(Logger):
    def __init__(self, logger: Logger):
        self._logger = logger
    
    @abstractmethod
    def log(self, message: str) -> None:
        pass

# -------------------- 2. Decoradores Especializados --------------------
class TimestampDecorator(LoggerDecorator):
    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._logger.log(f"[{timestamp}] {message}")

class LevelDecorator(LoggerDecorator):
    def __init__(self, logger: Logger, level: str):
        super().__init__(logger)
        self._level = level.upper()

    def log(self, message: str) -> None:
        self._logger.log(f"[{self._level}] {message}")

class ColorDecorator(LoggerDecorator):
    COLORS = {
        'ERROR': '\033[91m',    # Rojo
        'WARNING': '\033[93m',  # Amarillo
        'INFO': '\033[94m',     # Azul
        'DEBUG': '\033[92m',    # Verde
        'RESET': '\033[0m'
    }

    def __init__(self, logger: Logger, level: str):
        super().__init__(logger)
        self._level = level.upper()

    def log(self, message: str) -> None:
        color = self.COLORS.get(self._level, self.COLORS['RESET'])
        self._logger.log(f"{color}{message}{self.COLORS['RESET']}")

class JsonDecorator(LoggerDecorator):
    def log(self, message: str) -> None:
        log_data = {
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        self._logger.log(json.dumps(log_data))

class PriorityDecorator(LoggerDecorator):
    def __init__(self, logger: Logger, priority: int):
        super().__init__(logger)
        self._priority = priority

    def log(self, message: str) -> None:
        self._logger.log(f"[Priority: {self._priority}] {message}")

# -------------------- 3. Factory y Utilidades --------------------
class LoggerFactory:
    @staticmethod
    def create_logger(config: Dict[str, Any]) -> Logger:
        logger = BaseLogger()
        
        if config.get('timestamp', False):
            logger = TimestampDecorator(logger)
        
        if 'level' in config:
            logger = LevelDecorator(logger, config['level'])
            if config.get('color', False):
                logger = ColorDecorator(logger, config['level'])
        
        if config.get('json', False):
            logger = JsonDecorator(logger)
        
        if 'priority' in config:
            logger = PriorityDecorator(logger, config['priority'])
        
        return logger

# -------------------- 4. Interfaz de Usuario --------------------
def mostrar_menu() -> None:
    print("\n=== Sistema de Logging Dinámico con Decoradores ===")
    print("1. Crear logger personalizado")
    print("2. Ver ejemplos predefinidos")
    print("3. Salir")

def crear_logger_personalizado() -> Logger:
    config = {}
    print("\nConfiguración del logger:")
    
    # Obtener configuración del usuario
    config['level'] = input("Nivel (ERROR/WARNING/INFO/DEBUG): ").upper()
    if config['level'] not in ['ERROR', 'WARNING', 'INFO', 'DEBUG']:
        config['level'] = 'INFO'
        print("Nivel no válido. Usando INFO por defecto.")
    
    config['timestamp'] = input("¿Incluir timestamp? (s/n): ").lower() == 's'
    config['color'] = input("¿Incluir colores? (s/n): ").lower() == 's'
    config['json'] = input("¿Formato JSON? (s/n): ").lower() == 's'
    
    try:
        priority = int(input("Prioridad (1-5): "))
        if 1 <= priority <= 5:
            config['priority'] = priority
    except:
        pass
    
    return LoggerFactory.create_logger(config)

def mostrar_ejemplos() -> None:
    mensaje = "Este es un mensaje de prueba"
    
    # Ejemplo 1: Logger básico
    print("\n1. Logger Básico:")
    logger = LoggerFactory.create_logger({})
    logger.log(mensaje)
    
    # Ejemplo 2: Logger completo
    print("\n2. Logger con todos los decoradores:")
    logger = LoggerFactory.create_logger({
        'timestamp': True,
        'level': 'ERROR',
        'color': True,
        'priority': 1,
        'json': True
    })
    logger.log(mensaje)
    
    # Ejemplo 3: Logger personalizado
    print("\n3. Logger personalizado:")
    logger = LoggerFactory.create_logger({
        'level': 'WARNING',
        'color': True,
        'timestamp': True
    })
    logger.log(mensaje)

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == "1":
            logger = crear_logger_personalizado()
            mensaje = input("\nIngrese su mensaje: ")
            logger.log(mensaje)
        
        elif opcion == "2":
            mostrar_ejemplos()
        
        elif opcion == "3":
            print("\n¡Gracias por usar el Sistema de Logging!")
            break
        
        else:
            print("\nOpción no válida!")

if __name__ == "__main__":
    main()