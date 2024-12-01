# Ejemplo del Patrón Observer con Sensor de Temperatura

Este proyecto implementa el patrón de diseño Observer utilizando un ejemplo de sensor de temperatura. El objetivo es demostrar cómo los observadores pueden reaccionar a los cambios en el estado de un objeto (en este caso, la temperatura).

## Descripción del Código

### Clases Principales

#### Observador

```python
class Observador:
    def actualizar(self, temperatura: float) -> None:
        pass
```

#### Sujeto

```python
class Sujeto:
    def __init__(self) -> None:
        self.observadores = []

    def agregar_observador(self, observador: Observador) -> None:
        self.observadores.append(observador)

    def eliminar_observador(self, observador: Observador) -> None:
        self.observadores.remove(observador)

    def notificar_observadores(self, temperatura: float) -> None:
        for observador in self.observadores:
            observador.actualizar(temperatura)
```

#### SensorTemperatura

```python
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
```

### Observador Celsius

```python
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
```

## Explicación

La clase ObservadorCelsius implementa la interfaz Observador y define cómo debe reaccionar cuando se notifica un cambio en la temperatura. Si la temperatura excede los 28 grados Celsius, ajusta la temperatura a 22 grados Celsius

El SensorDeTemperatura es el Sujeto que notifica a los observadores cuando la temperatura cambia. En este caso, solo hay un observador (ObservadorCelsius) que reacciona a los cambios en la temperatura.

## Resultado Esperado

El programa establece la temperatura a 30 grados Celsius, lo que activa la alerta de temperatura alta y ajusta la temperatura a 22 grados Celsius.

```bash
Observador ObservadorCelsius agregado.
Temperatura establecida a 30.00 ºC
[ALERTA] La temperatura en grados Celsius es de 30.00 ºC
[AJUSTE] La temperatura es demasiado alta (30.00 ºC). Ajustando a 22.0 ºC.
Temperatura establecida a 22.00 ºC
```

## Conclusión

El patrón Observer es útil cuando se necesita notificar a múltiples observadores sobre los cambios en el estado de un objeto. En este ejemplo, el sensor de temperatura notifica a un observador cuando la temperatura cambia, lo que permite reaccionar a los cambios de manera oportuna.


