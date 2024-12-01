from typing import List
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

class Observador:
    def actualizar(self, temperatura: float) -> None:
        pass

class SensorDeTemperatura:
    def __init__(self) -> None:
        self._observadores: List[Observador] = []
        self._temperatura: float = 0.0

    def agregar_observador(self, observador: Observador) -> None:
        self._observadores.append(observador)
        print(Fore.GREEN + f"Observador {observador.__class__.__name__} agregado.")

    def eliminar_observador(self, observador: Observador) -> None:
        self._observadores.remove(observador)
        print(Fore.YELLOW + f"Observador {observador.__class__.__name__} eliminado.")

    def establecer_temperatura(self, temperatura: float) -> None:
        self._temperatura = temperatura
        print(Fore.CYAN + f"Temperatura establecida a {temperatura:.2f} ºC")
        self._notificar_observadores()

    def _notificar_observadores(self) -> None:
        for observador in self._observadores:
            observador.actualizar(self._temperatura)

class ObservadorCelsius(Observador):
    def __init__(self, sensor: SensorDeTemperatura) -> None:
        self._sensor = sensor

    def actualizar(self, temperatura: float) -> None:
        if temperatura > 50:
            print(Fore.RED + f"[ALERTA] La temperatura en grados Celsius es de {temperatura:.2f} ºC")
        elif temperatura < 5:
            print(Fore.BLUE + f"[ALERTA] La temperatura en grados Celsius es de {temperatura:.2f} ºC")
        else:
            print(f"La temperatura en grados Celsius es de {temperatura:.2f} ºC")
        
        # Ajustar la temperatura si excede los 28 grados Celsius
        if temperatura > 28:
            print(Fore.MAGENTA + f"[AJUSTE] La temperatura es demasiado alta ({temperatura:.2f} ºC). Ajustando a 22.0 ºC.")
            self._sensor.establecer_temperatura(22.0)

# Ejemplo de uso

if __name__ == "__main__":
    sensor = SensorDeTemperatura()
    observador_celsius = ObservadorCelsius(sensor)
    
    # Agregar observador
    sensor.agregar_observador(observador_celsius)
    
    # Establecer temperaturas
    sensor.establecer_temperatura(25.0)
    sensor.establecer_temperatura(30.0)
    sensor.establecer_temperatura(35.0)
    sensor.establecer_temperatura(40.0)
    sensor.establecer_temperatura(45.0)
    sensor.establecer_temperatura(50.0)
    sensor.establecer_temperatura(55.0)
    sensor.establecer_temperatura(60.0)
    sensor.establecer_temperatura(65.0)
    sensor.establecer_temperatura(70.0)
    sensor.establecer_temperatura(75.0)
    sensor.establecer_temperatura(80.0)
    sensor.establecer_temperatura(85.0)


